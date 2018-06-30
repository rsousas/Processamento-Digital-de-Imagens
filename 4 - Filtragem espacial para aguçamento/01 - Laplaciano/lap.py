# -*- coding: utf-8 -*-

import sys
import numpy as np
from scipy import misc
from scipy.ndimage import filters
from skimage import img_as_float
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
img_entrada = img_as_float(img_entrada)

# Aplica borramento sobre a imagem
im = filters.gaussian_filter(img_entrada, sigma=3)

# Laplaciano -4
lap = np.array([
 [  0.,  1.,  0.],
 [  1., -4.,  1.],
 [  0.,  1.,  0.]], dtype=float)

# Calcula os imagens filtradas pelas máscaras laplacianas.
img_saida = filters.correlate(im, lap )

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