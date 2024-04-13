# Import the Azure Cognitive Services Speech SDK
import azure.cognitiveservices.speech as speechsdk

class SpeechRecognition:
    def __init__(self):
        # Initialize the speech configuration
        self.speech_config = speechsdk.SpeechConfig(subscription="ecc78c248bd64770877b86f6ef648a7e", region="westus2")
    
    # Define a method to recognize speech from microphone input
    def recognizespeech(self):
        # Create a speech recognizer using the speech configuration
        speech_recognizer = speechsdk.SpeechRecognizer(self.speech_config)
        
        # Prompt the user to speak into their microphone
        print("Speak into your microphone.")
        # Recognize the speech input from the microphone
        result = speech_recognizer.recognize_once_async().get()
        # Print the recognized text
        if result.text == '':
            SpeechRecognition.recognizespeech(SpeechRecognition())
        print("Result: " + result.text)
        # Return the recognized text
        return result.text

# Example of using the class

# If this script is run directly, start recognizing speech from the microphone
if __name__ == "__main__":
    SpeechRecognition.recognizespeech(SpeechRecognition())