
# És molt més recomenable llegir el programa oficial "complex.py"
# Conté més informació i maneres diferents (i més completes) d'implementar-ho.

import sys
import math
import stdio

class Complex:

    def __init__(self, x, y):
        self._a = x
        self._b = y
    
    def magnitude(self):
        return math.sqrt(self._a * self._a + self._b * self._b)

    def real_part(self):
        return self._a

    def imaginary_part(self):
        return self._b

    def conjugate(self):
        x = self._a
        y = - self._b
        c = Complex(x,y)
        return c

    def __str__(self):
        result = str(self._a)
        if self._b > 0:
            return result + ' + ' + str(self._b) + ' i'
        if self._b < 0:
            return result + ' - ' + str(abs(self._b)) + ' i'
        return result      

def addition(z,w):
    x = z._a + w._a
    y = z._b + w._b
    c = Complex(x, y)
    return c

def multiplication(z,w):
    x = z._a * w._a - z._b * w._b
    y = z._a * w._b + z._b * w._a
    c = Complex(x, y)
    return c

def division (z,w):
    c = multiplication(z,w.conjugate())
    c._a = c._a / (w._a ** w._a + w._b ** w._b)
    c._b = c._b / (w._a ** w._a + w._b ** w._b)
    return c

def main():
    c1 = Complex(float(sys.argv[1]), float(sys.argv[2]))
    c2 = Complex(float(sys.argv[3]), float(sys.argv[4]))
    p = division(c1,c2)
    stdio.writeln(p)
    stdio.writeln(p.magnitude())

if __name__ == '__main__':
    main()