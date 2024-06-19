import json
import os
import time
from rich import print

class ConfigurationHandler:
    config_file_path = 'config.json'

    # Read the configuration file and return the data as a dictionary
    @staticmethod
    def read_config():
        try:
            with open(ConfigurationHandler.config_file_path, 'r') as file:
                config = json.load(file)
                return config
                
        except FileNotFoundError:
            return {}

    # Write data to the configuration file
    @staticmethod
    def write_config(data):
        existing_data = ConfigurationHandler.read_config()
        existing_data.update(data)  # Merge new data with existing data
        with open(ConfigurationHandler.config_file_path, 'w') as file:
            json.dump(existing_data, file)

    # Prompt the user to accept the EULA
    @staticmethod
    def prompt_eula():
        # Read the configuration file to check if the EULA has already been accepted or doesn't need to be shown again
        config = ConfigurationHandler.read_config()
        # If the EULA has already been accepted and the user doesn't want to see it again, skip the prompt
        if config.get('eula') == "true" and config.get('dontShowAgain') == "true":
            # Indicate that the EULA has been accepted and won't be shown again
            print("[green]EULA has already been accepted and will not be shown again. You are still bound to the EULA when using this software.[/green]")
            return
        # Show the EULA and prompt the user to accept it
        print("[yellow]By using this software, you agree to the End User License Agreement or EULA in the 'EULA.txt' file.[/yellow]")
        print("[yellow]Would you like to see a copy of the EULA here? (yes/no)[/yellow]")
        # Get user input and convert it to lowercase for case-insensitive comparison
        viewEULA = input().strip().lower()
        # If the user wants to view the EULA, read the file and display its contents
        if viewEULA == "yes":
            with open('EULA.txt', 'r') as file:
                content = file.read()
                print("[white]" + content)
            print("\n[yellow]Please wait...[/yellow]\n")
        # Give the user time to read the EULA before prompting them to accept it
        time.sleep(3)
        # Prompt the user to accept the EULA
        print("[yellow]Have you read and agreed to the EULA? (yes/no)")
        # Get user input and convert it to lowercase for case-insensitive comparison
        response = input().strip().lower()
        if response == "yes":
            config['eula'] = "true"
            print("[green]EULA accepted.[/green]")
            # Prompt the user to choose whether to show the EULA on startup
            print("[yellow]Don't ask again?\nYou can always change this by deleting the config.json file in the main directory.\n (yes/no)[/yellow]")
            dontShowAgain = input().strip().lower()
            if dontShowAgain == "yes":
                config['dontShowAgain'] = "true"
                # Indicate that the EULA won't be shown again
                print("[green]EULA will not be shown again, you are still bound to the EULA. To reset this, delete config.json in the main directory.[/green]")
            else:
                config.pop('dontShowAgain', None)
                print("[green]EULA will be prompted on startup.[/green]")
            ConfigurationHandler.write_config(config)
        else:
            print("[red]You must agree to the EULA to use this software.[/red]")
            countdown = 3
            for i in range(countdown, 0, -1):
                print("[red]Closing Program in {i} seconds.[/red]")
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
            print("[green]Voice ID(s) retrieved.[/green]\n[yellow]Please select a voice by typing its name, or add a new voice by typing 'new'[/yellow]")
            for name, id in voice_ids.items():
                print(f"Name: {name}, Voice ID: {id}")
            print("[yellow]Make a selection:[/yellow]")
            selection = input()
            if selection != "new":
                return voice_ids.get(selection, "No such voice found.")
        else:
            print("[yellow]No voice IDs stored. Enter 'new' to add a voice:[/yellow]")
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
                print("[yellow]Voice ID not saved.[/yellow]")
                print("[yellow]Proceeding[/yellow]")
            return voice_id
        else:
            print("[red]Invalid option.[/red]")
            print("[yellow]Returning.[/yellow]")
            ConfigurationHandler.prompt_voice_id()
    

if __name__ == "__main__":
    ConfigurationHandler.prompt_eula()
    if not (api_key := ConfigurationHandler.get_api_key()):
        api_key = ConfigurationHandler.prompt_api_key()
    print("Your ElevenLabs API key is:", api_key)
    ConfigurationHandler.prompt_voice_id()