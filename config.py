import json
import os

class Config:
    @staticmethod
    def setup_api_key():
        api_key = input("Enter your ElevenLabs API Key: ")
        with open('config.json', 'w') as file:
            json.dump({'elevenlabs_api_key': api_key}, file)

    @staticmethod
    def get_api_key():
        if not os.path.exists('config.json'):
            Config.setup_api_key()
        with open('config.json', 'r') as file:
            try:
                config = json.load(file)
                api_key = config.get('elevenlabs_api_key')
                if not api_key:
                    print("API key not found in config.json.")
                    Config.setup_api_key()
                    return Config.get_api_key()
                return api_key
            except json.JSONDecodeError:
                print("Error reading the config file. It might be corrupted.")
                os.remove('config.json')
                return Config.get_api_key()
    @staticmethod
    def dont_ask_again(value):
        config_path = 'config.json'
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                config = json.load(file)
            config['dont_ask_again'] = value
            with open(config_path, 'w') as file:
                json.dump(config, file)
        else:
            # If the file does not exist, create it with the default configuration.
            with open(config_path, 'w') as file:
                json.dump({'dont_ask_again': value}, file)

if __name__ == "__main__":
    api_key = Config.get_api_key()
    print("Your ElevenLabs API key is:", api_key)
