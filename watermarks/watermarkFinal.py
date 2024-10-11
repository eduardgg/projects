
import math
import os
from PIL import Image

current_directory = os.getcwd()
thumbnails_folder = current_directory + "Thumbnails"
photos_folder = current_directory + "Photos"
results_folder = current_directory + "Results"

white = (255, 255, 255)
black = (0, 0, 0)
blue = (47,44,125)
red = (204,21,39)

def neighbors(position):
    # Vigilar: aquest codi accepta posicions fora del rang, si "position" està a un costat de la imatge
    # Ho tenim en compte durant el codi, analitzant els pixels només de l'interior de la imatge.
    x = position[0]
    y = position[1]
    return [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]

def distancia_euclidiana(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2)

def colors_semblants(color1, color2, threshold):
    distancia = distancia_euclidiana(color1, color2)
    return distancia <= threshold

def isBad(image, pos):
    x, y = pos
    pixel = image.getpixel(pos)
    if not isGrey(pixel):
        return False
    if 176 >= y >= 130 and 126 >= x-y >= 105: 
        return True
    if 342 <= x <= 428 and 339 <= y <= 390:
        return True
    return False

def isWhite(pixel):
    if pixel[0] + pixel[1] + pixel[2] > 680:
        return True
    return False

def isBlack(pixel):
    if pixel[0] + pixel[1] + pixel[2] < 100:
        return True
    return False

def isGrey(pixel):
    if max(pixel) - min(pixel) < 1:
        return True
    return False

def isRed(pixel):
    # return 150 < pixel[0] < 255 and pixel[1] < 100 and pixel[2] < 100
    return colors_semblants(pixel, red, 10)

def isGreen(pixel):
    return 50 < pixel[1] < 150 and pixel[2] < 100 and pixel[0] < 100

def isBlue(pixel):
    # return 120 < pixel[2] < 200 and pixel[0] < 100 and pixel[1] < 100
    return colors_semblants(pixel, blue, 20)

def remove_watermark(path1, path2, file):
    image1 = Image.open(path1)
    image2 = Image.open(path2)
    
    width1, height1 = image1.size   # Original:   768 x 511
    width2, height2 = image2.size   # Thumbnail:  270 x 180
    ratioW = width1 / width2
    ratioH = height1 / height2

    minX, minY = 100, 1000
    maxX, maxY = 0, 0

    for x in range(1, width1 - 1):
        for y in range(1, height1 - 1):
            pos = (x, y)
            pixel = image1.getpixel(pos)
            if isRed(pixel) or isBlue(pixel):
                if x < minX:
                    minX = x
                if x > maxX:
                    maxX = x
                if y < minY:
                    minY = y
                if y > maxY:
                    maxY = y
            
            # Trobar el tros amb lletres:
            if isWhite(pixel) or isGrey(pixel):
                thumbPos = (round(x / ratioW) - 1, round(y / ratioH) - 1)
                thumbPixel = image2.getpixel(thumbPos)
                if width2 - thumbPixel[0] >= 45 or height2 - thumbPixel[1] >= 30:
                    image1.putpixel(pos, thumbPixel)


    for x in range(minX-1, maxX+3):
        for y in range(minY-1, maxY+2):
            pos = (x, y)
            pixel = image1.getpixel(pos)
            thumbPos = (round(x / ratioW)-1, round(y / ratioH)-1)
            thumbPixel = image2.getpixel(thumbPos)
            image1.putpixel(pos, thumbPixel)

    image1.save(os.path.join(results_folder, file))



for image in os.listdir(thumbnails_folder):
    path1 = os.path.join(photos_folder, image)
    path2 = os.path.join(thumbnails_folder, image)
    if os.path.exists(path1):
        print("Correcting photo: ", image)
        remove_watermark(path1, path2, image)
    else:
        print("There is no photo for this thumbnail: ", image)
