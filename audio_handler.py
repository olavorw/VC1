"""
VC1 - VC1 - Voice Command 1
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

import pygame
from rich import print
import os

class AudioHandler:
    def play_audio(file_path, deleteaudio):
        print(f"[yellow]Playing audio file, please wait...[/yellow]")
        
        try:
            pygame.mixer.init() # Initialize the mixer
            pygame.mixer.music.load(file_path) # Load the sound file
            
            pygame.mixer.music.play() # Play the sound file
            # Keep the script running until the audio is finished playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            # Stop playback and unload the mixer
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            print(f"[red]Error playing audio file. This is probably because the file is corrupt.[/red]")
        
        # Delete the audio file
        if deleteaudio == True:
            try:
                print(f"[green]Audio file dseleted, continuing recognition.[/green]")
                os.remove(file_path)
            except PermissionError:
                print(f"[red]Error deleting audio file. Please delete the file manually.[/red]")

    def test_voice_id(file_path):
        print(f"[yellow]Playing test file, please wait...[/yellow]") # Notify the user to wait for the audio to play
        
        try:
            pygame.mixer.init() # Initialize the mixer
            pygame.mixer.music.load(file_path) # Load the sound file

            
            pygame.mixer.music.play() # Play the sound file
            while pygame.mixer.music.get_busy(): # Keep the script running until the audio is finished playing
                pygame.time.Clock().tick(10)
                
            # Stop playback and unload the mixer
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            print(f"[red]Error playing audio file. This voice doesn't seem right.[/red]")
            return "error" # Return error to signify the voice id doesn't work, or the file is corrupt. 
        
        # Delete the audio file
        try:
            print(f"[green]Audio file deleted, continuing recognition.[/green]")
            os.remove(file_path)
        except PermissionError:
            print(f"[red]Error deleting audio file. Please delete the file manually.[/red]")

# Tests
if __name__ == "__main__":
    AudioHandler.play_audio("./assets/audio/test.mp3", False)