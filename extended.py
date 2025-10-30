import time
import sys
import os

# Clear screen for better visual effect
os.system('cls' if os.name == 'nt' else 'clear')

# Some colors for terminal text
class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

# Typewriter effect for any text
def type_text(text, delay=0.05, color=Color.CYAN):
    for char in text:
        sys.stdout.write(color + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Fancy title
title = """
 _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)
"""

# Print intro
type_text("Initializing Python environment...\n", 0.03, Color.YELLOW)
time.sleep(0.8)
type_text("Loading modules...", 0.04, Color.YELLOW)
time.sleep(0.6)
type_text("Connecting to terminal...", 0.04, Color.YELLOW)
time.sleep(1)

# Print ASCII art with delay
for line in title.splitlines():
    type_text(line, 0.002, Color.GREEN)
time.sleep(0.5)

# Animated dots
for i in range(3):
    sys.stdout.write(Color.CYAN + "\rPreparing greeting" + "." * (i + 1) + " " * (3 - i) + Color.RESET)
    sys.stdout.flush()
    time.sleep(0.6)
print("\n")

# The grand reveal
type_text("🌍 Hello, World! 🌍", 0.1, Color.RED)
time.sleep(0.5)
type_text("\nWelcome to the world of Python — where creativity meets logic! 🐍", 0.05, Color.GREEN)
time.sleep(0.4)
type_text("\nProgram complete. Have a great day! 🚀", 0.05, Color.YELLOW)
