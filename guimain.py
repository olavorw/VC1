import pygame
import sys
import io
import time
import threading
from elevenlabs_handler import ElevenLabsHandler
from audio_handler import AudioHandler
from speech_to_text_handler import SpeechToTextHandler
from configuration_handler import ConfigurationHandler
from web_handler import WebHandler
from rich import print

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 900, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame GUI with Embedded Console')

# Load images
bg_image = pygame.image.load('./testing/gui/bg.png')
api_key_icon = pygame.image.load('./testing/gui/api-key-icon.png')

# Set positions
sidebar_width = 82  # Width of the sidebar
console_x = sidebar_width  # Console starts right after the sidebar
console_width = screen_width - sidebar_width  # Remaining width for the console
button_x = 10  # X position for the button (left side of the sidebar)
button_y = 5  # Y position for the button (top of the sidebar)

# Font settings for console
font = pygame.font.SysFont("Consolas", 17, bold=True)

input_text = ''
console_lines = []
input_active = False  # Flag to control whether input is allowed
cursor_visible = True  # To control cursor blinking
cursor_blink_time = 500  # Cursor blink time in milliseconds
last_blink = pygame.time.get_ticks()  # Track time for blinking

def wrap_text(text, font, max_width):
    """Wrap text to fit within the specified width when rendered with the given font."""
    words = text.split(' ')
    lines = []
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + ' ' + word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

def draw_console():
    console_surface = pygame.Surface((console_width, screen_height - 30))
    console_surface.fill((12, 12, 12))  # Console background color

    # Draw the console output lines
    y_offset = 10
    for line in console_lines[-20:]:  # Show only the last 20 lines
        wrapped_lines = wrap_text(line, font, console_width - 20)
        for wrapped_line in wrapped_lines:
            rendered_line = font.render(wrapped_line, True, (204, 204, 204))
            console_surface.blit(rendered_line, (10, y_offset))
            y_offset += rendered_line.get_height() + 3  # Adjust spacing to improve readability

    screen.blit(console_surface, (console_x, 0))

def draw_input_box():
    global cursor_visible, last_blink
    
    input_box_surface = pygame.Surface((console_width, 30))
    input_box_surface.fill((23, 23, 23))  # Input box background color

    # Blinking cursor logic
    if pygame.time.get_ticks() - last_blink > cursor_blink_time:
        cursor_visible = not cursor_visible
        last_blink = pygame.time.get_ticks()

    # Append cursor to input text if visible and input is active
    display_text = input_text + ('_' if cursor_visible and input_active else '')

    # Draw the current input text
    rendered_input = font.render(display_text, True, (204, 204, 204))
    input_box_surface.blit(rendered_input, (10, 5))

    screen.blit(input_box_surface, (console_x, screen_height - 30))

def add_console_line(text):
    # Split text at newline characters and add each line individually
    lines = text.split('\n')
    for line in lines:
        console_lines.append(line)
        if len(console_lines) > 1000:  # Prevent memory issues by keeping only the last 1000 lines
            console_lines.pop(0)

def request_input():
    global input_active
    input_active = True

def stop_input():
    global input_active
    input_active = False

class ConsoleStream(io.StringIO):
    def __init__(self):
        super().__init__()
        self.orig_stdout = sys.__stdout__  # Store the original stdout to avoid recursion
        self.orig_stderr = sys.__stderr__

    def write(self, text):
        if text:  # Avoid adding empty lines
            add_console_line(text)
            self.orig_stdout.write(text)  # Optionally also write to the original stdout

    def flush(self):
        self.orig_stdout.flush()
        self.orig_stderr.flush()

# Redirect stdout and stderr
sys.stdout = ConsoleStream()
sys.stderr = ConsoleStream()

