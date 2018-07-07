# -*- coding: utf-8 -*-
# Filtro da média

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float
from scipy.ndimage import filters 


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
    mask_size = 3

	
# Faz a leitura da imagem
img_entrada_1 = misc.imread(entrada) 

# Converte os pixels em float, com valores entre 0 e 1
img_entrada_1 = img_as_float(img_entrada_1)

# Define a máscara
masc_25 = np.ones([mask_size, mask_size], dtype = float)
masc_25 = masc_25 / (mask_size * mask_size)

# Aplica a média
img_saida = filters.correlate(img_entrada_1, masc_25, mode = 'constant', cval = 0)

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)

# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_entrada_1, cmap='gray', interpolation='nearest')
plt.title('img_entrada_1.tif')
plt.subplot(222)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Plota as imagens de entrada e saída na tela
plt.show()
