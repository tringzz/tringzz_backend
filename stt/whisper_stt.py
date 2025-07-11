# stt/whisper_stt.py

import whisper

model = whisper.load_model("base")  # You can try "tiny" or "small" if needed

def transcribe_audio(audio_path):
    """
    Transcribes the given audio file to text.
    """
    result = model.transcribe(audio_path)
    return result["text"]
