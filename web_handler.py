# web_handler.py
import requests
from rich import print

class WebHandler:
    
    @staticmethod
    def check_for_updates(current_version):
        try:
            response = requests.get("https://olanorw.com/projects/vc1/version.json")
            latest_version = response.text.strip()
            if current_version < latest_version:
                WebHandler.notify_update(latest_version)
        except Exception as e:
            print(f"[red]Failed to check for updates: {e}")
    
    @staticmethod
    def notify_update(latest_version):
        print(f"[yellow]A new version of VC1 is available! [cyan]{latest_version}[/cyan]\n[yellow]You can download it from [cyan]https://olanorw.com/projects/vc1/download[/cyan]")
    
    @staticmethod
    def check_if_usable():
        try:
            response = requests.get("https://olanorw.com/projects/vc1/usable.json")
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return 'error'


if __name__ == "__main__":
    print(f"[yellow]Testing outdated[/yellow]")
    current_version = "0.5"
    WebHandler.check_for_updates(current_version)

    print(f"[yellow]Testing up-to-date[/yellow]")
    WebHandler.check_for_updates(current_version)
