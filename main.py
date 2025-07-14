from tts.elevenlabs_tts import synthesize_speech
from stt.whisper_stt import transcribe_audio
from stt.mic_recorder import record_audio
from memory.memory_store import MemoryStore
from ai.response_engine import generate_response
from appointment.booking_engine import book_appointment
from booking.appointment_scheduler import schedule_appointment
from router.lead_rerouter import check_objection_or_reroute
import os
from dotenv import load_dotenv
from ai.response_engine import generate_greeting

load_dotenv()
FIRM_NAME = os.getenv("FIRM_NAME", "our company")

memory = MemoryStore()
session_id = "test_user_1"

# 1. Assistant speaks
text = generate_greeting(FIRM_NAME)
synthesize_speech(text)
print(f"🗣️ Assistant said: {text}")

# 2. Record user response via mic
user_audio_file = record_audio(duration=5)
transcribed_text = transcribe_audio(user_audio_file)
print(f"📝 User said: {transcribed_text}")

# 3. Save both turns to memory
memory.save_message(session_id, "assistant", text)
memory.save_message(session_id, "user", transcribed_text)

# 4. Get LLM response
conversation = memory.get_conversation(session_id)
ai_reply = generate_response(conversation)
print(f"\n🤖 AI Reply: {ai_reply}")

# Check if AI reply indicates objection/rerouting
routing_decision = check_objection_or_reroute(ai_reply)

if routing_decision["action"] == "reroute":
    print(f"🚨 Lead flagged for rerouting: {routing_decision['reason']}")
    # Optionally, notify human via email, CRM, or log
    synthesize_speech("Thank you. One of our team members will get in touch shortly.")
    exit()  # Exit early — don't proceed with booking


# 5. Speak the AI reply
short_reply = ai_reply[:250]  # Truncate to 250 characters
synthesize_speech(short_reply)
print("🔊 AI reply spoken (shortened).")

# 6. Store assistant response
memory.save_message(session_id, "assistant", ai_reply)

# 7. Appointment intent check (LLM-driven)
formatted_conversation = [
    {"role": msg["role"], "content": msg["message"]} for msg in conversation
]
formatted_conversation.append({"role": "assistant", "content": ai_reply})
booking_info = book_appointment(formatted_conversation)


if isinstance(booking_info, dict) and booking_info.get("intent") == "book":
    print(f"\n📅 Booking Info Detected:\n{booking_info}")
    # 8. Schedule the appointment
    scheduling_result = schedule_appointment(booking_info)
    print(f"✅ Scheduling Result: {scheduling_result}")
else:
    print("ℹ️ No booking intent detected.")
