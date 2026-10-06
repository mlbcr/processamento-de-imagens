#convolução
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

imagem = cv2.imread('../imagens/mimikyu.png')

matriz = np.array([
    0,  1, 0, 1, 0,
    0,  1, 0, 1, 0,
    0, 1, -10, 1, 0,
    0,  1, 0, 1, 0,
    0,  1, 0, 1, 0
])

tamanhoMatriz = int(math.sqrt(matriz.size))
iBorda = tamanhoMatriz // 2
borda = iBorda * 2

qtdConvolucoes = 2

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

imagemFinal = np.zeros((A, B), dtype=np.uint8)

for q in range(qtdConvolucoes):
    for i in range(iBorda, A + iBorda):
        for j in range(iBorda, B + iBorda):
            somatorio = 0
            index = 0
            
            for y in range(-iBorda, (iBorda + 1)):
                for x in range(-iBorda, (iBorda + 1)):
                    somatorio += int(novaImagem[i + x][j + y]) * matriz[index]
                    index += 1

            if somatorio < 0:
                somatorio = 0
            elif somatorio > 255:
                somatorio = 255

            imagemFinal[i - iBorda][j - iBorda] = somatorio

cv2.imshow("Imagem P&B", novaImagem)
cv2.imshow("Imagem Final", imagemFinal)
cv2.waitKey(0)
cv2.destroyAllWindows()