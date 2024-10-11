
import os
from PIL import Image

def modify(image_path):

    imageLum = Image.open(image_path)
    imageSat = Image.open(image_path)
    width, height = imageLum.size

    for x in range(width):
        for y in range(height):
            pixel = imageLum.getpixel((x,y))
            maxim = max(pixel)/255
            minim = min(pixel)/255
            luminosity = maxim - minim
            if minim + maxim == 0:
                saturation = 0
            elif luminosity < 0.5:
                saturation = (maxim - minim)/(minim + maxim)
            else:
                saturation = (maxim - minim)/(2 - minim - maxim)
            # average = (pixel[0] + pixel[1] + pixel[2]) // 3
            # blackWhiteColor =  (average, average, average)
            luminosity = round(255*luminosity)
            saturation = round(255*saturation)
            imageLum.putpixel((x, y), (luminosity, luminosity, luminosity))
            imageSat.putpixel((x, y), (saturation, saturation, saturation))

    imageLum.save("imageLuminosity.jpg")
    imageSat.save("imageSaturation.jpg")

current_directory = os.getcwd()
path_to_change = os.path.join(current_directory, "fotoProva.jpg")
modify(path_to_change)