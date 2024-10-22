import pygame
import sys
import io
import time

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
# Changing to "DejaVu Sans Mono" with a slightly larger font size
font = pygame.font.SysFont("DejaVu Sans Mono", 20, bold=False)

input_text = ''
console_lines = []
input_active = False  # Flag to control whether input is allowed
cursor_visible = True  # To control cursor blinking
cursor_blink_time = 500  # Cursor blink time in milliseconds
last_blink = pygame.time.get_ticks()  # Track time for blinking

def draw_console():
    console_surface = pygame.Surface((console_width, screen_height - 30))
    console_surface.fill((12, 12, 12))  # Console background color

    # Draw the console output lines
    y_offset = 10
    for line in console_lines[-20:]:  # Show only the last 20 lines
        rendered_line = font.render(line, True, (204, 204, 204))
        console_surface.blit(rendered_line, (10, y_offset))
        y_offset += rendered_line.get_height() + 5

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
    console_lines.append(text)
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
        if text.strip():  # Avoid adding empty lines
            add_console_line(text.strip())
            self.orig_stdout.write(text)  # Optionally also write to the original stdout

    def flush(self):
        self.orig_stdout.flush()
        self.orig_stderr.flush()

# Redirect stdout and stderr
sys.stdout = ConsoleStream()
sys.stderr = ConsoleStream()

# Example of how to use request_input
# You can call this in your code to start capturing input
def example_function():
    print("Example function output:")
    request_input()

# Main loop
running = True
example_function()  # Call example function to test input capturing

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
