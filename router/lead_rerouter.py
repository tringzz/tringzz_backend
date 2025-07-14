# router/lead_rerouter.py

def check_objection_or_reroute(ai_reply: str) -> dict:
    """
    Checks if the AI reply contains phrases indicating objection or lead disqualification.

    Returns:
        dict with keys:
        - action: "continue" or "reroute"
        - reason: explanation string (if reroute)
    """
    objection_keywords = [
        "not interested",
        "call me later",
        "already bought",
        "not looking",
        "do not call",
        "stop calling",
        "wrong number",
        "not now",
        "busy",
        "spam"
    ]

    lower_reply = ai_reply.lower()

    for keyword in objection_keywords:
        if keyword in lower_reply:
            return {
                "action": "reroute",
                "reason": f"Detected objection or disinterest: '{keyword}'"
            }

    return {"action": "continue", "reason": ""}
