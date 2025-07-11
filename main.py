# main.py

from tts.elevenlabs_tts import synthesize_speech

if __name__ == "__main__":
    text = "Hi, this is Tringzz AI agent. I'm here to help you find your dream home!"
    audio_file = synthesize_speech(text)
    print(f"Speech synthesized and saved to: {audio_file}")
