import speech_recognition as sr

class SpeechRecognition:
    @staticmethod
    def listen_and_recognize():
        # Initialize recognizer class (for recognizing the speech)
        r = sr.Recognizer()

        # Start a loop that will run until the user's speech is recognized
        while True:  
            # Use the microphone as source for input. Here we are using sr.Microphone() as source
            with sr.Microphone() as source:
                print("Listening...")
                # Adjust the recognizer sensitivity to ambient noise and record audio from the microphone
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                text = None  # Initialize text variable to handle scope issues.
                try:
                    # Using Google Web Speech API to recognize audio
                    text = r.recognize_google(audio)
                    # If some text was recognized, break the loop
                    if text:  
                        print("RECOGNIZED: " + text)
                        return text  # Return text immediately after recognition
                # Handle exceptions
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio, please try again...")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")

# TESTS
if __name__ == '__main__':
    speech = SpeechRecognition()
    result = speech.listen_and_recognize()
    print(f"Final recognized text: {result}")
