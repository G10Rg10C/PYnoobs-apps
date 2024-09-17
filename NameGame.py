# Questo è un commento. Non viene eseguito dal programma.

# Dichiarazione di una variabile e assegnamento di un valore
nome = input("Inserisci il tuo nome!")

# Stampa il contenuto della variabile
print("Ora valuteremo la lunghezza del tuo nome")

# Inserimento di un parametro temporale in base ai secondi
import time
time.sleep(1.75)

# Esempio di utilizzo di più condizioni if-elif-else
if len(nome) == 5 or len(nome) == 6 or len(nome) == 7  : 
    print("Hai un nome di lunghezza normale!")
elif len(nome) == 8 :
    print("Il tuo nome è lungo!")
elif len(nome) == 4 :
    print("Il tuo nome è corto!")
elif len(nome) < 4 :
    print("Hai un nome è cortissimo!")    
else:
    print("Hai un nome lunghissimo!") 

import time
time.sleep(2.4)

 