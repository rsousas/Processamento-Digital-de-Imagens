# -*- coding: utf-8 -*-

import sys
from scipy import misc 
from skimage import img_as_float
from scipy.ndimage import filters 

try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada.tif'
    
try:
    saida_1 = sys.argv[2]
except IndexError:
    saida_1 = 'img_saida_min.tif'  
    
try:
    saida_2 = sys.argv[3]
except IndexError:
    saida_2 = 'img_saida_max.tif'
	
try:
    parametro = int(sys.argv[4])
except IndexError:
    parametro = 3


	# Falta definir mask_size

# Carrega a imagem
img_entrada = misc.imread(entrada) 
img_entrada = img_as_float(img_entrada)

img_saida_min = filters.minimum_filter(img_entrada, size=parametro, mode='constant', cval=0)
img_saida_max = filters.maximum_filter(img_entrada, size=parametro, mode='constant')

# Salva as imagens processadas
misc.imsave(saida_1, img_saida_min)
misc.imsave(saida_2, img_saida_max)