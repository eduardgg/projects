
import numpy as np

def fft_convolucio(x, y):

    # Troba la longitud òptima per l'FFT (longitud de la convolució)
    n = len(x) + len(y) - 1

    # Fem zero-padding a les seqüències per evitar aliasing (múltiples de 2 per eficàcia)
    N = 2**np.ceil(np.log2(n)).astype(int)
    
    # Apliquem FFT a les seqüències amb zero-padding fins a longitud N
    X_fft = np.fft.fft(x, N)
    Y_fft = np.fft.fft(y, N)
    
    # Multipliquem les dues FFT punt a punt
    Z_fft = X_fft * Y_fft
    
    # Apliquem la IFFT per tornar al domini temporal
    z = np.fft.ifft(Z_fft)
    
    # Ens quedem només amb els primers n elements, arrodonint i convertint a enters
    return np.round(np.real(z[:n])).astype(int)



# Exemples d'ús
cat = [1,1,2,5,14,42,132,429,1430,4862,16796]

# Crida a la funció de convolució
cat2 = list(fft_convolucio(cat, cat)[:10])
cat3 = list(fft_convolucio(cat2, cat)[:10])
cat4 = list(fft_convolucio(cat3, cat)[:10])

print(cat)
print(cat2)
print(cat3)
print(cat4)