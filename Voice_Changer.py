from elevenlabs_handler import ElevenLabsHandler
from audio_handler import AudioHandler
from speech_to_text_handler import SpeechToTextHandler
from configuration_handler import ConfigurationHandler

# Import necessary modules

# Initialize the Config object
config = ConfigurationHandler()

# Prompt the user to accept the EULA
config.prompt_eula()

# Initialize the ElevenLabsSpeech object
elevenlabs = ElevenLabsHandler()

# Get the API key from the config
api_key = config.call_api_key()

# Initialize the audio player
audiomanager = AudioHandler()

# Initialize the SpeechRecognition object
speech = SpeechToTextHandler()

# Ask the user for their ElevenLabs voice ID
voice_id = input("Enter your ElevenLabs voice ID: ")

# Main loop
while True:
    # Get the recognized speech from the microphone using SpeechRecognition
    result = speech.listen_and_recognize()
    
    # Get the audio for the specified voice ID using ElevenLabsSpeech
    audio_file = elevenlabs.get_audio(result, voice_id, api_key)
    
    # Play the generated audio using AudioManager
    audiomanager.play_audio(audio_file)