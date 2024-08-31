"""
VC1 - Voice Command 1
Copyright (C) 2024  Olav Sharma

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

import speech_recognition as sr
import time
from rich import print

# Define the SpeechToTextHandler class
class SpeechToTextHandler:
    """
    A class to handle speech recognition using the Google Web Speech API.
    
    Attributes:
    None
    
    Methods:
    listen_and_recognize(): Listen to the user's speech and recognize it using Google Web Speech API.
    """
    @staticmethod
    def listen_and_recognize():
        """
        Listen to the user's speech and recognize it using Google Web Speech API.
        
        Args:
        None
        
        Example:
        SpeechToTextHandler.listen_and_recognize()
        
        Returns:
        str: The recognized text from the user's speech.
        """
        # Initialize recognizer class (for recognizing the speech)
        try:
            r = sr.Recognizer()
        except Exception as e:
            print(f"[red]An error occurred while trying to initialize the recognizer class. Error: {e}[/red]")
            return SpeechToTextHandler.listen_and_recognize()

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
                except sr.UnknownValueError:
                    # Indicate that the recognizer could not understand the audio
                    print(f"[yellow]Google Speech Recognition could not understand audio, please try again...")
                    time.sleep(0.1)
                    return SpeechToTextHandler.listen_and_recognize()
                except sr.RequestError as e:
                    # Indicate that the recognizer could not request results from Google Speech Recognition service
                    print(f"Could not request results from Google Speech Recognition service; {e}")
                    time.sleep(0.1)
                    return SpeechToTextHandler.listen_and_recognize()
                if text:
                        # Indicate that the text was recognized
                        print(f"[blue]Received: " + text)
                        # Return text immediately after recognition
                        return text
                # Handle exceptions

# Tests
if __name__ == '__main__':
    # Initialize the SpeechToTextHandler object
    speech = SpeechToTextHandler()
    
    # Listen to the user's speech and recognize it
    result = speech.listen_and_recognize()
    
    # Print the final recognized text
    print(f"Final recognized text: {result}")
