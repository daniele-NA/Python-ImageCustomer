import os  # Importa il modulo os per gestire i file e le directory

from PIL import Image, ImageDraw, ImageFont, \
    ImageFilter  # Importa moduli dalla libreria Pillow per la manipolazione delle immagini

"""
1) resize_round: rende tonda l'immagine
2) resize: Ridimensiona l'immagine a nuove dimensioni specificate.
3) resize_aspect_ratio: Ridimensiona l'immagine mantenendo il rapporto d'aspetto originale, adattandola ai limiti di larghezza e altezza massimi.
4) rotate: Ruota l'immagine di un angolo specificato (in gradi).
5) crop: Esegue un taglio dell'immagine in base a una regione definita dai valori di sinistra, superiore, destra e inferiore.
6) apply_blur: Applica un filtro di sfocatura all'immagine.
7) apply_sharpen: Applica un filtro per aumentare la nitidezza dell'immagine.
8) apply_contour: Applica un filtro di contorno.
9) convert_to_grayscale: Converte l'immagine in scala di grigi.
10) convert_to_rgb: Converte l'immagine in modalità RGB.
11) save: Salva l'immagine nel percorso specificato e con il formato desiderato.
12) show: Mostra l'immagine in una finestra.
"""


# Classe che incapsula tutte le operazioni di manipolazione delle immagini
class ImageManipulator:
    def __init__(self, image_path):
        # Carica l'immagine dal percorso specificato
        self.image = Image.open(image_path)

    # 1) Funzione per rendere l'immagine tonda
    def resize_round(self):
        width, height = self.image.size  # Ottieni la larghezza e l'altezza dell'immagine
        if width != height:
            raise ValueError("L'immagine deve essere quadrata.")  # Alza un errore se l'immagine non è quadrata

        # Crea una maschera tonda (un cerchio trasparente)
        mask = Image.new('L', (width, height), 0)  # Crea una maschera in scala di grigi (bianca su sfondo nero)
        draw = ImageDraw.Draw(mask)  # Disegna sulla maschera
        draw.ellipse((0, 0, width, height), fill=255)  # Disegna un cerchio bianco

        # Applica la maschera all'immagine
        self.image.putalpha(mask)

    # 2) Funzione per ridimensionare l'immagine a nuove dimensioni specificate
    def resize(self, new_width, new_height):
        self.image = self.image.resize(
            (new_width, new_height))  # Usa il metodo resize di Pillow per modificare le dimensioni

    # 3) Funzione per ridimensionare l'immagine mantenendo il rapporto d'aspetto originale
    def resize_aspect_ratio(self, max_width, max_height):
        self.image.thumbnail((max_width, max_height))  # Mantieni il rapporto d'aspetto durante il ridimensionamento

    # 4) Funzione per ruotare l'immagine di un angolo specificato
    def rotate(self, angle):
        self.image = self.image.rotate(angle)  # Ruota l'immagine dell'angolo specificato

    # 5) Funzione per applicare un filtro di sfocatura
    def apply_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)  # Applica il filtro di sfocatura

    # 6) Funzione per applicare un filtro per aumentare la nitidezza
    def apply_sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)  # Applica il filtro di nitidezza

    # 7) Funzione per applicare un filtro di contorno
    def apply_contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)  # Applica il filtro di contorno

    # 8) Funzione per convertire l'immagine in scala di grigi
    def convert_to_grayscale(self):
        self.image = self.image.convert("L")  # Converte l'immagine in scala di grigi (modalità 'L')

    # 9) Funzione per convertire l'immagine in modalità RGB
    def convert_to_rgb(self):
        self.image = self.image.convert("RGB")  # Converte l'immagine in modalità RGB

    # 10) Funzione per salvare l'immagine come JPEG
    def save(self, output_path):
        """Salva l'immagine in formato JPEG, rimuovendo la trasparenza (se presente)."""
        # Rimuovi eventuali doppi apici o apici singoli nel percorso per evitare errori
        output_path = output_path.strip().replace("\"", "").replace("\'", "")

        # Verifica se la directory di destinazione esiste, se no la crea
        output_dir = os.path.dirname(output_path)  # Ottieni la directory dal percorso
        if output_dir and not os.path.exists(output_dir):  # Se la directory non esiste
            os.makedirs(output_dir)  # Crea la directory

        # Se l'immagine è in modalità RGBA (con trasparenza), la converte in RGB
        if self.image.mode == 'RGBA':
            self.image = self.image.convert('RGB')  # Rimuove il canale alfa per salvare in formato JPEG

        # Salva l'immagine nel percorso specificato come JPEG
        self.image.save(output_path, format="JPEG")

    # 11) Funzione per mostrare l'immagine a schermo
    def show(self):
        """Mostra l'immagine a schermo."""
        self.image.show()  # Mostra l'immagine in una finestra
