"""
VC1 - Voice Command 1
Copyright (C) 2024  Olanorw aka Olav SHarma

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import requests
from rich import print

class WebHandler:
    """
    A class to handle web interactions tailored to the VC1 project.
    
    Attributes:
    None
    
    Methods:
    check_for_updates(current_version): Check for updates to VC1 by comparing the current version with the latest version available on the website.
    notify_update(latest_version): Notify the user that a new version of VC1 is available.
    check_if_usable(): Check if VC1 is usable by pinging the website.
    """
    @staticmethod
    def check_for_updates(current_version):
        """
        Check for updates to VC1 by comparing the current version with the latest version available on the website.
        
        Args:
        current_version (str): The current version of VC1.
        
        Example:
        WebHandler.check_for_updates("0.5")
        
        Returns:
        None
        """
        try:
            response = requests.get("https://olanorw.com/projects/vc1/version.json")
            latest_version = response.text.strip()
            if current_version < latest_version:
                WebHandler.notify_update(latest_version)
        except Exception as e:
            print(f"[red]Failed to check for updates: {e}")
    
    @staticmethod
    def notify_update(latest_version):
        """
        Notify the user that a new version of VC1 is available.
        
        Args:
        latest_version (str): The latest version of VC1 available on the website.
        
        Example:
        WebHandler.notify_update("0.6")
        
        Returns:
        None
        """
        print(f"[yellow]A new version of VC1 is available! [cyan]{latest_version}[/cyan]\n[yellow]You can download it from [cyan]https://olanorw.com/projects/vc1/download[/cyan]")
    
    @staticmethod
    def check_if_usable():
        """
        Check if VC1 is usable by pinging the website.
        
        Args:
        None
        
        Example:
        WebHandler.check_if_usable()
        
        Returns:
        bool: True if VC1 is usable, False if VC1 is unusable, 'error' if an error occurred.
        """
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
    current_version = "0.45"
    WebHandler.check_for_updates(current_version)

    print(f"[yellow]Testing up-to-date[/yellow]")
    current_version = "0.5"
    WebHandler.check_for_updates(current_version)
