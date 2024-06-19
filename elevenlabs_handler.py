from elevenlabs import Voice, VoiceSettings, save
from elevenlabs.client import ElevenLabs
from rich import print
import time

class ElevenLabsHandler:
    def __init__(self, api_key):
        self.client = ElevenLabs(
            api_key=api_key  # Defaults to ELEVEN_API_KEY
        )

    def generate(self, text, voice_id):
        print("[yellow]Making a POST request to the ElevenLabs API, please wait...[/yellow]")
        audio = self.client.generate(
            text=text,
            voice=Voice(
                voice_id=voice_id,
                settings=VoiceSettings(
                    stability=0.71,
                    similarity_boost=0.5,
                    style=0.0,
                    use_speaker_boost=True
                )
            )
        )
        timestamp = str(int(time.time()))
        file_name = timestamp + '.mp3'
        save(audio, file_name)
        return file_name
    
# Tests
if __name__ == "__main__":
    handler = ElevenLabsHandler("")
    handler.generate("Hello!", "")
