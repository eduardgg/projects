
import os
from PIL import Image

def modify(image_path):
    image1 = Image.open(image_path)
    image2 = Image.open(image_path)
    width, height = image1.size

    for x in range(width):
        for y in range(height):
            (r,g,b) = image1.getpixel((x,y))
            
            # Mètode Meu
            average = (r+g+b) // 3
            newColor =  (average, average, average)
            image1.putpixel((x, y), newColor)

            # Mètode oficial
            luminancia = round(0.299 * r + 0.587 * g + 0.114 * b)
            newColor =  (luminancia, luminancia, luminancia)
            image2.putpixel((x,y), newColor)

    image1.save("blackAndWhite1.jpg")
    image2.save("blackAndWhite2.jpg")

current_directory = os.getcwd()
path_to_change = os.path.join(current_directory, "fotoProva.jpg")
modify(path_to_change)