# -*- coding: utf-8 -*-
# Filtro da mediana

import sys
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float
from scipy.ndimage import filters 


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

	
# Faz a leitura da imagem
img_entrada = misc.imread(entrada)

# Converte os pixels em float, com valores entre 0 e 1
img_entrada = img_as_float(img_entrada)

# Aplica a mediana
img_saida = filters.median_filter(img_entrada, size = mask_size, mode = 'constant', cval = 0) 

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida)

# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_entrada, cmap='gray', interpolation='nearest')
plt.title('img_entrada')
plt.subplot(222)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Plota as imagens de entrada e saída na tela
plt.show()
