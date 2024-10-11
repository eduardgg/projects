
# Fast Fourier Transform to compute efficiently the convolution of two polynomials:

from cmath import pi, sin, cos, exp

def FFT(a):
    m = len(a)
    if m == 1:
        return [a[0]]
    if m & (m-1):
        # m no és potència de 2
        l = m.bit_length()
        a += [0 for _ in range((1<<l)-m)]
        m = len(a)
    e = FFT([a[2*i] for i in range(m//2)])
    o = FFT([a[2*i+1] for i in range(m//2)])
    omega = exp(2j*pi/m)
    c1 = [(e[i] + (omega**i) * o[i]) for i in range(m//2)]
    c2 = [(e[i] - (omega**i) * o[i]) for i in range(m//2)]
    return c1+c2

def invFFT(f):
    m = len(f)
    v = FFT(f)
    c = [round(e.real)//m for e in v]
    c = [c[0]] + c[1:][::-1]
    while c[-1] == 0:
        c.pop()
    return c

def conv(a, b):
    m = 1 << ((len(a)+len(b)-1).bit_length())
    a += [0]*(m-len(a))
    b += [0]*(m-len(b))
    fa = FFT(a)
    fb = FFT(b)
    fc = [fa[i]*fb[i] for i in range(m)]
    c = invFFT(fc)
    return c



# Exemple senzill de càlcul de la FFT:
# (i comprovació que la inversa és correcta)
v = [1,2,3,4,5]
f = FFT(v)
i = invFFT(f)
print(v)
print(f)
print(i)
print(i == v)

# Convolució d'un polinomi amb ell mateix (P(z)^2)
print(conv(v, v))

# Convolució de dos polinomis diferents
w = [1,1,1,1,1,1,1]
print(conv(v, w))