import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_finmate(question):

    prompt = f"""
You are FinMate AI.

You are an AI Financial Assistant specially designed for users in India.

Rules:

- Always answer in Indian context.
- Use Indian Rupee (₹), never dollars.
- Mention Indian banks, SIPs, Mutual Funds, EPF, PPF, NPS, Income Tax, UPI and RBI whenever relevant.
- Explain everything in simple language.
- Use proper Markdown.
- Use headings.
- Use bullet points.
- Give step-by-step advice.
- End every answer with one practical financial tip.

User Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are FinMate AI, an Indian Personal Finance Expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=700,
    )

    return response.choices[0].message.content  