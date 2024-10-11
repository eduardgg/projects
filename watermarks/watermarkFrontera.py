
import random
import os
from PIL import Image

white = (255, 255, 255)
black = (0, 0, 0)

def neighbors(position):
    # Vigilar: aquest codi accepta posicions fora del rang, si "position" està a un costat de la imatge
    # Ho tenim en compte durant el codi, analitzant els pixels només de l'interior de la imatge.
    x = position[0]
    y = position[1]
    return [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]

def isWhite(pixel):
    if pixel[0] + pixel[1] + pixel[2] > 660:
        return True
    return False

def isBlack(pixel):
    if pixel[0] + pixel[1] + pixel[2] < 120:
        return True
    return False

def isGrey(pixel):
    if max(pixel) - min(pixel) < 10:
        return True
    return False

def remove_watermark(image_path):
    image = Image.open(image_path)
    width, height = image.size
    # print(width, height)

    """for x in range(342, 428):
        for y in range(339, 390):
            image.putpixel((x, y), white)
    
    for x in range(220, 550):
        for y in range(434, 455):
            image.putpixel((x, y), white)"""

    frontera = set()

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pixel = image.getpixel((x, y))
            if isWhite(pixel):
                count = 0
                for pos in neighbors((x,y)):
                    if not isWhite(image.getpixel(pos)):
                        frontera.add((x,y))
                        break

    while len(frontera) > 0:
        position = random.choice(list(frontera))
        frontera.remove(position)
        
        count = 0
        red, green, blue = 0, 0, 0

        for vei in neighbors(position):
            if vei[0] < 0 or vei[0] >= width:
                continue
            if vei[1] < 0 or vei[1] >= height:
                continue
            pixel = image.getpixel(vei)
            if isWhite(pixel):
                frontera.add(vei)
            else:
                count += 1
                red += pixel[0]
                green += pixel[1]
                blue += pixel[2]
        
        red = red // count
        green = green // count
        blue = blue // count

        image.putpixel(position, (red, green, blue))

    current_directory = os.getcwd()
    output_figure = current_directory + "result.PNG"
    image.save(output_figure)

current_directory = os.getcwd()
input_figure = current_directory + "figure.PNG"
remove_watermark(input_figure)
