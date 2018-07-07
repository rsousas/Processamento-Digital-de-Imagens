# -*- coding: utf-8 -*-
# Equalização de histogramas

import sys
import matplotlib.pyplot as plt
from scipy import misc 
from skimage import exposure


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

# Aplica a equalização do histograma e retorna a imagem
img_saida = exposure.equalize_hist(img_entrada) 

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
