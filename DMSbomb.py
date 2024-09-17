import pyautogui
import time
import keyboard  # Aggiunta per gestire il pulsante di sicurezza

# Definisci il messaggio da inviare e il numero di ripetizioni
message = "IT'S A SCAAAAM!! ESCAPE AND DON'T CLICK IT "
repeat_count = 100000000000000  # Numero di volte in cui inviare il messaggio
interval = 0.0001  # Intervallo di 1/3 di secondo
safety_key = 'q'  # Pulsante di sicurezza per interrompere l'invio

# Pausa prima di iniziare per dare tempo all'utente di selezionare la chat
print(f"Hai 15 secondi per selezionare la chat. Premi '{safety_key}' per interrompere l'invio.")
time.sleep(20)

for i in range(repeat_count):
    if keyboard.is_pressed(safety_key):
        print(f"Interrotto dall'utente premendo '{safety_key}'")
        break
    # Scrivi il messaggio
    pyautogui.write(message)
    # Premi "invio" per inviare il messaggio
    pyautogui.press("enter")
    # Attendi l'intervallo definito
    time.sleep(interval)

print("Processo completato.")
