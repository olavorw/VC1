import json
import os
import time
from rich import print

class ConfigurationHandler:
    config_file_path = 'config.json'

    @staticmethod
    def read_config():
        try:
            with open(ConfigurationHandler.config_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def write_config(data):
        existing_data = ConfigurationHandler.read_config()
        existing_data.update(data)  # Merge new data with existing data
        with open(ConfigurationHandler.config_file_path, 'w') as file:
            json.dump(existing_data, file)

    @staticmethod
    def prompt_eula():
        config = ConfigurationHandler.read_config()
        if config.get('eula') == "true" and config.get('dontShowAgain') == "true":
            print("[green]EULA has already been accepted and will not be shown again. You are still bound to the EULA when using this software.[/green]")
            return

        print("[yellow]By using this software, you agree to the EULA provided in the main directory.[/yellow]")
        print("[yellow]Do you agree to the EULA? (yes/no)")
        response = input().strip().lower()
        if response == "yes":
            config['eula'] = "true"
            print("[green]EULA accepted.[/green]")
            print("[yellow]Don't show again? You can always change this by deleting the config.json file in the main directory. (yes/no)[/yellow]")
            dontShowAgain = input().strip().lower()
            if dontShowAgain == "yes":
                config['dontShowAgain'] = "true"
                print("[green]EULA will not be shown again, you are still bound to the EULA. To reset this, delete config.json in the main directory.[/green]")
            else:
                config.pop('dontShowAgain', None)
                print("[green]EULA will be shown again.[/green]")
            ConfigurationHandler.write_config(config)
        else:
            print("[red]You must agree to the EULA to use this software.[/red]")
            print("[red]Closing Program in 3 seconds.[/red]")
            time.sleep(3)
            exit()

    @staticmethod
    def prompt_api_key():
        if ConfigurationHandler.get_api_key():
            print("[green]API key retrieved.[/green]")  # Indicate saved status without showing the key
            return
        print("[yellow]Please enter your ElevenLabs API key:[/yellow]")
        api_key = input()
        ConfigurationHandler.write_config({'api_key': api_key})
        print("[green]API key saved successfully. To change your API key, delete the config.json file.[/green]")
        return api_key

    @staticmethod
    def get_api_key():
        config = ConfigurationHandler.read_config()
        return config.get('api_key')
    
    @staticmethod
    def get_voice_ids():
        config = ConfigurationHandler.read_config()
        return config.get('voice_ids', {})  # Ensures a dictionary is returned even if 'voice_ids' does not exist
    
    @staticmethod
    def prompt_voice_id():
        voice_ids = ConfigurationHandler.get_voice_ids()
        if voice_ids:
            print("[green]Voice ID(s) retrieved. Please select a voice by name. To add a new voice, type 'new'.[green]")
            for name, id in voice_ids.items():
                print(f"Name: {name}, Voice ID: {id}")
            print("[yellow]Enter a name or type 'new' to add a new voice ID:")
            selection = input()
            if selection != "new":
                return voice_ids.get(selection, "No such voice ID found.")
        else:
            print("[yellow]No voice IDs stored. Enter 'new' to add a voice ID:[/yellow]")
            selection = input()
    
        if selection == "new":
            print("[yellow]Please enter a new ElevenLabs voice ID:[/yellow]")
            voice_id = input()
            print("[yellow]Would you like to save this voice ID? (yes/no)[/yellow]")
            save_voice = input().strip().lower()
            if save_voice == "yes":
                name = ""
                while True:
                    print("[yellow]Please enter a name to save this voice ID under:[/yellow]")
                    name = input()
                    if name.lower() != "new":
                        break
                    print("[red]Invalid name. 'new' is not allowed as a name. Please enter a different name:[/red]")
                voice_ids[name] = voice_id  # Use the name as the key and voice ID as the value
                ConfigurationHandler.write_config({'voice_ids': voice_ids})
                print(f"[green]Voice ID saved successfully under the name: {name}[green]")
            elif save_voice == "no":
                print("[yellow]Voice ID not saved. Proceeding...[/yellow]")
            return voice_id
        else:
            print("[red]Invalid option. Returning to the main menu.[/red]")
            return "Invalid selection"
    

if __name__ == "__main__":
    ConfigurationHandler.prompt_eula()
    if not (api_key := ConfigurationHandler.get_api_key()):
        api_key = ConfigurationHandler.prompt_api_key()
    print("Your ElevenLabs API key is:", api_key)