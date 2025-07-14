# booking/appointment_scheduler.py

def schedule_appointment(booking_info):
    """
    Placeholder logic to simulate appointment scheduling.
    In future, this will connect to a calendar or CRM system.
    """
    if not booking_info:
        return {"status": "failed", "reason": "Missing booking info"}

    # Extract and log booking details
    slot = booking_info.get("slot")
    appointment_type = booking_info.get("type")

    # Simulated booking confirmation
    print(f"📆 Scheduled a {appointment_type} on {slot}")
    return {
        "status": "success",
        "message": f"{appointment_type.replace('_', ' ').title()} booked for {slot}"
    }
