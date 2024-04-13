from eleven_labs import ElevenLabsSpeech
from audio_player_main import audio_player
from speech_recognizer import SpeechRecognition
from config import Config
from rich import print

#Initialize the Config object
config = Config()

while True:
    agreement = input("To continue, please read the EULA.txt and agree to proceed. Do you agree to the EULA? Yes/No:")
    if agreement == "Yes":
        print("[green]Proceeding...")
        break
    if agreement == "No":
        print("[red]Exiting...")
        exit()
while True:
    dontAskAgain = input("Don't ask again? Remember, by using this software you agree to the EULA. Yes/No:")
    if dontAskAgain == "Yes":
        print("[green]You will not be asked again. To reset this setting, change it in the config.json file.")
        config.dont_ask_again(True)
        break
    if dontAskAgain == "No":
        print("[green]Understood.")
        break
    else:
        print("[red]Invalid input. Please enter 'Yes' or 'No'.")
#Get the API key from the user
api_key = config.get_api_key()

# Initialize the speech recognition, ElevenLabsSpeech, and AudioManager objects
elevenlabs = ElevenLabsSpeech()
audiomanager = audio_player()
speech = SpeechRecognition()

# Get the voice ID from the user
voice_id = input("Enter your ElevenLabs voice ID: ")

#Start the loop
while True:
    # Get the recognized speech from the microphone using SpeechRecognition
    result = speech.listen_and_recognize()
    
    # Get the audio for the specified voice ID using ElevenLabsSpeech
    file = elevenlabs.get_audio(result, voice_id, api_key)
    
    # Play the generated audio using AudioManager
    audiomanager.play_audio(file, True, True, True)