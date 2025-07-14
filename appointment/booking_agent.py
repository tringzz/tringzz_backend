# appointment/booking_agent.py

from ai.response_engine import generate_response

def extract_appointment_details(conversation: list) -> dict:
    prompt = """
You are an appointment assistant for a real estate agent.

Given the following conversation, extract structured booking details as JSON.
Only respond with JSON like:
{
  "intent": "book_appointment",
  "datetime": "2025-07-15T14:00:00",
  "project": "Wagholi",
  "status": "ready_to_book"
}

If info is missing, include:
{
  "intent": "book_appointment",
  "status": "incomplete",
  "missing": ["datetime", "project"]
}

Conversation:
{}
""".format(conversation)

    raw_reply = generate_response([{"role": "user", "message": prompt}])
    try:
        parsed = eval(raw_reply.strip())  # Use with caution; better to use `json.loads` if valid JSON
        return parsed
    except Exception as e:
        print("⚠️ Error parsing appointment data:", e)
        return {}
