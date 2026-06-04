import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("DEEPINFRA_API_KEY")

def ask_llm(context, question):

    prompt = f"""
You are a Senior Upwork API Consultant.

Use ONLY the documentation provided below.

If the answer is not found, respond exactly:

I'm sorry, but the provided documentation does not contain that information.

Context:
{context}

Question:
{question}
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2
    }

    response = requests.post(
        "https://api.deepinfra.com/v1/openai/chat/completions",
        headers=headers,
        json=payload
    )

    return response.json()["choices"][0]["message"]["content"]