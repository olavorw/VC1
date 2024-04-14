import json
import os
import time
from rich import print

class Config:
    @staticmethod
    def prompt_eula():
        print("[yellow]By using this software, you agree to the EULA provided in the main directory.[/yellow]")
        print("[yellow]Do you agree to the EULA? (yes/no)")
        response = input()
        if response == "yes":
            with open('config.json', 'w') as file:
                json.dump({'eula': "true"}, file)
            print("[green]EULA accepted.[/green]")
            print("[green]Don't show again? You can always change this by deleting the config.json file in the main directory. (yes/no)[/green]")
            dontShowAgain = input()
            if dontShowAgain == "yes":
                with open('config.json', 'w') as file:
                    json.dump({'eula': "true", 'dontShowAgain': "true"}, file)
                print("[green]EULA will not be shown again. Reminder: You are still binded to the EULA by using this software. To reset this, delete config.json in the main directory.[/green]")
            else:
                with open('config.json', 'w') as file:
                    json.dump({'eula': "true"}, file)
                print("[green]EULA will be shown again.[/green]")
            return
        else:
            print("[red]You must agree to the EULA to use this software.[/red]")
            print("[red]Closing Program in 3 seconds.[/red]")
            time.sleep(3)
            exit()
    @staticmethod
    def call_api_key():
        print("[yellow]Please enter your ElevenLabs API key:[/yellow]")
        api_key = input()
        with open('config.json', 'w') as file:
            json.dump({'api_key': api_key}, file)
        print("[green]API key saved successfully.[/green]")
        return api_key

if __name__ == "__main__":
    api_key = Config.get_api_key()
    print("Your ElevenLabs API key is:", api_key)
