from elevenlabs import save
from elevenlabs.client import ElevenLabs
from rich import print
import time

class ElevenLabsHandler:
    def __init__(self, api_key):
        self.client = ElevenLabs(
            api_key=api_key  # Defaults to ELEVEN_API_KEY
        )

    def generate(self, text, voice_id):
        print("[yellow]Making a request to the ElevenLabs API, please wait...[/yellow]")
        audio = self.client.generate(
            text=text,
            voice=voice_id,
            model="eleven_turbo_v2"
        )
        timestamp = str(int(time.time()))
        file_name = timestamp + '.mp3'
        save(audio, file_name)
        return file_name
    
# Tests
if __name__ == "__main__":
    handler = ElevenLabsHandler("")
    handler.generate("Hello! The quick brown fox jumped over the fence", "")
