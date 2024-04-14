from eleven_labs import ElevenLabsSpeech
from audio_player_main import audio_player
from speech_recognizer import SpeechRecognition
from config import Config

config = Config()
config.prompt_eula()
elevenlabs = ElevenLabsSpeech()
api_key = config.call_api_key()
audiomanager = audio_player()
speech = SpeechRecognition()
voice_id = input("Enter your ElevenLabs voice ID: ")
while True:
    # Get the recognized speech from the microphone using SpeechRecognition
    result = speech.listen_and_recognize()
    
    # Get the audio for the specified voice ID using ElevenLabsSpeech
    file = elevenlabs.get_audio(result, voice_id, api_key)
    
    # Play the generated audio using AudioManager
    audiomanager.play_audio(file)