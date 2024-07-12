import speech_recognition as sr
from rich import print

# Define the SpeechToTextHandler class
class SpeechToTextHandler:
    
    # Define a static method to listen to the user's speech and recognize it
    @staticmethod
    def listen_and_recognize():
        
        # Initialize recognizer class (for recognizing the speech)
        r = sr.Recognizer()

        # Start a loop that will run until the user's speech is recognized
        while True:  
            # Use the microphone as source for input. Here we are using sr.Microphone() as source
            with sr.Microphone() as source:
                # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
                print(f"[cyan]Adjusting...")
                # Adjust the recognizer sensitivity to ambient noise and record audio from the microphone
                r.adjust_for_ambient_noise(source, duration=0.5)
                # Indicate that the program is listening
                print(f"[cyan]Listening...")
                # Listen to the user's input
                audio = r.listen(source)
                # Initialize text variable to handle scope issues
                text = None
                try:
                    # Using Google Web Speech API to recognize audio
                    text = r.recognize_google(audio)
                    # If some text was recognized, break the loop
                    if text:
                        # Indicate that the text was recognized
                        print(f"[blue]Received: " + text)
                        # Return text immediately after recognition
                        return text
                # Handle exceptions
                except sr.UnknownValueError:
                    # Indicate that the recognizer could not understand the audio
                    print(f"[yellow]Google Speech Recognition could not understand audio, please try again...")
                    SpeechToTextHandler.listen_and_recognize()
                except sr.RequestError as e:
                    # Indicate that the recognizer could not request results from Google Speech Recognition service
                    print(f"Could not request results from Google Speech Recognition service; {e}")

# Tests
if __name__ == '__main__':
    # Initialize the SpeechToTextHandler object
    speech = SpeechToTextHandler()
    
    # Listen to the user's speech and recognize it
    result = speech.listen_and_recognize()
    
    # Print the final recognized text
    print(f"Final recognized text: {result}")
