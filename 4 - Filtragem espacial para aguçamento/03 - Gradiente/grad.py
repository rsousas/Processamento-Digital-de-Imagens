# -*- coding: utf-8 -*-

import numpy as np
from scipy import misc
from scipy.ndimage import filters
from skimage import img_as_float
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
img_entrada = img_as_float(img_entrada)

# Operadores de Sobel Horizontal
sob_h = np.array([
 [-1., -2., -1.],
 [ 0.,  0.,  0.],
 [ 1.,  2.,  1.]], dtype=float)

# Gradiente de Sobel
img_saida = filters.correlate(img_entrada, sob_h)

# Salva a imagem processada
misc.imsave(saida, img_saida)

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