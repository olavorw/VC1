from elevenlabs_handler import ElevenLabsSpeech
from audio_player_main import audio_player
from speech_to_text_handler import SpeechRecognition
from configuration_handler import Config

# Import necessary modules

# Initialize the Config object
config = Config()

# Prompt the user to accept the EULA
config.prompt_eula()

# Initialize the ElevenLabsSpeech object
elevenlabs = ElevenLabsSpeech()

# Get the API key from the config
api_key = config.call_api_key()

# Initialize the audio player
audiomanager = audio_player()

# Initialize the SpeechRecognition object
speech = SpeechRecognition()

# Ask the user for their ElevenLabs voice ID
voice_id = input("Enter your ElevenLabs voice ID: ")

# Main loop
while True:
    # Get the recognized speech from the microphone using SpeechRecognition
    result = speech.listen_and_recognize()
    
    # Get the audio for the specified voice ID using ElevenLabsSpeech
    file = elevenlabs.get_audio(result, voice_id, api_key)
    
    # Play the generated audio using AudioManager
    audiomanager.play_audio(file)