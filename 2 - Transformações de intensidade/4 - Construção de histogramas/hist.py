# -*- coding: utf-8 -*-
# Construção de histogramas

import sys
import matplotlib.pyplot as plt
from scipy import misc 


try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada.tif'

saida = 'histograma.tif'  


# Faz a leitura da imagem
img_entrada = misc.imread(entrada) 

# Transforma os níveis de intensidade numa imagem de uma dimensão
histograma = img_entrada.flatten()	

# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.hist(histograma, bins=256, range=(0,255))
plt.title('histograma')
plt.savefig(saida)
plt.subplot(222)
plt.imshow(img_entrada, cmap='gray', interpolation='nearest')
plt.title('img_entrada')

# Plota as imagens de entrada e saída na tela
plt.show()
