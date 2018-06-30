# -*- coding: utf-8 -*-

import sys
from scipy import misc
from scipy import ndimage
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

im_blurred = ndimage.gaussian_filter(img_entrada, sigma=7)
im_mask = img_entrada - im_blurred
img_saida = im_blurred + (4.5 * im_mask)

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