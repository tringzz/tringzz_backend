# stt/mic_recorder.py

import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(duration=5, sample_rate=44100, output_file="input/user_input.wav"):
    print(f"🎙️ Recording for {duration} seconds...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    write(output_file, sample_rate, recording)
    print(f"✅ Audio saved to {output_file}")
    return output_file
