# erosão

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

imagem = cv2.imread('../imagens/quadrados.png')
pixel = 256 * [0]
histograma = 256 * [0]

for i in range(256):
    pixel[i] = i

matriz = np.array([
    0, 255, 0,
    255, 255, 255,
    0, 255, 0

])

tamanhoMatriz = int(math.sqrt(matriz.size))
iBorda = tamanhoMatriz // 2
borda = iBorda * 2
destino = 0

for i in range (matriz.size):
    destino += matriz[i]

qtdConvolucoes = 1

cv2.imshow("Imagem Original", imagem)
cv2.waitKey(0)

A, B, C = imagem.shape # altura, largura e cor

novaImagem = np.zeros((A + borda, B + borda), dtype=np.uint8)

for i in range(A + borda):
    for j in range(B + borda):
        if i < iBorda or (i >= A + iBorda) or j < iBorda or (j >= B + iBorda):
            novaImagem[i][j] = 255  
        else:
            novaImagem[i][j] = (int(imagem[i - iBorda][j - iBorda].sum())) // 3 

plt.xlabel('Pixel')
plt.ylabel('Quantidade')

plt.title('Histograma da Imagem em Tons de Cinza')

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
            histograma[novaImagem[i][j]] += 1

plt.bar(pixel, histograma, color='black')
cv2.imshow("Imagem P&B", novaImagem)
plt.show()

for i in range(A + borda):
    for j in range(B + borda):
        if novaImagem[i][j] < 150:
            novaImagem[i][j] = 0  
        else:
            novaImagem[i][j] = 255

imagemFinal = np.zeros((A, B), dtype=np.uint8)

for q in range(qtdConvolucoes):
    for i in range(iBorda, A + iBorda):
        for j in range(iBorda, B + iBorda):
            somatorio = 0
            index = 0
            
            for y in range(-iBorda, (iBorda + 1)):
                for x in range(-iBorda, (iBorda + 1)):
                    if novaImagem[i + x][j + y] == matriz[index]:
                        somatorio += matriz[index]
                    index += 1

            if somatorio == destino:
                imagemFinal[i - iBorda][j - iBorda] = 255
            else: imagemFinal[i - iBorda][j - iBorda] = 0

cv2.imshow("Nova Imagem P&B", novaImagem)
cv2.imshow("Imagem Final", imagemFinal)
cv2.waitKey(0)
cv2.destroyAllWindows()