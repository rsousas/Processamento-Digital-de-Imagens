# -*- coding: utf-8 -*-
# Efeitos da suavização da detecção de bordas

import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import misc
from scipy.ndimage import filters
from skimage import img_as_float


try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada_1.tif'
    
try:
    saida = sys.argv[2]
except IndexError:
    saida = 'img_saida.tif'  
    
try:
    mask_size = int(sys.argv[3])
except IndexError:
    mask_size = 5


# Faz a leitura da imagem
img_entrada = misc.imread(entrada) 

# Converte os pixels em float, com valores entre 0 e 1
img_entrada = img_as_float(img_entrada)

# Aplica o filtro da média
ave_masc = np.ones([mask_size, mask_size], dtype = float)
ave_masc = ave_masc / (mask_size * mask_size)
img_entrada = filters.correlate(img_entrada, ave_masc)

# Operadores de Sobel Horizontal
sob_h = np.array([[ -1., -2., -1.],
                 [  0.,  0.,  0.],
                 [  1.,  2.,  1.]], dtype = float)
				 
# Operadores de Sobel Vertical				 
sob_v = np.array([[ -1.,  0.,  1.],
                  [ -2.,  0.,  2.],
                  [ -1.,  0.,  1.]], dtype = float)

# Aplica Gradiente de Sobel
img_saida_h = filters.correlate(img_entrada, sob_h)
img_saida_v = filters.correlate(img_entrada, sob_v)

# Magnitude do gradiente
img_saida = np.sqrt(img_saida_h**2 + img_saida_v**2)

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
