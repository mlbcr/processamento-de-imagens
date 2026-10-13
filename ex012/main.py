# dilatação

import numpy as np
import cv2
import math

imagem = cv2.imread('../imagens/quadrados.png')

matriz = np.array([
    0, 255, 0,
    255, 255, 255,
    0, 255, 0
])

tamanhoMatriz = int(math.sqrt(matriz.size))
iBorda = tamanhoMatriz // 2
borda = iBorda * 2

A, B, C = imagem.shape

novaImagem = np.zeros((A + borda, B + borda), dtype=np.uint8)

for i in range(A + borda):
    for j in range(B + borda):
        if i < iBorda or i >= A + iBorda or j < iBorda or j >= B + iBorda:
            novaImagem[i][j] = 0
        else:
            novaImagem[i][j] = int(imagem[i - iBorda][j - iBorda].sum()) // 3

for i in range(A + borda):
    for j in range(B + borda):
        if novaImagem[i][j] < 150:
            novaImagem[i][j] = 0
        else:
            novaImagem[i][j] = 255

imagemFinal = np.zeros((A, B), dtype=np.uint8)

for i in range(iBorda, A + iBorda):
    for j in range(iBorda, B + iBorda):
        encontrou = False
        index = 0

        for y in range(-iBorda, iBorda + 1):
            for x in range(-iBorda, iBorda + 1):
                if matriz[index] == 255 and novaImagem[i + x][j + y] == 255:
                    encontrou = True
                index += 1

        if encontrou:
            imagemFinal[i - iBorda][j - iBorda] = 255
        else:
            imagemFinal[i - iBorda][j - iBorda] = 0

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem", novaImagem)
cv2.imshow("Dilatacao", imagemFinal)
cv2.waitKey(0)
cv2.destroyAllWindows()