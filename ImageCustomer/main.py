# Menu di opzioni
from model.customer import ImageManipulator

text = '''
0) Rende l'immagine tonda
1) Ridimensiona l'immagine a nuove dimensioni specificate.
2) Ridimensiona l'immagine mantenendo il rapporto d'aspetto originale, adattandola ai limiti di larghezza e altezza massimi.
3) Ruota l'immagine di un angolo specificato (in gradi).
4) Applica un filtro di sfocatura all'immagine.
5) Applica un filtro per aumentare la nitidezza dell'immagine.
6) Applica un filtro di contorno.
7) Converte l'immagine in scala di grigi.
8) Converte l'immagine in modalità RGB.
9) Salva l'immagine nel percorso specificato e con il formato desiderato.
10) Mostra l'immagine in una finestra.
11) Esci
'''

print(text)

# Inizializza la variabile choice
choice = None
while True:
    try:
        path = input("Enter the file path of the image: ").strip()
        path = path.replace("\"", "")  # per doppi apici
        path = path.replace("\'", "")  # per apici singoli
        print(path)
        image_manipulator = ImageManipulator(path)  # Crea un oggetto per manipolare l'immagine
        break
    except Exception as e:
        print(e)

while choice != "12":
    try:
        # Chiedi il percorso dell'immagine

        # Mostra il menu e prendi la scelta dell'utente
        choice = input("\nEnter choice: ").strip()

        # Usa il match-case per chiamare la funzione corrispondente
        match choice:
            case "0":
                image_manipulator.resize_round()
                print("L'immagine è stata resa tonda.")
            case "1":
                new_width = int(input("Enter new width: "))
                new_height = int(input("Enter new height: "))
                image_manipulator.resize(new_width, new_height)
                print(f"L'immagine è stata ridimensionata a {new_width}x{new_height}.")
            case "2":
                max_width = int(input("Enter max width: "))
                max_height = int(input("Enter max height: "))
                image_manipulator.resize_aspect_ratio(max_width, max_height)
                print(f"L'immagine è stata ridimensionata mantenendo il rapporto d'aspetto.")
            case "3":
                angle = int(input("Enter rotation angle (in degrees): "))
                image_manipulator.rotate(angle)
                print(f"L'immagine è stata ruotata di {angle} gradi.")
            case "4":
                image_manipulator.apply_blur()
                print("È stato applicato il filtro di sfocatura.")
            case "5":
                image_manipulator.apply_sharpen()
                print("È stato applicato il filtro di nitidezza.")
            case "6":
                image_manipulator.apply_contour()
                print("È stato applicato il filtro di contorno.")
            case "7":
                image_manipulator.convert_to_grayscale()
                print("L'immagine è stata convertita in scala di grigi.")
            case "8":
                image_manipulator.convert_to_rgb()
                print("L'immagine è stata convertita in modalità RGB.")
            case "9":
                output_path = input("Enter output path: ")
                image_manipulator.save(output_path)
                print(f"L'immagine è stata salvata in {output_path}.")
            case "10":
                image_manipulator.show()
                print("L'immagine è stata mostrata.")
            case "11":
                print("Uscita dal programma.")
                break
            case _:
                print("Scelta non valida, per favore inserisci un'opzione valida.")
    except Exception as e:
        print(f"Errore: {e}")
