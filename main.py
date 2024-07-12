from elevenlabs_handler import ElevenLabsHandler
from audio_handler import AudioHandler
from speech_to_text_handler import SpeechToTextHandler
from configuration_handler import ConfigurationHandler
from web_handler import WebHandler
from rich import print


ConfigurationHandler.prompt_eula() # Prompt the user to accept the EULA

# Check if VC1 is usable
if WebHandler.check_if_usable() == False:
    
    print(f"[red]VC1 is currently unusable.[/red]") # If VC1 is not usable, print a message and exit the program
    exit() # Exit the program
# If VC1 is usable, print a message and continue    
elif WebHandler.check_if_usable() == True:
    pass # Pass through check
# If an error occurred while checking if VC1 is usable, print a message and exit the program
else:
    print(f"[red]An error occurred while checking if VC1 is usable. Please check your internet connection. Closing program...[/red]") # Print an error message
    
    exit() # Exit the program

current_version = '0.5' # Define current version
WebHandler.check_for_updates(current_version) # Check for updates

api_key = ConfigurationHandler.get_api_key() # Get or prompt for the API key
ElevenLabsHandler(api_key) # Initialize the ElevenLabsSpeech object

AudioHandler() # Initialize the audio player
SpeechToTextHandler() # Initialize the SpeechRecognition object

print(f"[yellow]Please enter your ElevenLabs voice ID...[/yellow]") # Ask the user for their ElevenLabs voice ID
voice_id = ConfigurationHandler.prompt_voice_id() # Get the voice ID from the user using the ConfigurationHandler class
print(f"[green]Selected Voice ID: {voice_id}.[/green]") # Let the user know that the voice ID has been selected

# Initialize the main loop
while True:
    result = SpeechToTextHandler.listen_and_recognize() # Get the recognized speech from the microphone using SpeechRecognition
    
    # Check if the result wants to access configuration files
    #if result.lower() == "configure":
    #    # Get the configuration file
    #    ConfigurationHandler.get_config()
    #    # Continue the loop
    #    continue
    
    audio_file = ElevenLabsHandler.generate(result, voice_id) # Get the audio for the specified voice ID using ElevenLabsSpeech
    
    AudioHandler.play_audio(audio_file) # Play the generated audio using AudioHandler