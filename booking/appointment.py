import json

def parse_booking_response(llm_reply):
    try:
        booking_data = json.loads(llm_reply)
        if booking_data.get("intent") == "book":
            slot = booking_data.get("slot")
            visit_type = booking_data.get("type")
            return {
                "slot": slot,
                "type": visit_type
            }
    except json.JSONDecodeError:
        pass
    return None
