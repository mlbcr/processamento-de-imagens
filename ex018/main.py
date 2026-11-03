# esqueletização

import cv2
import numpy as np
import matplotlib.pyplot as plt
from utils import binarizar, esqueletizacao

imagem = cv2.imread('../imagens/letra.png')

altura, largura, canais = imagem.shape

imagemCinza = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = imagem[i][j].sum() / 3


imagem = binarizar(imagemCinza, 150)

for i in range(altura):
    for j in range(largura):

        if imagem[i][j] == 255:
            imagem[i][j] = 0
        else:
            imagem[i][j] = 255

elemento = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
], dtype=np.uint8)

esqueleto = esqueletizacao(imagem, elemento)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(esqueleto, cmap='gray')
plt.title('Esqueleto')
plt.axis('off')

plt.show()