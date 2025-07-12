# main.py

from tts.elevenlabs_tts import synthesize_speech
from stt.whisper_stt import transcribe_audio
from memory.memory_store import MemoryStore

memory = MemoryStore()
session_id = "test_user_1"  # Static for now

# 1. Synthesize speech
text = "Hi! How can I help you today?"
audio_file = synthesize_speech(text)
print(f"Speech synthesized and saved to: {audio_file}")

# 2. Transcribe audio back to text
transcribed_text = transcribe_audio(audio_file)
print(f"Transcribed text: {transcribed_text}")

# 3. Save to memory
memory.save_message(session_id, role="assistant", message=text)
memory.save_message(session_id, role="user", message=transcribed_text)

# 4. Retrieve history
conversation = memory.get_conversation(session_id)
print(f"\nConversation so far:\n{conversation}")
