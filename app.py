try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="VReceipt Tracker",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="expanded",
)

from modules.vector_db import VectorDB
from modules.extractor import extract_receipt
from modules.embedder  import embed_text
from modules.ai_chat_menu   import answer_question
import modules.styles  as styles

st.markdown(styles.CSS, unsafe_allow_html=True)

if "chat_history"   not in st.session_state:
    st.session_state.chat_history   = []
if "last_extracted" not in st.session_state:
    st.session_state.last_extracted = None


@st.cache_resource
def get_db() -> VectorDB:
    return VectorDB(path="data/vector_db.json")

db = get_db()

def build_text_repr(r: dict) -> str:
    items_str = ", ".join(
        f"{i['name']} Rp{i.get('price', 0)}" for i in r.get("items", [])
    )
    return (
        f"Restaurant: {r.get('restaurant','?')} | "
        f"Date: {r.get('date','?')} | "
        f"Items: {items_str} | "
        f"Total: Rp{r.get('total', 0)}"
    )


def render_receipt_card(r: dict):
    items_html = "".join(
        f'<div class="item-row">'
        f'<span>{i.get("name","?")}</span>'
        f'<span class="item-price">Rp {int(i.get("price", 0)):,}</span>'
        f'</div>'
        for i in r.get("items", [])
    )
    st.markdown(
        f"""
        <div class="receipt-card">
          <div class="receipt-header">
            <div class="restaurant-name">🍽️ {r.get('restaurant','Unknown')}</div>
            <div class="receipt-meta">📅 {r.get('date','Unknown date')}</div>
          </div>
          <div class="items-section">{items_html}</div>
          <div class="total-row">
            <span>TOTAL</span>
            <span class="total-amount">Rp {int(r.get('total',0)):,}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with st.sidebar:
    st.markdown("## 🧾 VReceipt Tracker")
    st.caption("by Verren Angelina Saputra")
    st.divider()

    page = st.radio(
        "nav",
        ["📤  Upload Your Receipt 📤", "🗃️  Database 🗃️", "💬  Chat with AI 💬"],
        label_visibility="collapsed",
    )

    st.divider()

# Page 1: Upload 

if page == "📤  Upload Your Receipt 📤":
    st.markdown("## 📤 Upload Your Receipt 📤")

    col_left, col_right = st.columns(2, gap="large")

    with col_left:
        st.markdown("### Receipt Image")
        uploaded = st.file_uploader(
            "Upload image",
            type=["jpg", "jpeg", "png", "webp"],
            label_visibility="collapsed",
        )

        if uploaded:
            st.image(uploaded, caption=uploaded.name, use_container_width=True)
            st.markdown("")
            c1, c2 = st.columns(2)
            do_extract = c1.button("Extract", type="primary", use_container_width=True)
            do_reset   = c2.button("Reset",                   use_container_width=True)

            if do_reset:
                st.session_state.last_extracted = None
                st.rerun()

            if do_extract:
                with st.spinner("Analyzing receipt..."):
                    try:
                        data = extract_receipt(uploaded)
                        if data:
                            vec = embed_text(build_text_repr(data))
                            rid = f"{uploaded.name}__{data.get('date','x')}"
                            db.upsert(rid, vec, metadata=data)
                            db.save()
                            st.session_state.last_extracted = data
                            st.success("Extracted and saved!")
                            st.rerun()
                        else:
                            st.error("Could not read receipt. Try a clearer image.")
                    except Exception as e:
                        st.error(f"Error: {e}")
        else:
            st.markdown(
                '<div class="upload-hint">📎 Drop any Image Format or WEBP file here</div>',
                unsafe_allow_html=True,
            )

    with col_right:
        st.markdown("### Extracted Data")
        if st.session_state.last_extracted:
            render_receipt_card(st.session_state.last_extracted)
        else:
            st.markdown(
                '<div class="empty-state">Upload and extract a receipt</div>',
                unsafe_allow_html=True,
            )


# Page 2: Database 

elif page == "🗃️  Database 🗃️":
    st.markdown("## 🗃️ Database 🗃️")

    if not db.store:
        st.info("No receipts stored yet.")
    else:
        records = db.get_all_metadata()
        total_spent = sum(int(r.get("total", 0)) for r in records)
        n_rest = len({r.get("restaurant","?") for r in records})

        c1, c3 = st.columns(2)
        c1.metric("Total Receipts",  len(records))
        c3.metric("Total Spent",     f"Rp {total_spent:,}")
        st.divider()

        # Table with delete button per row
        col_r, col_d, col_i, col_t, col_a = st.columns([2, 1.5, 3, 1.5, 1])
        col_r.markdown("**Restaurant**")
        col_d.markdown("**Date**")
        col_i.markdown("**Items**")
        col_t.markdown("**Total**")
        col_a.markdown("**Action**")
        st.divider()

        for rid, v in list(db.store.items()):
            m = v["metadata"]
            col_r, col_d, col_i, col_t, col_a = st.columns([2, 1.5, 3, 1.5, 1])
            col_r.write(m.get("restaurant", "?"))
            col_d.write(m.get("date", "?"))
            col_i.write(", ".join(i["name"] for i in m.get("items", [])))
            col_t.write(f"Rp {int(m.get('total', 0)):,}")
            if col_a.button("Delete", key=f"del_{rid}"):
                db.delete(rid)
                db.save()
                st.success("Deleted.")
                st.rerun()

# Page 3: Ask AI 

elif page == "💬  Chat with AI 💬":
    st.markdown("## 💬 Chat with AI 💬")

    st.markdown("**Quick questions:**")
    quick = [
        "What food did I buy yesterday?",
        "Give me total expenses for food on 2024-06-20",
        "Where did I buy hamburger in the last 7 days?",
    ]
    qc = st.columns(3)
    for i, q in enumerate(quick):
        if qc[i % 3].button(q, key=f"qq{i}", use_container_width=True):
            st.session_state.chat_history.append({"role": "user", "content": q})
            with st.spinner("Thinking..."):
                reply = answer_question(q, db)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            st.rerun()

    st.divider()

    if not st.session_state.chat_history:
        st.markdown(
            '<div class="empty-state">Click the quick question above or type below.</div>',
            unsafe_allow_html=True,
        )
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("You can ask anything about your receipts...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("Thinking..."):
            reply = answer_question(user_input, db)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

    if st.session_state.chat_history:
        st.markdown("")
        if st.button("Clear chat"):
            st.session_state.chat_history = []
            st.rerun()