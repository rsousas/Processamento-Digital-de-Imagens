# -*- coding: utf-8 -*-
#Limiarização iterativa

import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import misc
from skimage import img_as_float 

    
def limiar_global_simples(img_entrada, T_ini):
    
    # Consderar delta-T mínimo como 0.001
    min_delta_T = img_entrada.max() * 0.001
		
    # Inicializa T com T_ini
    T = T_ini
	
    # Inicializa delta_T com Infinito
    delta_T = np.inf

    # Iteração
    while delta_T >= min_delta_T:
        # Segmenta a imagem usando T
        g = img_entrada > T
        
		# Calcula o numero de pixels de objeto e de fundo
        num_px_back, num_px_front = np.bincount(g.flatten())
        
		# Constroi imagem com os pixels de objeto
        g_front = img_entrada * g
        
		# Constroi imagem com os pixels de fundo
        g_back = img_entrada * np.invert(g)
        
		# Intensidade média - pixels de objeto
        fg_mean = g_front.sum() / float(num_px_front)
        
		# Intensidade média – pixels de fundo
        bg_mean = g_back.sum() / float(num_px_back)
        
		# Armazena valor atual de T
        T_old = T
        
		# Calcula um novo limiar T
        T = 0.5 * (fg_mean + bg_mean)
        
		# Calcula o novo valor de delta_T
        delta_T = np.abs(T - T_old)
    return T 
	
	
try:
    entrada = sys.argv[1]
except IndexError:
    entrada = 'img_entrada.tif'
    
try:
    saida = sys.argv[2]
except IndexError:
    saida = 'img_saida.tif'  
    
try:
    T_ini = sys.argv[3]
except IndexError:
    T_ini = 0.5  
	
	
T_ini = float(T_ini)

# Faz a leitura da imagem
img_entrada = misc.imread(entrada)

# Converte os pixels em float, com valores entre 0 e 1
img_entrada = img_as_float(img_entrada.astype(np.uint8))
 
# Chama a função para cálculo do limiar global iterativo
valor_T = limiar_global_simples(img_entrada, T_ini)
 
# Segmenta a imagem com o limiar T
img_saida = img_entrada > valor_T
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
