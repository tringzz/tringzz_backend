import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
from pathlib import Path

load_dotenv()

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
if not ELEVEN_API_KEY:
    raise ValueError("Please set ELEVEN_API_KEY in your .env file or environment.")

client = ElevenLabs(api_key=ELEVEN_API_KEY)

def synthesize_speech(text, voice_id="21m00Tcm4TlvDq8ikWAM", output_path="output/tts_output.mp3"):
    """
    Generate speech using ElevenLabs API and save to a file.
    voice_id: Rachel = "21m00Tcm4TlvDq8ikWAM"
    """
    audio_stream = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=text,
        output_format="mp3_44100"  # instead of "pcm_44100"
    )

    Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)
    
    return output_path
