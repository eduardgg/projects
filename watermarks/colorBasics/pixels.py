from PIL import Image

def isWhite(pixel):
    if pixel[0] + pixel[1] + pixel[2] > 710:
        return True
    return False

def isBlack(pixel):
    if pixel[0] + pixel[1] + pixel[2] < 100:
        return True
    return False

def isGrey(pixel):
    if max(pixel) - min(pixel) < 3:
        return True
    return False

def modify():
    image = Image.new('RGB', (256, 256), color='white')
    # width, height = image.size

    for x in range(256):
        for y in range(256):
            image.putpixel((x, y), (x, y, 0))

    image.save(r"colorets.jpg")

modify()