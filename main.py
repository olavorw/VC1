from elevenlabs_handler import ElevenLabsHandler
from audio_handler import AudioHandler
from speech_to_text_handler import SpeechToTextHandler
from configuration_handler import ConfigurationHandler
from web_handler import WebHandler
from rich import print

# Prompt the user to accept the EULA
ConfigurationHandler.prompt_eula()

if WebHandler.check_if_usable() == False:
    print("[red]VC1 is currently unusable.[/red]")
    exit()
elif WebHandler.check_if_usable() == True:
    pass
else:
    print("[red]An error occurred while checking if VC1 is usable. Please check your internet connection. Closing program...[/red]")
    exit()

# Define current version
current_version = '0.5'

# Check for updates
WebHandler.check_for_updates(current_version)

# Get or prompt for the API key
api_key = ConfigurationHandler.get_api_key()
if not api_key:
    api_key = ConfigurationHandler.prompt_api_key()
    
# Initialize the ElevenLabsSpeech object
elevenlabs = ElevenLabsHandler(api_key)

# Initialize the audio player
audio = AudioHandler()

# Initialize the SpeechRecognition object
speech = SpeechToTextHandler()

# Ask the user for their ElevenLabs voice ID
print("[yellow]Please enter your ElevenLabs voice ID:[/yellow]")
voice_id = ConfigurationHandler.prompt_voice_id()
print(f"[green]Selected Voice ID: {voice_id}.[/green]")

while True:
    
    # Get the recognized speech from the microphone using SpeechRecognition
    result = speech.listen_and_recognize()
    
    # Get the audio for the specified voice ID using ElevenLabsSpeech
    audio_file = elevenlabs.generate(result, voice_id)
    
    # Play the generated audio using AudioHandler
    audio.play_audio(audio_file)