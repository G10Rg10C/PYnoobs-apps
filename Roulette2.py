import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import random
import math

# Crea la finestra principale
root = tk.Tk()
root.title("Roulette")

# Carica l'immagine della roulette e la converte in un formato Tkinter
roulette_img = Image.open(r"C:\Users\giorgio\OneDrive\Desktop\Raccoglitore\Creazioni personali e Media Vari\Scrypt in PY\roulette\roulette.png")
roulette_tk = ImageTk.PhotoImage(roulette_img)

# Imposta l'immagine della roulette come sfondo della finestra
root.geometry(f"{roulette_img.width}x{roulette_img.height}")
root.configure(bg="white")

background_label = tk.Label(root, image=roulette_tk)
background_label.place(relwidth=1, relheight=1)

# Funzione per generare un numero casuale da 1 a 31
def roulette():
    return random.randint(0, 36)

def ruota_roulette1():
    numero = roulette()

    # Carica l'immagine della roulette
    roulette_img = Image.open(r"C:\Users\giorgio\OneDrive\Desktop\Raccoglitore\Creazioni personali e Media Vari\Scrypt in PY\roulette\roulette.png")

    # Calcola l'angolo in cui posizionare il pallino rosso
    angolo = 360 / 37 * (numero - 1)
    angolo_rad = math.radians(angolo)

    # Crea un'immagine copia per disegnare il pallino rosso
    roulette_copia = roulette_img.copy()

    # Crea un disegnatore sull'immagine
    disegnatore = ImageDraw.Draw(roulette_copia)

    # Calcola le coordinate del centro e del pallino rosso
    centro_x = roulette_img.width // 2
    centro_y = roulette_img.height // 2
    x = centro_x + int(centro_x * 0.8 * math.cos(angolo_rad))
    y = centro_y - int(centro_y * 0.8 * math.sin(angolo_rad))

    # Disegna il pallino rosso
    disegnatore.ellipse((x - 10, y - 10, x + 10, y + 10), fill="blue")

    # Converte l'immagine modificata in un formato Tkinter
    roulette_tk = ImageTk.PhotoImage(roulette_copia)

    # Aggiorna l'immagine sulla canvas
    background_label.config(image=roulette_tk)
    background_label.image = roulette_tk

# Funzione per ruotare la roulette e visualizzare il numero casuale
def ruota_roulette():
    numero = roulette()
    label_numero.config(text=f"Numero: {numero}")


# Crea una label per visualizzare il numero casuale
label_numero = tk.Label(root, text="", font=("Helvetica", 24))
label_numero.pack()

# Crea un pulsante per ruotare la roulette
pulsante_ruota = tk.Button(root, text="Ruota la roulette", command=lambda: [ruota_roulette(), ruota_roulette1()])
pulsante_ruota.pack()

# Avvia l'applicazione
root.mainloop()
