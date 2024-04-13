import requests

class ElevenLabsSpeech:

  @staticmethod
  # Define a method to get audio from the ElevenLabs API
  def get_audio(text, voice, key):
    # Set the chunk size for downloading the audio file
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice

    # Set the headers for the API request
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": key
    }

    # Set the data for the API request
    data = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    
    # Make a POST request to the API
    response = requests.post(url, json=data, headers=headers)
    file_name = "LatestSound" + '.mp3'
    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    return file_name