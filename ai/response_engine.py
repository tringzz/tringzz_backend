import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(conversation):
    """
    Sends conversation history to Groq API and returns the LLM's reply as a string.
    Supports both {"role", "message"} and {"role", "content"} formatted inputs.
    """
    formatted_conversation = [
        {
            "role": msg["role"],
            "content": msg.get("message", msg.get("content", ""))
        }
        for msg in conversation
    ]

    # Prepend strict real estate assistant behavior system prompt
    system_prompt = {
        "role": "system",
        "content": (
            "You are a professional, polite, human-like real estate assistant working for ABC Constructions. "
            "You never say you are an AI or list generic capabilities. "
            "Only help users with real estate-related matters like site visits, property inquiries, booking appointments, follow-ups, etc. "
            "Always respond in a warm, natural, and conversational tone like a human representative. "
            "Avoid bullet points, asterisks, or overly robotic formatting."
        )
    }

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[system_prompt] + formatted_conversation,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()


# 💬 Add this for personalized greetings
def get_greeting_prompt(firm_name):
    return f"""
You are a voice assistant working for {firm_name}, a real estate company.

Start your response by saying:
"Hello, this is {firm_name}."

Then politely ask how you may help the caller. Be warm and professional.
Keep it under 25 words. No emojis or bullet points.
Respond in natural spoken language.
"""

def generate_greeting(firm_name):
    prompt = get_greeting_prompt(firm_name)
    return generate_response([{"role": "system", "content": prompt}])
