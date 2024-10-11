from PIL import Image
import math


def HSVtoRGB(hsv):
    
    (H, S, V) = hsv
    # V és el valor (de 0 a 1). De fet, V = max(R,G,B)
    # H és el to: des de RGB, passant per CMY, fins a colors intermitjos.
    # S és la saturació (de 0 a 1).

    if H < 0 or H >= 360:
        print("H is not in the expected range: ", H, " not in [0, 360)")
        return
    if S < 0 or S > 1:
        print("S is not in the expected range: ", S, " not in [0, 1]")
    if V < 0 or V > 1:
        print("V is not in the expected range: ", V, " not in [0, 1]")

    # C -> Cromància, valor auxiliar
    C = V*S
    
    # m -> De fet, m = min(R,G,B), valor auxiliar
    m = V - C

    # X -> Un altre valor auxiliar
    X = V * S * (1 - math.fabs((H/60)%2 - 1))

    if H < 60:
        (R, G, B) = (C+m, X+m, m)
    elif H < 120:
        (R, G, B) = (X+m, C+m, m)
    elif H < 180:
        (R, G, B) = (m, C+m, X+m)
    elif H < 240:
        (R, G, B) = (m, X+m, C+m)
    elif H < 300:
        (R, G, B) = (X+m, m, C+m)
    else:
        (R, G, B) = (C+m, m, X+m)
    
    (R, G, B) = (int(round(255*R)), int(round(255*G)), int(round(255*B)))
    return (R, G, B)


def RGBtoHSV(rgb):
    (R, G, B) = rgb
    V = max(R, G, B)
    minim = min(R, G, B)
    if V == 0:
        S = 0
        H = 0
    else:
        S = 1 - minim/V
        if V == R:
            H = 60*(((G - B)/(V - minim)) % 6)
        if V == G:
            H = 60*(((B - R)/(V - minim)) + 2)
        if V == B:
            H = 60*(((R - G)/(V - minim)) + 4)
    return (H, S, V)


def paintCircle(value):
    image = Image.new('RGB', (201, 201), color='white')
    width, height = image.size
    V = value
    for x in range(width):
        for y in range(height):
            D = math.sqrt((x-100)**2 + (y-100)**2)
            if D <= 100:
                S = D/100
                if x == 100:
                    if y <= 100:
                        H = 90
                    else:
                        H = 270
                else:
                    H = math.degrees(math.atan((y-100)/(x-100)))
                    if x > 100:
                        H += 180
                    elif y > 100:
                        H += 360
                hsv = (H, S, V)
                rgb = HSVtoRGB(hsv)
                image.putpixel((x, y), rgb)
    image.save(r"cercleValor{}.jpg".format(value))


def paintProva():
    image = Image.new('RGB', (201, 201), color='white')
    width, height = image.size
    V = 1
    for x in range(width):
        for y in range(height):
            D = math.sqrt((x-100)**2 + (y-100)**2)
            if D <= 100:
                S = D/100
                if x == 100:
                    if y <= 100:
                        H = 90
                    else:
                        H = 270
                else:
                    H = math.degrees(math.atan((y-100)/(x-100)))
                    if x > 100:
                        H += 180
                    elif y > 100:
                        H += 360
                hsv = (H, S, V)
                (R, G, B) = HSVtoRGB(hsv)
                m = (R + G + B - 255) // 2
                image.putpixel((x, y), (m, m, m))
    image.save(r"cercleProva.jpg")

def paintQuadratProva(hsv):
    image = Image.new('RGB', (50, 50), color='white')
    width, height = image.size
    for i in range(height):
        for j in range(width):
            image.putpixel((i,j), HSVtoRGB(hsv))
    image.save(r"quadratProva.jpg")



paintQuadratProva((30, 1, 0.59))
paintProva()

for i in range(6):
    paintCircle(i/5)