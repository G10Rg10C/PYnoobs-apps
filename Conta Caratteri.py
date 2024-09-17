import tkinter as tk

def conta_caratteri():
    testo = entry.get()
    caratteri = len(testo)
    label.config(text=f"Numero di caratteri: {caratteri}")

# Creazione della finestra principale
root = tk.Tk()
root.title("Contatore Caratteri")

# Creazione della casella di testo e del pulsante
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

pulsante = tk.Button(root, text="Conta Caratteri", command=conta_caratteri)
pulsante.pack()

label = tk.Label(root, text="")
label.pack()

# Avvio del loop dell'interfaccia grafica
root.mainloop()
