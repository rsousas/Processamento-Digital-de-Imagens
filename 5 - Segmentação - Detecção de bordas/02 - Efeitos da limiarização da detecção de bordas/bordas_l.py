# -*- coding: utf-8 -*-

import numpy as np
from scipy import misc
from scipy.ndimage import filters
from scipy import ndimage as ndi
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
    
try:
    mask_size = int(sys.argv[3])
except IndexError:
    mask_size = 3
	


# Carrega a imagem
img_entrada = misc.imread(entrada) 
img_entrada = img_as_float(img_entrada)

# Aplica o filtro da média
masc = np.ones([mask_size,mask_size], dtype=float)
masc = masc / (mask_size*mask_size)
img_entrada = filters.correlate(img_entrada, masc)

# Laplaciano 4
lap_4 = np.array([[ 0.,  1., 0.],
                  [ 1., -4., 1.],
                  [ 0.,  1., 0.]], dtype=float)
lap_8 = np.array([[-1., -1., -1.],
                  [-1.,  8., -1.],
                  [-1., -1., -1.]], dtype=float)
    
    
# Calcula os imagens filtradas pelas máscaras laplacianas.
im_m0_l4 = ndi.convolve(img_entrada, lap_4 )
im_m0_l8 = ndi.convolve(img_entrada, lap_8 )

# Corrige intensidades negativas.
im_m0_l4_ = np.abs( im_m0_l4 )
im_m0_l8_ = np.abs( im_m0_l8 )

# Limiarização do Laplaciano
perc = 0.2 # Porcentagem da intensidade maxima.
im_m0_l4_t = im_m0_l4_ >= im_m0_l4_.max() * perc
im_m0_l8_t = im_m0_l8_ >= im_m0_l8_.max() * perc

img_saida = im_m0_l8_t
	
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