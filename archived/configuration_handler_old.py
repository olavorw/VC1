import time

class ConfigurationHandler:
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
        viewLicense = input().strip().lower()
        print(viewLicense)
        # If the user wants to view the EULA, read the file and display its contents
        if viewLicense == "yes":
            with open('EULA.txt', 'r') as file:
                content = file.read()
                print("[white]" + content)
            print("\n[yellow]Please wait...[/yellow]\n")
            # Give the user time to read the EULA before prompting them to accept it
            time.sleep(3)
            pass
        elif viewLicense == "no":
            pass
        else:
            print("[red]Invalid option. Please enter 'yes' or 'no' next time.[/red]")
            ConfigurationHandler.prompt_eula()
        # Prompt the user to accept the EULA
        print("[yellow]Have you read and agreed to the EULA? (yes/no)")
        # Get user input and convert it to lowercase for case-insensitive comparison
        response = input().strip().lower()
        if response == "yes":
            config['eula'] = "true"
            print("[green]EULA accepted.[/green]")
            # Prompt the user to choose whether to show the EULA on startup
            print("[yellow]Don't ask again?\nYou can always change this by deleting the config.json file in the main directory.\n(yes/no)[/yellow]")
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