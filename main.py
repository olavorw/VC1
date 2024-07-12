from elevenlabs_handler import ElevenLabsHandler
from audio_handler import AudioHandler
from speech_to_text_handler import SpeechToTextHandler
from configuration_handler import ConfigurationHandler
from web_handler import WebHandler
from rich import print


ConfigurationHandler.prompt_agreements() # Prompt the user to accept the EULA

if WebHandler.check_if_usable() == False:
    
    print(f"[red]VC1 is currently unusable.[/red]")
    exit()
  
elif WebHandler.check_if_usable() == True: # If VC1 is usable, continue  
    pass
else: # If an error occurred while checking if VC1 is usable, print a message and exit the program
    print(f"[red]An error occurred while checking if VC1 is usable. Please check your internet connection. Closing program...[/red]")
    exit()

# Check for updates
current_version = '0.5'
WebHandler.check_for_updates(current_version)

# Get or prompt for the API key
api_key = ConfigurationHandler.get_api_key() 
ElevenLabsHandler(api_key) # Initialize the ElevenLabsSpeech object

# Initialize the handlers
AudioHandler()
SpeechToTextHandler()

# Get the voice ID
print(f"[yellow]Please enter your ElevenLabs voice ID...[/yellow]")
voice_id = ConfigurationHandler.prompt_voice_id()
print(f"[green]Selected Voice ID: {voice_id}.[/green]") # Let the user know that the voice ID has been selected

# Initialize the main loop
while True:
    result = SpeechToTextHandler.listen_and_recognize() # Get the recognized speech from the microphone using SpeechRecognition
    
    audio_file = ElevenLabsHandler.generate(result, voice_id) # Get the audio for the specified voice ID using ElevenLabsSpeech
    
    AudioHandler.play_audio(audio_file) # Play the generated audio using AudioHandler