import pygame
from rich import print

class audio_player:
    @staticmethod
    def play_audio(file_path):
        
        #Notify the user to wait for the audio to play
        print("[yellow]Playing audio file, please wait...[/yellow]")
        
        #Load the sound file
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        
        #Play the sound file
        pygame.mixer.music.play()
        
        #Keep the script running until the audio is finished playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
            
        print("[green]Playback finished, Continuing voice recognition[/green]")
        
#Tests
if __name__ == "__main__":
    audio_player.play_audio("test.mp3")