from eleven_labs import ElevenLabsSpeech
from audio_player import AudioManager
from speech_recognizer import SpeechRecognition
from locks import Lock
from rich import print
#pyaudio is necassary for the speech_recognizer.py file as a hidden import
while True:
    agreement = input("[yellow]Please read README.md, and LICENSE.md before proceeding. By proceeding, you agree to the terms and conditions in LICENSE.md, README.md, and EULA.txt. These conditions are located under the _internal folder. Proceed and Agree? yes/no:")
    if agreement == "yes":
        print("[yellow]Proceeding...")
        break
    if agreement == "no":
        print("[yellow]Exiting...")
        exit()
keys = Lock()
api_key = keys.get_api_key()

# Initialize the speech recognition, ElevenLabsSpeech, and AudioManager objects
elevenlabs = ElevenLabsSpeech()
audiomanager = AudioManager()
speech = SpeechRecognition()

# Get the voice ID from the user
voice_id = input("Enter the voice ID: ")

#Start the loop
while True:
    # Get the recognized speech from the microphone using SpeechRecognition
    result = speech.listen_and_recognize()
    # Get the audio for the specified voice ID using ElevenLabsSpeech
    file = elevenlabs.get_audio(result, voice_id, api_key)
    # Play the generated audio using AudioManager
    audiomanager.play_audio(file, True, True, True)