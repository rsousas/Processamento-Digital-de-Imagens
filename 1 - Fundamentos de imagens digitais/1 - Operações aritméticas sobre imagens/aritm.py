# -*- coding: utf-8 -*-
# Operações aritméticas sobre imagens 

import sys
from scipy import misc
import matplotlib.pyplot as plt

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


# Carrega as imagens
img_entrada_1 = misc.imread(entrada_1)
img_entrada_2 = misc.imread(entrada_2)

# Subtrai as imagens
img_saida = img_entrada_1 - img_entrada_2

# Salva a imagem processada
misc.imsave(saida, img_saida)

# Plota imagens
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

# Mostra as figuras na tela
plt.show()
