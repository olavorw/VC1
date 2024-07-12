"""
VC1 - Voice Command 1
Copyright (C) 2024  Olanorw aka Olav SHarma

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from elevenlabs_handler import ElevenLabsHandler
from audio_handler import AudioHandler
from speech_to_text_handler import SpeechToTextHandler
from configuration_handler import ConfigurationHandler
from web_handler import WebHandler
from rich import print

print("[bold yellow]VC1  Copyright (C) 2024  Olanorw and Olav Sharma This program comes with ABSOLUTELY NO WARRANTY; for details say `show w'. This is free software, and you are welcome to redistribute itunder certain conditions; say `show c' for details.")

async def show_w():
    with open('CODE_OF_CONDUCT.md', 'r') as file:
        code_of_conduct = file.read()
        print(f"[bold white]\n" + code_of_conduct)

async def show_c():
    with open('LICENSE.md', 'r') as file:
        license = file.read()
        print(f"[white]\n" + license)
    print(f"\n[bold white]Please wait...[/yellow]\n")

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
    
    if result == "show w":
        show_w()
    elif result == "show c":
        show_c()

    audio_file = ElevenLabsHandler.generate(result, voice_id) # Get the audio for the specified voice ID using ElevenLabsSpeech
    
    AudioHandler.play_audio(audio_file) # Play the generated audio using AudioHandler