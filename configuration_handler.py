import json
import time
from tkinter import N
from rich import print
from elevenlabs_handler import ElevenLabsHandler

class ConfigurationHandler():
    config_file_path = 'config.json'

    def read_config():
        try:
            with open(ConfigurationHandler.config_file_path, 'r') as file:
                config = json.load(file)
                return config
                
        except FileNotFoundError:
            return {}

    def rewrite_config(data):
        with open(ConfigurationHandler.config_file_path, 'w') as file:
            json.dump(data, file)

    def write_config(data):
        existing_data = ConfigurationHandler.read_config()
        
        existing_data.update(data)  # Merge new data with existing data
        with open(ConfigurationHandler.config_file_path, 'w') as file:
            json.dump(existing_data, file)

    def prompt_agreements():
        config = ConfigurationHandler.read_config() # Read the configuration file to check if the license and permission notice has already been accepted or doesn't need to be shown again
        if config.get('license') == "true" and config.get('dontShowAgain') == "true":
            print(f"[green]Code of Conduct, License, and Permission notice has already been accepted and will not be shown again as requested by the user. You are still bound to the license and permission notice when using this software.[/green]")
            return
        
        # Prompt the user to view the license and permission notice
        print(f"[yellow]By using this software, you agree to the Code of Conduct, License, and Permission notice in the \"LICENSE.md\" and \"CODE_OF_CONDUCT.md\" files respectively.[/yellow]")
        print(f"[yellow]Please read the Code of Conduct and License file.[/yellow]")
        with open('CODE_OF_CONDUCT.md', 'r') as file:
            code_of_conduct = file.read()
            print(f"[white]\n" + code_of_conduct)
        with open('LICENSE.md', 'r') as file:
            license = file.read()
            print(f"[white]\n" + license)
        print(f"\n[yellow]Please wait...[/yellow]\n")
        # Give the user time to read the license and permission notice before prompting them to accept it
        time.sleep(3)
            
        # Prompt the user to accept the license and permission notice
        print(f"[yellow]Have you read and agree to the Code of Conduct, License, and Permission notice? (yes/no)")
        response = input().strip().lower()
        if response == "yes":
            config['license'] = "true"
            print(f"[green]License and permission notice accepted.[/green]")
        else:
            print(f"[red]You must agree to the license and permission notice to use this software.[/red]")
            agreementCloseCountdown = 3
            for i in range(agreementCloseCountdown, 0, -1):
                print(f"[red]Closing Program in {i} seconds.[/red]")
            exit()
            
        # Prompt the user to choose whether to show the license and permission notice on startup
        print(f"[yellow]Don't ask again?\nYou can always change this by deleting the config.json file in the main directory.\n(yes/no)[/yellow]")
        dontShowAgain = input().strip().lower()
        if dontShowAgain == "yes":
            config['dontShowAgain'] = "true"
            print(f"[green]Code of Conduct, License and Permission notice will not be prompted for again, you are still bound to them. To reset this, delete config.json in the main directory.[/green]")
        else:
            config.pop('dontShowAgain', None)
            print(f"[green]Code of Conduct, License and Permission notice will be prompted on startup.[/green]")
        ConfigurationHandler.write_config(config)

    # Ask the user for their ElevenLabs API key
    def prompt_api_key():
        print(f"[yellow]Please enter your ElevenLabs API key:[/yellow]")
        api_key = input()
        
        print(f"[yellow]Checking API key...[/yellow]")
        status = ElevenLabsHandler.check_api_key(api_key) # Check if the API key is valid
        if status == "invalid":
            print(f"[red]Invalid API key.[/red]")
            print(f"[yellow]Returning.[/yellow]")
            return ConfigurationHandler.prompt_api_key() # Prompt the user for the API key again
        elif status == "valid":
            print(f"[green]API key is valid. Saving API key.[/green]")
            ConfigurationHandler.write_config({'api_key': api_key}) # Save the API key to the configuration file
            print(f"[green]API key saved successfully. To change your API key, delete the config.json file.[/green]")
            return api_key

    def get_api_key():
        config = ConfigurationHandler.read_config() # Read the configuration file
        if 'api_key' not in config:
            return ConfigurationHandler.prompt_api_key()
        else:
            return config.get('api_key') # Return the API key if it exists
    
    def get_voice_ids():
        config = ConfigurationHandler.read_config()
        return config.get('voice_ids', {})  # Ensures a dictionary is returned even if 'voice_ids' does not exist
    
    def prompt_voice_id():
        # Find out if there are any voice IDs stored in the configuration file
        voice_ids = ConfigurationHandler.get_voice_ids()
        if voice_ids:
            print(f"[green]Voice ID(s) retrieved.[/green]\n[yellow]Please select a voice by typing its name, or add a new voice by typing 'new'[/yellow]")
            for name, id in voice_ids.items():
                print(f"Name: {name}, Voice ID: {id}")
            print(f"[yellow]Make a selection:[/yellow]")
            selection = input()
            if selection != "new":
                return voice_ids.get(selection, "No such voice found.")
        # If no voice IDs are stored, prompt the user to add a new voice ID
        else:
            print(f"[yellow]No voice IDs stored. Enter 'new' to add a voice:[/yellow]")
            selection = input()
        
        # If the user wants to add a new voice ID
        if selection == "new":
            print(f"[yellow]Please enter a new ElevenLabs voice ID:[/yellow]")
            voice_id = input()
            
            print(f"[yellow]Checking voice ID...[/yellow]")
            status = ElevenLabsHandler.check_voice_status(voice_id, ConfigurationHandler.get_api_key()) # Check if the voice ID is valid
            if status == "invalid":
                print(f"[red]Invalid voice ID.[/red]")
                print(f"[yellow]Returning.[/yellow]")
                ConfigurationHandler.prompt_voice_id()
            if status == "valid":
                print(f"[green]Voice ID is valid.[/green]")
                
                print(f"[yellow]Would you like to save this voice ID? (yes/no)[/yellow]")
                save_voice = input().strip().lower()
                if save_voice == "yes":
                    name = ""
                    while True:
                        print(f"[yellow]Please enter a name to save this voice ID under:[/yellow]")
                        name = input()
                        if name.lower() != "new":
                            break
                        print(f"[red]Invalid name. 'new' is not allowed as a name. Please enter a different name:[/red]")
                    voice_ids[name] = voice_id  # Use the name as the key and voice ID as the value
                    ConfigurationHandler.write_config({'voice_ids': voice_ids})
                    print(f"[green]Voice ID saved successfully under the name: {name}[green]")
                elif save_voice == "no":
                    print(f"[yellow]Voice ID not saved.[/yellow]")
                    print(f"[yellow]Proceeding[/yellow]")
                    
                return voice_id
        else:
            print(f"[red]Invalid option.[/red]")
            print(f"[yellow]Returning.[/yellow]")
            
            ConfigurationHandler.prompt_voice_id()
    
    def remove_config_item(item):
        config = ConfigurationHandler.read_config()
        if item in config:
            config.pop(item)
            print(config)
            ConfigurationHandler.rewrite_config(config)
            print(f"[green]{item} removed from configuration.[/green]")
        else:
            print(f"[red]{item} not found in configuration.[/red]")

# Tests
if __name__ == "__main__":
    ConfigurationHandler.prompt_license()
    ConfigurationHandler.get_api_key()
    ConfigurationHandler.prompt_voice_id()