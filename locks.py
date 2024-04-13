import json
import os

class Lock:
    @staticmethod
    def setup_api_key():
        api_key = input("Enter your ElevenLabs API Key: ")
        with open('config.json', 'w') as file:
            json.dump({'elevenlabs_api_key': api_key}, file)

    @staticmethod
    def get_api_key():
        if not os.path.exists('config.json'):
            Lock.setup_api_key()

        with open('config.json', 'r') as file:
            try:
                config = json.load(file)
                api_key = config.get('elevenlabs_api_key')
                if not api_key:
                    print("API key not found in config.json.")
                    Lock.setup_api_key()
                    return Lock.get_api_key()
                return api_key
            except json.JSONDecodeError:
                print("Error reading the config file. It might be corrupted.")
                os.remove('config.json')
                return Lock.get_api_key()

if __name__ == "__main__":
    api_key = Lock.get_api_key()
    print("Your ElevenLabs API key is:", api_key)
