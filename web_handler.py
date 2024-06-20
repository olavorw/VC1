import requests
from rich import print
import main

# Define the WebHandler class
class WebHandler:
    
    # Define a static method to check for updates
    def check_for_updates(current_version):
        # Try to get the latest version from the server
        try:
            # Get the latest version from the server
            response = requests.get("https://olanorw.com/projects/vc1/version.json")
            # If the response is successful, get the latest version
            latest_version = response.text.strip()
            # Compare the current version with the latest version
            if current_version < latest_version:
                # Notify the user that a new version is available
                WebHandler.notify_update(latest_version)
        # Handle exceptions
        except Exception as e:
            # Print an error message if failed to check for updates
            print(f"[red]Failed to check for updates: {e}")
    
    # Define a static method to notify the user of an update
    def notify_update(latest_version):
        # Notify the user that a new version is available
        print(f"[yellow]A new version of VC1 is available! [cyan]{latest_version}[/cyan]\n[yellow]You can download it from [cyan]https://olanorw.com/projects/vc1/download[/cyan]")
    
    # Define a static method to check if VC1 is usable
    def check_if_usable():
        # Try to get the usable status from the server
        try:
            # Get the usable status from the server
            response = requests.get("https://olanorw.com/projects/vc1/usable.json")
            # If the response is successful, check if VC1 is usable
            if response.status_code == 200:
                # VC1 is usable
                return True
            # If VC1 is not usable, return False
            else:
                # VC1 is not usable
                return False
        # Handle exceptions
        except:
            # Return 'error' if an error occurred
            return 'error'


# Tests
# Check if the script is being run as the main module
if __name__ == "__main__":
    # Print a message indicating that the test for outdated version is being performed
    print("[yellow]Testing outdated[/yellow]")
    
    # Set the current version to a specific value
    current_version = "0.41"
    
    # Call the check_for_updates method of the WebHandler class, passing the current version as an argument
    WebHandler.check_for_updates(current_version)
    
    # Print a message indicating that the test for up-to-date version is being performed
    print("[yellow]Testing up-to-date[/yellow]")
    
    # Set the current version to the value of the current_version variable in the main module
    current_version = main.current_version
    
    # Call the check_for_updates method of the WebHandler class, passing the current version as an argument
    WebHandler.check_for_updates(current_version)
