import pygame
from rich import print
import os

class AudioHandler:
    def play_audio(file_path):
        
        # Notify the user to wait for the audio to play
        print(f"[yellow]Playing audio file, please wait...[/yellow]")
        
        try:
            # Initialize the mixer
            pygame.mixer.init()
            
            # Load the sound file
            pygame.mixer.music.load(file_path)

            # Play the sound file
            pygame.mixer.music.play()

            # Keep the script running until the audio is finished playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            # Stop playback and unload the mixer
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            # Handle error if the audio file is corrupt
            print(f"[red]Error playing audio file. This is probably because the file is corrupt.[/red]")
        
        # Delete the audio file
        try:
            print(f"[green]Audio file deleted, continuing recognition.[/green]")
            os.remove(file_path)
        except PermissionError:
            # Handle error if unable to delete the audio file
            print(f"[red]Error deleting audio file. Please delete the file manually.[/red]")

    def test_voice_id(file_path):
        
        # Notify the user to wait for the audio to play
        print(f"[yellow]Playing test file, please wait...[/yellow]")
        
        try:
            # Initialize the mixer
            pygame.mixer.init()
            
            # Load the sound file
            pygame.mixer.music.load(file_path)

            # Play the sound file
            pygame.mixer.music.play()

            # Keep the script running until the audio is finished playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            # Stop playback and unload the mixer
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            # Handle error if the audio file cannot be played
            print(f"[red]Error playing audio file. This voice doesn't seem right.[/red]")
            
            return "error"
        
        # Delete the audio file
        try:
            print(f"[green]Audio file deleted, continuing recognition.[/green]")
            os.remove(file_path)
        except PermissionError:
            # Handle error if unable to delete the audio file
            print(f"[red]Error deleting audio file. Please delete the file manually.[/red]")

# Tests
if __name__ == "__main__":
    AudioHandler.play_audio("test.mp3")