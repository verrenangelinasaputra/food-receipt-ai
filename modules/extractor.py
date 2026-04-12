import base64
import json
import re
from datetime import date
import os 

from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

def extract_receipt(uploaded_file) -> dict | None:
    """
    Send the uploaded Streamlit file to Groq Llama 4 Scout Vision.
    Returns a dict with keys: restaurant, date, items, total, currency
    """
    client = Groq(api_key=GROQ_API_KEY)  # reads GROQ_API_KEY from env

    # Read raw bytes and build a data-URL for Groq's OpenAI-compatible API
    raw_bytes  = uploaded_file.read()
    b64_data   = base64.standard_b64encode(raw_bytes).decode("utf-8")
    media_type = uploaded_file.type or "image/jpeg"
    data_url   = f"data:{media_type};base64,{b64_data}"

    today = date.today().isoformat()

    user_prompt = f"""You are a receipt OCR and data extraction expert.
Analyze this food/grocery receipt image and extract ALL data.
Today's date is {today}.

Return ONLY a JSON object — no markdown fences, no explanation — in exactly this schema:
{{
  "restaurant": "store or restaurant name",
  "date": "YYYY-MM-DD (use {today} if not visible)",
  "items": [
    {{"name": "item name", "price": 12000}},
    ...
  ],
  "total": 50000,
  "currency": "IDR"
}}

Rules:
- prices must be plain numbers (no currency symbols, no commas)
- If a price is ambiguous, use 0
- Include every line item visible
- Return ONLY the JSON object, nothing else"""

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": data_url},
                    },
                    {
                        "type": "text",
                        "text": user_prompt,
                    },
                ],
            }
        ],
    )

    raw_text = response.choices[0].message.content.strip()
    clean = re.sub(r"^```[a-zA-Z]*\n?", "", raw_text)
    clean = re.sub(r"\n?```$", "", clean).strip()

    data = json.loads(clean)
    return data