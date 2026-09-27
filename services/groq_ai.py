import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

index = faiss.read_index("rag/faiss_index.bin")

with open("rag/texts.pkl", "rb") as file:
    texts = pickle.load(file)

model = SentenceTransformer("all-MiniLM-L6-v2")


def ask_ai(prompt):

    query_embedding = model.encode([prompt])

    distances, results = index.search(query_embedding, k=2)

    context = ""

    for result in results[0]:
        context += texts[result] + "\n\n"

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": """You are FinMate AI, a helpful personal financial assistant.

Give clear, practical and easy-to-understand financial guidance.

IMPORTANT CURRENCY RULE:
- FinMate AI is designed for users in India.
- Always express monetary amounts in Indian Rupees (₹).
- Never use $, USD, dollars, or other foreign currency unless the user explicitly asks for another currency.
- If the user gives an amount in another currency, convert it to INR before presenting the financial advice.
- Use ₹ for all example amounts and calculations.

Use the following financial knowledge when it is relevant:

""" + context
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_completion_tokens=1024
    )

    return completion.choices[0].message.content

def explain_spending_risk(transaction_data):

    prompt = f"""
Analyze the following unusual spending transactions from a personal finance application.

Transactions:
{transaction_data}

Explain:
1. What spending pattern looks unusual
2. Possible reason for the unusual spending
3. How it may affect the user's budget
4. One practical recommendation

Keep the explanation simple and concise.
Always use Indian Rupees (₹).
Do not claim that the transaction is fraud. It is only an unusual spending pattern.
"""

    return ask_ai(prompt)