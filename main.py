from tts.elevenlabs_tts import synthesize_speech
from stt.whisper_stt import transcribe_audio
from stt.mic_recorder import record_audio
from memory.memory_store import MemoryStore
from ai.response_engine import generate_response

memory = MemoryStore()
session_id = "test_user_1"

# 1. Assistant speaks
text = "Hi! How can I help you today?"
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

# 5. Speak the AI reply
#synthesize_speech(ai_reply)
short_reply = ai_reply[:250]  # Truncate to 250 characters
synthesize_speech(short_reply)
print("🔊 AI reply spoken (shortened).")


# 6. Store in memory
memory.save_message(session_id, "assistant", ai_reply)
