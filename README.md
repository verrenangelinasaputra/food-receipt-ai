# 🧾 VReceipt Tracker

VReceipt Tracker is an AI-powered food receipt management platform. Upload your receipt images, let AI extract the data automatically, store them, and ask questions about your spending in plain language.

---

## 📹 Demo Video

Coding No 1
https://drive.google.com/file/d/14-jp-YDLLZl2LUchrN-ZnW_KAx1T3unG/view?usp=sharing

Coding No 2 & 3
https://drive.google.com/file/d/1ZRwUBj-mjVKlXsB8gcM_1ph9Lk8zti9j/view?usp=sharing

Coding No 4
https://drive.google.com/file/d/1mtnPLUqxpdFLUQqXKyd-zLs0v0JtCaLu/view?usp=sharing

Coding No 5
https://drive.google.com/file/d/1ML0x6L3fwdiU64hnxfPWrmwhHLipUCQZ/view?usp=sharing 

---

## ✨ Features

- **Upload Receipt** — Upload JPG/PNG/WEBP receipt images
- **AI Extraction** — Automatically extracts restaurant name, items, prices, and date using Groq Vision
- **Database** — View and manage all stored receipts
- **Chat with AI** — Ask natural language questions like "What did I buy yesterday?" or "How much did I spend last week?"

---

## 💬 Example Questions

- *"What food did I buy yesterday?"*
- *"Give me total expenses for food on 2024-06-20"*
- *"Where did I buy hamburger in the last 7 days?"*

---

## 🛠️ Tech Stack

- **UI** — Streamlit
- **Vision / OCR** — Groq Llama 4 Scout Vision
- **AI Chat** — Groq Llama 3.3 70B
- **Vector Search** — Custom cosine similarity implementation (pure NumPy)
- **Storage** — JSON-backed Vector Database (built from scratch)
- **Container** — Docker
- **CI/CD** — GitHub Actions → Docker Hub

---

## 🚀 How to Run

```bash
# Pull from Docker Hub
docker run -p 8501:8501 \
  -e GROQ_API_KEY=your_key_here \
  verrenangelinas/receipt-ai:latest
```

Open **http://localhost:8501**

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Free API key from [console.groq.com](https://console.groq.com) |

---

## 👩‍💻 Author

**Verren Angelina Saputra**
