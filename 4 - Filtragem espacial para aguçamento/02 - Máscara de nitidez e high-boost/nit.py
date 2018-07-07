# -*- coding: utf-8 -*-
# Máscara de nitidez e high-boost

import sys
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage


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

# Aplica o gaussiano, borrando a imagem
img_blurred = ndimage.gaussian_filter(img_entrada, sigma = 7)
img_mask = img_entrada - img_blurred
img_saida = img_blurred + (4.5 * img_mask)

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
