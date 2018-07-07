# -*- coding: utf-8 -*-
# Limiarização utilizando o método de Otsu

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from skimage import img_as_float, filters


try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada_1.tif'
    
try:
    saida = sys.argv[2]
except IndexError:
    saida = 'img_saida.tif'  

    
# Faz a leitura da imagem
img_entrada = misc.imread(entrada)

# Converte os pixels em float, com valores entre 0 e 1
img_entrada = img_as_float(img_entrada.astype(np.uint8))

# Limiar de Otsu
l_otsu = filters.threshold_otsu(img_entrada)

# Segmenta a imagem por limiarização
img_saida = img_entrada < l_otsu

# Faz o salvamento das imagens de saída após o processamento
misc.imsave(saida, img_saida.astype(np.uint8))

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
