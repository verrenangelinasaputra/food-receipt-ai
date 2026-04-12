import json
from datetime import date, timedelta

from groq import Groq

from .vector_db import VectorDB
from .embedder  import embed_text
import os 
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

def answer_question(question: str, db: VectorDB) -> str:
    all_receipts = db.get_all_metadata()

    if not all_receipts:
        return "📭 Your receipt database is empty. Please upload some receipts first!"

    # Semantic search
    q_vec      = embed_text(question)
    top_matches = db.query(q_vec, top_k=min(5, len(db.store)))
    top_ids    = [m[0] for m in top_matches]

    today      = date.today()
    yesterday  = (today - timedelta(days=1)).isoformat()
    week_start = (today - timedelta(days=7)).isoformat()

    receipts_json = json.dumps(all_receipts, indent=2, ensure_ascii=False)

    system_prompt = f"""You are a helpful food expense assistant.
You have access to the user's complete food receipt database.
Answer questions accurately, concisely, and in a friendly tone.

Date context:
- Today      : {today.isoformat()}
- Yesterday  : {yesterday}
- 7 days ago : {week_start}

When answering:
- Format currency as "Rp X,XXX" (Indonesian Rupiah).
- Use bullet points for lists.
- If no matching data exists, say so clearly.
- Cite the restaurant and date for each relevant purchase."""

    user_prompt = f"""Receipt database:
<receipts>
{receipts_json}
</receipts>

Most relevant receipts for this query (IDs): {top_ids}

Question: {question}"""

    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
    )

    return response.choices[0].message.content