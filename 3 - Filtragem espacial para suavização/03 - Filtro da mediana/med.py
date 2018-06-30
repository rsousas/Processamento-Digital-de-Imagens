# -*- coding: utf-8 -*-

import sys
from scipy import misc 
from skimage import img_as_float
from scipy.ndimage import filters 
import matplotlib.pyplot as plt

try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada.tif'
    
try:
    saida = sys.argv[2]
except IndexError:
    saida = 'img_saida.tif'  
    
try:
    mask_size = int(sys.argv[3])
except IndexError:
    mask_size = 3

# Carrega a imagem
img_entrada = misc.imread(entrada) 
img_entrada = img_as_float(img_entrada)

img_saida = filters.median_filter(img_entrada, size=mask_size, mode='constant', cval=0) 

# Salva a imagem processada
misc.imsave(saida, img_saida)

# Plota imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_entrada, cmap='gray', interpolation='nearest')
plt.title('img_entrada')
plt.subplot(222)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Mostra as figuras na tela
plt.show()