# Main logic from the second script
def main_logic():
    print(f"\n[yellow]VC1 Copyright (C) 2024  Olav Sharma This program comes with ABSOLUTELY NO WARRANTY; for details say `show w'. This is free software, and you are welcome to redistribute it under certain conditions; say `show c' for details.\n")

    def show_w():
        try:
            with open('CODE_OF_CONDUCT.md', 'r') as file:
                code_of_conduct = file.read()
                print(f"[bold white]\n" + code_of_conduct)
            with open('LICENSE.md', 'r') as file:
                license = file.read()
                print(f"[white]\n" + license)
        except Exception as e:
            print(f"[red]An error occurred while trying to show the warranty information. Please check the files and try again. Error: {e}[/red]")

    def show_c():
        try:
            with open('LICENSE.md', 'r') as file:
                license = file.read()
                print(f"[white]\n" + license)
            with open('CODE_OF_CONDUCT.md', 'r') as file:
                code_of_conduct = file.read()
                print(f"[bold white]\n" + code_of_conduct)
        except Exception as e:
            print(f"[red]An error occurred while trying to show the license information. Please check the files and try again. Error: {e}[/red]")

    try:
        print(f"[bold white]__/\\\\\\________/\\\\\\_        ________/\\\\\\\\\\\\\\\\\\_        ______/\\\\\\_\n _\\/\\\\\\_______\\/\\\\\\_        _____/\\\\\\////////__        __/\\\\\\\\\\\\\\_\n  _\\//\\\\\\______/\\\\\\__        ___/\\\\\\/___________        _\\/////\\\\\\_\n   __\\//\\\\\\____/\\\\\\___        __/\\\\\\_____________        _____\\/\\\\\\_\n    ___\\//\\\\\\__/\\\\\\____        _\\/\\\\\\_____________        _____\\/\\\\\\_\n     ____\\//\\\\\\/\\\\\\_____        _\\//\\\\\\____________        _____\\/\\\\\\_\n      _____\\//\\\\\\\\\\______        __\\///\\\\\\__________        _____\\/\\\\\\_\n       ______\\//\\\\\\_______        ____\\////\\\\\\\\\\\\\\\\\\_        _____\\/\\\\\\_\n        _______\\///________        _______\\/////////__        _____\\///_\n")
        print(f"Loading VC1...")
        time.sleep(3)
    except Exception as e:
        print(f"[red]An error occurred while trying to load VC1. Error: {e}[/red]")

    try:
        print(f"[yellow]Loading ConfigurationHandler...[/yellow]")
        Config = ConfigurationHandler()
        Config.prompt_agreements()  # Prompt the user to accept the EULA
    except Exception as e:
        print(f"[red]An error occurred while trying to prompt the user to accept the EULA. Error: {e}[/red]")
        exit()

    try:
        print("Loading WebHandler...")
        Online = WebHandler()
        if Online.check_if_usable() == False:
            print(f"[red]VC1 is currently unusable.[/red]")
            exit()
        elif Online.check_if_usable() == True:  # If VC1 is usable, continue  
            pass
        else:  # If an error occurred while checking if VC1 is usable, print a message and exit the program
            print(f"[red]An error occurred while checking if VC1 is usable. Please check your internet connection. Closing program...[/red]")
            exit()
        
        # Check for updates
        current_version = '0.5'
        Online.check_for_updates(current_version)
    except Exception as e:
        print(f"[red]An error occurred while trying to check if VC1 is usable. Error: {e}[/red]")

    try:
        api_key = Config.get_api_key()  # Get or prompt for the API key for initializing the ElevenLabs client
    except Exception as e:
        print(f"[red]An error occurred while trying to get the API key. Error: {e}[/red]")

    try:
        print(f"[yellow]Initializing ElevenLabsHandler, SpeechRecognition, and AudioHandler...[/yellow]")
        TTS = ElevenLabsHandler(api_key)
        STT = SpeechToTextHandler()
        Audio = AudioHandler()
    except Exception as e:
        print(f"[red]An error occurred while trying to initialize the ElevenLabs client, SpeechRecognition, or AudioHandler. Error: {e}[/red]")

    try:
        # Get the voice ID
        print(f"[yellow]Please enter your ElevenLabs voice ID...[/yellow]")
        voice_id = ConfigurationHandler.prompt_voice_id()
        print(f"[green]Selected Voice ID: {voice_id}.[/green]")  # Let the user know that the voice ID has been selected
    except Exception as e:
        print(f"[red]An error occurred while trying to get the voice ID. Error: {e}[/red]")

    try:
        # Initialize the main loop
        while True:
            result = STT.listen_and_recognize()  # Get the recognized speech from the microphone using SpeechRecognition
        
            if str.lower(result) == "show w":
                show_w()
            elif str.lower(result) == "show c" or str.lower(result) == "chelsea" or str.lower(result) == "josie":  # Google may detect "show c" as "chelsea" or "josie" sometimes
                show_c()

            audio_file = TTS.generate(result, voice_id)  # Get the audio for the specified voice ID using ElevenLabsSpeech
            time.sleep(0.5)  # Waiting to make sure everything is ready
        
            Audio.play_audio(audio_file, True)  # Play the generated audio using AudioHandler
    except Exception as e:
        print(f"[red]An error occurred while trying to run the main loop. Error: {e}[/red]")

# Main loop for GUI
running = True
main_logic_thread_started = False  # Flag to ensure the main logic starts only once

def start_main_logic():
    main_logic()

# Run the main logic in a separate thread
main_logic_thread = threading.Thread(target=start_main_logic)
main_logic_thread.daemon = True  # Set as a daemon thread to close with the main program
main_logic_thread.start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                # Check if the button is clicked
                if button_x <= mouse_pos[0] <= button_x + api_key_icon.get_width() and \
                   button_y <= mouse_pos[1] <= button_y + api_key_icon.get_height():
                    print("API Key button clicked!")
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                print(f'> {input_text}')
                input_text = ''
                stop_input()  # Stop input after Enter is pressed
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Draw the background image
    screen.blit(bg_image, (0, 0))

    # Draw the API key button on the sidebar
    screen.blit(api_key_icon, (button_x, button_y))

    # Draw the embedded console
    draw_console()

    # Draw the input box at the bottom
    draw_input_box()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
