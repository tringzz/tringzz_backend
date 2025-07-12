# ai/response_engine.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

def generate_response(conversation):
    messages = [{"role": msg["role"], "content": msg["message"]} for msg in conversation]

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages
    )

    return response.choices[0].message.content
