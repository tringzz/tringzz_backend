# main.py

from tts.elevenlabs_tts import synthesize_speech
from stt.whisper_stt import transcribe_audio

text = "Hello! Welcome to Tringgz, your smart property assistant."
audio_file = synthesize_speech(text)
print(f"Speech synthesized and saved to: {audio_file}")

# Simulate user replying (we use the same file here for testing)
transcribed_text = transcribe_audio(audio_file)
print("Transcribed User Reply:", transcribed_text)
