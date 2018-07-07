# -*- coding: utf-8 -*-
# Operações lógicas sobre imagens

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc 


try:
    entrada_1 = sys.argv[1]
except IndexError:
    entrada_1 = 'img_entrada_1.tif'

try:
    entrada_2 = sys.argv[2]
except IndexError:
    entrada_2 = 'img_entrada_2.tif'
    
try:
    saida = sys.argv[3]
except IndexError:
    saida = 'img_saida.tif'  


# Faz a leitura de duas imagens
img_entrada_1 = misc.imread(entrada_1)
img_entrada_2 = misc.imread(entrada_2)

# Faz a intersecção entre as imagens lidas
img_saida = img_entrada_1 != img_entrada_2

# Faz o salvamento da imagem de saída após o processamento
misc.imsave(saida, img_saida.astype(np.uint8)) 


#import numpy as np
#im.astype(bool)    im.astype(np.uint8)


# Organiza o plote das imagens
plt.figure()
plt.subplot(221)
plt.imshow(img_entrada_1, cmap='gray', interpolation='nearest')
plt.title('img_entrada_1')
plt.subplot(222)
plt.imshow(img_entrada_2, cmap='gray', interpolation='nearest')
plt.title('img_entrada_2')
plt.subplot(223)
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')

# Plota as imagens de entrada e saída na tela
plt.show()
