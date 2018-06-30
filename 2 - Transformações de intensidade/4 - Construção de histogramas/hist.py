# -*- coding: utf-8 -*-

import sys
from scipy import misc 
import matplotlib.pyplot as plt

try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada.tif'

saida = 'histograma.tif'  


# Carrega a imagem
img_entrada = misc.imread(entrada) 

histograma = img_entrada.flatten()

plt.figure()

print(histograma)
# Plota imagens
plt.subplot(221)
plt.hist(histograma, bins=256, range=(0,255))
plt.title('histograma')
plt.savefig(saida)
plt.subplot(222)
plt.imshow(img_entrada, cmap='gray', interpolation='nearest')
plt.title('img_entrada')

# Mostra as figuras na tela
plt.show()