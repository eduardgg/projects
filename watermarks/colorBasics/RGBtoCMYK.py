import sys

def conv_rgb_to_cmyk(r,g,b):
    M = max(r,g,b)
    if [r,g,b] == [0,0,0]:
        return (0,0,0,1)
    c = 1 - r/M
    m = 1 - g/M
    y = 1 - b/M
    k = 1 - M/255
    return (c,m,y,k)

r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])
(c,m,y,k) = conv_rgb_to_cmyk(r,g,b)

print("cyan    = " + str(c))
print("magenta = " + str(m))
print("yellow  = " + str(y))
print("black   = " + str(k))