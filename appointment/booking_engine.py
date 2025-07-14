from ai.response_engine import generate_response
import json

def book_appointment(conversation_history):
    """
    Generate an appointment slot suggestion from the conversation context using LLM.
    """
    prompt = """
You are a highly polite, accurate, and human-like real estate appointment assistant.

Your task is to extract the user's booking intent and proposed time for a site visit or call, based on the conversation.

Always respond strictly with a single JSON object, like:
{"intent": "book", "slot": "DD-MM-YYYY HH:MM AM/PM", "type": "site_visit"}

If the user did not provide enough info, respond with:
{"intent": "none"}

⚠️ Do not include explanations, greetings, follow-up questions, or formatting characters like *, -, or newlines. Just output plain JSON.
"""

    formatted_conversation = [{"role": msg["role"], "content": msg["content"]} for msg in conversation_history]

    messages = [{"role": "system", "content": prompt}] + formatted_conversation
    response = generate_response(messages).strip()

    # Force JSON only
    if "{" not in response:
        return {"intent": "none"}

    try:
        booking_info = json.loads(response)
        return booking_info
    except Exception as e:
        print(f"❌ JSON parsing failed: {e}")
        return {"intent": "none"}
