# -*- coding: utf-8 -*-

import sys
from scipy import misc 
from skimage import exposure
import matplotlib.pyplot as plt

try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada.tif'
    
try:
    saida = sys.argv[2]
except IndexError:
    saida = 'img_saida.tif'  


# Carrega a imagem
img_entrada = misc.imread(entrada) 

# Aplica a equalização
img_saida = exposure.equalize_hist(img_entrada) 

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