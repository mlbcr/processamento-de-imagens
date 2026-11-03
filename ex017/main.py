# extração de componentes conectados

import cv2
import numpy as np
import matplotlib.pyplot as plt

from utils import binarizar, extrairComponenteConectado

imagem = cv2.imread('../imagens/contorno.png')

imagem = binarizar(imagem, 150)

elemento = np.ones((3, 3), dtype=np.uint8)

pontoInicial = (100, 150)

componente = extrairComponenteConectado(imagem, elemento, pontoInicial)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')

plt.subplot(1, 2, 2)
plt.imshow(componente, cmap='gray')
plt.title('Componente Conectado')

plt.show()