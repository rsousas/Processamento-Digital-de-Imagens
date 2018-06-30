# -*- coding: utf-8 -*-

import numpy as np
from scipy import misc
from skimage import img_as_float
import matplotlib.pyplot as plt
import sys

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
    
    
def limiar_global_simples(img, T_ini=None, min_delta_T=None):

    if T_ini==None:
        # Nenhum valor inicial atribuido: Considerar intensidade média.
        T_ini = img.mean()

    if min_delta_T==None:
        # Se min_delta_T nao informado: 'min_delta_T' eh 1% da maior intensidade!
        min_delta_T = img.max() * 0.001

    # Inicializa T com T_ini.
    T = T_ini
    # Inicializa delta_T com Infinito.
    delta_T = np.inf

    # Iteracao
    while delta_T >= min_delta_T:
        # Segmenta a imagem usando T.
        g_bw = img > T
        # Calcula o numero de pixels de objeto e de fundo.
        num_px_bg, num_px_fg = np.bincount(g_bw.flatten())
        # Constroi imagem com os pixels de objeto.
        g_fg = img * g_bw
        # Constroi imagem com os pixels de fundo.
        g_bg = img * np.invert(g_bw)
        # Intensidade média - pixels de objeto
        fg_mean = g_fg.sum() / float( num_px_fg )
        # Intensidade média – pixels de fundo
        bg_mean = g_bg.sum() / float( num_px_bg )
        # Armazena valor atual de T.
        T_old = T
        # Calcula um novo limiar T.
        T = 0.5 * (fg_mean + bg_mean)
        # Calcula o novo valor de delta_T.
        delta_T = np.abs(T - T_old)
    return T


# Carrega a imagem.
img_entrada = misc.imread(entrada)
img_entrada = img_as_float(img_entrada.astype(np.uint8))
 
# Chama a funcao para calculo do limiar global iterativo
valor_T = limiar_global_simples(img_entrada, T_ini, min_delta_T)
 
# Segmenta a imagem com o limiar T.
img_saida = img_entrada > valor_T

# Salva a imagem processada
misc.imsave(saida, img_saida.astype(np.uint8))

# Plota imagens
plt.figure() 
plt.subplot(221); 
plt.imshow(img_entrada, cmap='gray', interpolation='nearest'); 
plt.title('img_entrada')
plt.subplot(222); 
plt.imshow(img_saida, cmap='gray', interpolation='nearest')
plt.title('img_saida')


# Mostra as figuras na tela
plt.show()