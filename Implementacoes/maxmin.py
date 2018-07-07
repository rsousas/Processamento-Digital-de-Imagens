# -*- coding: utf-8 -*-
# Filtro de máximo e mínimo

import sys
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import img_as_float
from scipy.ndimage import filters 


try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada_1.tif'
    
try:
    saida_1 = sys.argv[2]
except IndexError:
    saida_1 = 'img_saida_min.tif'  
    
try:
    saida_2 = sys.argv[3]
except IndexError:
    saida_2 = 'img_saida_max.tif'
	
try:
    mask_size = int(sys.argv[4])
except IndexError:
    mask_size = 3


# Faz a leitura da imagem
img_entrada = misc.imread(entrada) 

# Converte os pixels em float, com valores entre 0 e 1
img_entrada = img_as_float(img_entrada)

# Aplica o filtro de mínimo
img_saida_min = filters.minimum_filter(img_entrada, size = mask_size, mode = 'constant', cval = 0)

# Aplica o filtro de máximo
img_saida_max = filters.maximum_filter(img_entrada, size = mask_size, mode = 'constant')

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida_1, img_saida_min)
misc.imsave(saida_2, img_saida_max)

# Organiza o plote das imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_entrada, cmap='gray', interpolation='nearest'); 
plt.title('img_entrada')
plt.subplot(222); 
plt.imshow(img_saida_min, cmap='gray', interpolation='nearest')
plt.title('img_saida_min')
plt.subplot(223); 
plt.imshow(img_saida_max, cmap='gray', interpolation='nearest')
plt.title('img_saida_max')

# Plota as imagens de entrada e saída na tela
plt.show()
