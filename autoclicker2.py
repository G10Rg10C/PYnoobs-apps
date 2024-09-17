from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController
import time

# Impostazioni mouse e tastiera
mouse = MouseController()
keyboard = KeyboardController()

# Tasti di avvio e stop
start_key = KeyCode(char='q')
stop_key = KeyCode(char='w')

clicking = False  # Flag per gestire il loop dei click
click_interval = 0.001  # Intervallo tra i click

# Funzione per gestire i click
def start_clicking():
    global clicking
    while clicking:
        mouse.click(Button.left)
        time.sleep(click_interval)

# Gestore degli eventi della tastiera
def on_press(key):
    global clicking
    if key == start_key:
        if not clicking:
            clicking = True
            print("Cliccaggio iniziato.")
            start_clicking()  # Inizia il loop dei click
    elif key == stop_key:
        clicking = False
        print("Cliccaggio fermato.")

# Avvia il listener della tastiera
with Listener(on_press=on_press) as listener:
    listener.join()
