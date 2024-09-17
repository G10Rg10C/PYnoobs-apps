import pyautogui
import keyboard
import time

# Variabili di configurazione
click_interval = 0.1  # Intervallo tra i click (1 millisecondo per migliaia di click al minuto)
safety_start_key = 'q'  # Tasto per iniziare il cliccaggio
safety_stop_key = 'w'   # Tasto per fermare il cliccaggio

print(f"Premi '{safety_start_key}' per iniziare i click e '{safety_stop_key}' per fermarli.")

# Loop principale
while True:
    # Aspetta finché non viene premuto 'q' per iniziare
    if keyboard.is_pressed(safety_start_key):
        print("Cliccaggio automatico iniziato. Premi 'w' per fermare.")
        # Loop di cliccaggio
        while True:
            if keyboard.is_pressed(safety_stop_key):
                print("Cliccaggio automatico fermato.")
                break
            # Esegui il click sinistro
            pyautogui.click()
            # Attendi l'intervallo tra i click
            time.sleep(click_interval)
    # Evita di saturare la CPU durante l'attesa
    time.sleep(0.1)
q