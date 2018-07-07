# -*- coding: utf-8 -*-
# Laplaciano

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import filters
from skimage import img_as_float


try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada.tif'
    
try:
    saida = sys.argv[2]
except IndexError:
    saida = 'img_saida.tif'  


# Faz a leitura da imagem
img_entrada = misc.imread(entrada) 

# Converte os pixels em float, com valores entre 0 e 1
img_entrada = img_as_float(img_entrada)

# Aplica borramento sobre a imagem
img_blur = filters.gaussian_filter(img_entrada, sigma = 3)

# Laplaciano -4
lap_4 = np.array([[  0.,  1.,  0.],
                  [  1., -4.,  1.],
                  [  0.,  1.,  0.]], dtype = float)

# Calcula os imagens filtradas pelas máscaras laplacianas.
img_saida = filters.correlate(img_blur, lap_4)

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida)

# Organiza o plote das imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_entrada, cmap='gray', interpolation='nearest'); 
plt.title('img_entrada')
plt.subplot(222); 
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Plota as imagens de entrada e saída na tela
plt.show()
