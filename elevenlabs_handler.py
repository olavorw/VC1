"""
VC1 - Voice Command 1
Copyright (C) 2024  Olanorw aka Olav Sharma

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

from elevenlabs import save
from elevenlabs.client import ElevenLabs
from rich import print
import time
import requests
import re

# Define the ElevenLabsHandler class
class ElevenLabsHandler:
    """
    A class to handle interactions with the ElevenLabs API.
    
    Attributes:
    client (ElevenLabs): The ElevenLabs client object.
    
    Methods:
    generate(text, voice_id): Generate audio using the ElevenLabs API.
    check_voice_status(voice_id, api_key): Check the status of a voice ID using the ElevenLabs API.
    check_api_key(api_key): Check the validity of an API key using the ElevenLabs API.
    """
    def __init__(self, api_key):
        """
        Initialize the ElevenLabsHandler class with the provided API key.
        
        Args:
        api_key (str): The API key to use for ElevenLabs API requests.
        
        Example:
        el = ElevenLabsHandler("API KEY HERE")
        
        Returns:
        None
        """
        try:
            self.client = ElevenLabs(
                api_key=api_key # Initialize the ElevenLabs client with the provided API key
            )
        except Exception as e:
            print(f"[red]An error occurred while trying to initialize the ElevenLabs client. Error: {e}[/red]")
    
    def generate(self, text, voice_id):
        """
        Generate audio using the ElevenLabs API.
        
        Args:
        text (str): The text to generate audio from.
        voice_id (str): The voice ID to use for the audio.
        
        Example:
        el.generate("Hello, world!", "VOICE_ID_HERE")
        
        Returns:
        str: The file name of the generated audio.
        """
        try:
            print(f"[yellow]Making a request to the ElevenLabs API, please wait...[/yellow]")
            # Generate audio using the ElevenLabs client
            audio = self.client.generate(
                text=text,
                voice=voice_id,
                model="eleven_turbo_v2"
            )
        except Exception as e:
            print(f"[red]An error occurred while trying to generate audio. Error: {e}[/red]")
            return ElevenLabsHandler.generate(text, voice_id)
        
        try:
            # Save the generated audio to a file
            timestamp = str(int(time.time()))
            file_name = timestamp + '.mp3'
            save(audio, file_name)
        except Exception as e:
            print(f"[red]An error occurred while trying to save the audio. Error: {e}[/red]")
            return ElevenLabsHandler.generate(text, voice_id)
        
        return file_name
    
    def check_voice_status(voice_id, api_key):
        """
        Check the status of a voice ID using the ElevenLabs API.
        
        Args:
        voice_id (str): The voice ID to check the status of.
        api_key (str): The API key to use for the API request.
        
        Example:
        check_voice_status("VOICE_ID_HERE", "API_KEY_HERE")
        
        Returns:
        str: The status of the voice ID.
        """
        url = "https://api.elevenlabs.io/v1/voices/" + voice_id + "/"
        headers = {"xi-api-key": api_key}

        try:
            response = requests.request("GET", url, headers=headers)
            json_string = response.text
            match = re.search(r'"status":"(.*?)"', json_string)
        except Exception as e:
            print(f"[red]An error occurred while trying to check the voice status. Error: {e}[/red]")
            return ElevenLabsHandler.check_voice_status(voice_id, api_key)
        
        if match:
            status = match.group(1)
            if status == "voice_not_found":
                return "invalid"
            else:
                return "valid"
        else:
            print(f"Status not found")

    def check_api_key(api_key):
        """
        Check the validity of an API key using the ElevenLabs API.
        
        Args:
        api_key (str): The API key to check the validity of.
        
        Example:
        check_api_key("API_KEY_HERE")
        
        Returns:
        str: The validity of the API key.
        """
        url = "https://api.elevenlabs.io/v1/voices/"
        headers = {"xi-api-key": api_key}
        
        try:
            response = requests.request("GET", url, headers=headers)
        except Exception as e:
            print(f"[red]An error occurred while trying to check the API key. Error: {e}[/red]")
            return ElevenLabsHandler.check_api_key(api_key)
        
        if response.text == '{"detail":{"status":"invalid_api_key","message":"Invalid API key"}}':
            return "invalid"
        else:
            return "valid"
        
# Tests
if __name__ == "__main__":
    pass
