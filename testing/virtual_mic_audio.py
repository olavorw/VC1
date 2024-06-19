import pygame
from rich import print
import os

class AudioHandler:
    @staticmethod
    def play_audio(file_path):
        
        # Notify the user to wait for the audio to play
        print("[yellow]Playing audio file, please wait...[/yellow]")
        
        
        try:
            # Load the sound file
            pygame.mixer.init()
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
            print("[red]Error playing audio file. This is probably because the file is corrupt.[/red]")
        
        # Delete the audio file
        #try:
        #    print("[green]Audio file deleted, continuing recognition.[/green]")
        #    os.remove(file_path)
        #except PermissionError:
        #    print("[red]Error deleting audio file. Please delete the file manually.[/red]")

    @staticmethod
    def test_voice_id(file_path):
        
        # Notify the user to wait for the audio to play
        print("[yellow]Playing test file, please wait...[/yellow]")
        
        try:
            # Load the sound file
            pygame.mixer.init()
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
            print("[red]Error playing audio file. This voice doesn't seem right.[/red]")
            
            return "error"
            
            
        
        # Delete the audio file
        try:
            print("[green]Audio file deleted, continuing recognition.[/green]")
            os.remove(file_path)
        except PermissionError:
            print("[red]Error deleting audio file. Please delete the file manually.[/red]")

# Tests
if __name__ == "__main__":
    AudioHandler.play_audio("test.mp3")