"""
VC1 - Voice Command 1
Copyright (C) 2024  Olanorw aka Olav SHarma

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
        self.client = ElevenLabs(
            api_key=api_key # Initialize the ElevenLabs client with the provided API key
        )

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
        print(f"[yellow]Making a request to the ElevenLabs API, please wait...[/yellow]")
        # Generate audio using the ElevenLabs client
        audio = self.client.generate(
            text=text,
            voice=voice_id,
            model="eleven_turbo_v2"
        )
        
        # Save the generated audio to a file
        timestamp = str(int(time.time()))
        file_name = timestamp + '.mp3'
        save(audio, file_name)
        
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

        response = requests.request("GET", url, headers=headers)
        json_string = response.text
        match = re.search(r'"status":"(.*?)"', json_string)
        
        if match:
            status = match.group(1)
            if status == "voice_not_found":
                return "invalid"
            elif status == "invalid_uid":
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
        response = requests.request("GET", url, headers=headers)
        
        if response.text == '{"detail":{"status":"invalid_api_key","message":"Invalid API key"}}':
            return "invalid"
        else:
            return "valid"
        
# Tests
if __name__ == "__main__":
    el = ElevenLabsHandler("API_KEY_HERE")
    # Check the validity of an API key
    el.generate("Hello, world!", "VOICE_ID_HERE")
