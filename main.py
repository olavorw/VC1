from elevenlabs_handler import ElevenLabsHandler
from audio_handler import AudioHandler
from speech_to_text_handler import SpeechToTextHandler
from configuration_handler import ConfigurationHandler
from web_handler import WebHandler
from rich import print

# Prompt the user to accept the EULA
ConfigurationHandler.prompt_eula()

# Check if VC1 is usable
if WebHandler.check_if_usable() == False:
    # If VC1 is not usable, print a message and exit the program
    print(f"[red]VC1 is currently unusable.[/red]")
    # Exit the program
    exit()
    # If VC1 is usable, print a message and continue
elif WebHandler.check_if_usable() == True:
    # Pass through check
    pass
# If an error occurred while checking if VC1 is usable, print a message and exit the program
else:
    # Print an error message
    print(f"[red]An error occurred while checking if VC1 is usable. Please check your internet connection. Closing program...[/red]")
    # Exit the program
    exit()

# Define current version
current_version = '0.5'

# Check for updates
WebHandler.check_for_updates(current_version)

# Get or prompt for the API key
api_key = ConfigurationHandler.get_api_key()

# Initialize the ElevenLabsSpeech object
ElevenLabsHandler(api_key)

# Initialize the audio player
AudioHandler()

# Initialize the SpeechRecognition object
SpeechToTextHandler()

# Ask the user for their ElevenLabs voice ID
print(f"[yellow]Please enter your ElevenLabs voice ID...[/yellow]")
# Get the voice ID from the user using the ConfigurationHandler class
voice_id = ConfigurationHandler.prompt_voice_id()
# Let the user know that the voice ID has been selected
print(f"[green]Selected Voice ID: {voice_id}.[/green]")


# Initialize the main loop
while True:
    
    # Get the recognized speech from the microphone using SpeechRecognition
    result = SpeechToTextHandler.listen_and_recognize()
    
    # Check if the result wants to access configuration files
    #if result.lower() == "configure":
    #    # Get the configuration file
    #    ConfigurationHandler.get_config()
    #    # Continue the loop
    #    continue
    
    # Get the audio for the specified voice ID using ElevenLabsSpeech
    audio_file = ElevenLabsHandler.generate(result, voice_id)
    
    # Play the generated audio using AudioHandler
    AudioHandler.play_audio(audio_file)