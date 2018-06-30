# -*- coding: utf-8 -*-

import numpy as np
from scipy import misc
from skimage import img_as_float, filters
import matplotlib.pyplot as plt
import sys

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
img_entrada = img_as_float(img_entrada.astype(np.uint8))

# Limiar de Otsu
t_otsu = filters.threshold_otsu(img_entrada)

# Segmenta a imagem por limiarizacao
img_saida = img_entrada < t_otsu

# Salva a imagem processada
misc.imsave(saida, img_saida.astype(np.uint8))

# Plota imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_entrada, cmap='gray', interpolation='nearest'); 
plt.title('img_entrada')
plt.subplot(222); 
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')


# Mostra as figuras na tela
plt.show()