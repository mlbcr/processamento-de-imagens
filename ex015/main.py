# hit or miss

import numpy as np
import cv2
import math

imagem = cv2.imread('../imagens/quadrados.png')

if imagem is None:
    print("Erro ao carregar a imagem")
    exit()

A, B, C = imagem.shape

matriz = np.array([
    255, 255, 255,
    255, 255, 255,
    255, 255, 255
])

tamanhoMatriz = int(math.sqrt(matriz.size))
iBorda = tamanhoMatriz // 2
borda = iBorda * 2

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
            novaImagem[i][j] = 255
        else:
            novaImagem[i][j] = 0

imagemErosao = np.zeros((A, B), dtype=np.uint8)

for i in range(iBorda, A + iBorda):
    for j in range(iBorda, B + iBorda):
        somatorio = 0
        index = 0

        for y in range(-iBorda, iBorda + 1):
            for x in range(-iBorda, iBorda + 1):
                if matriz[index] == 255 and novaImagem[i + x][j + y] == 255:
                    somatorio += 255
                index += 1

        if somatorio == np.sum(matriz):
            imagemErosao[i - iBorda][j - iBorda] = 255

imagemFinal = np.zeros((A, B), dtype=np.uint8)

for i in range(A):
    for j in range(B):
        if imagemErosao[i][j] == 255:
            imagemFinal[i][j] = 255

cv2.imshow("Erosao", imagemErosao)
cv2.imshow("Hit or Miss", imagemFinal)

cv2.waitKey(0)
cv2.destroyAllWindows()
