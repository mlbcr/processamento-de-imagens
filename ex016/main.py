import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

imagem = cv2.imread('../imagens/contorno.png')

imagem = imagem[:, :, 0]

matriz = np.array([
    255,  255,  255,
    255,  255,  255, 
    255,  255,  255
])

tamanhoMatriz = int(math.sqrt(matriz.size))
iBorda = tamanhoMatriz // 2
borda = iBorda * 2

A, B = imagem.shape 
destino = matriz.size

qtdConvolucoes = 1
novaImagem = np.zeros((A + borda, B + borda), dtype=np.uint8)

for i in range(A + borda):
    for j in range(B + borda):
        if i < iBorda or (i >= A + iBorda) or j < iBorda or (j >= B + iBorda):
            novaImagem[i][j] = 0
        else:
            novaImagem[i][j] = imagem[i - iBorda][j - iBorda]

for i in range(A + borda):
    for j in range(B + borda):
        if novaImagem[i][j] < 150:
            novaImagem[i][j] = 0  
        else:
            novaImagem[i][j] = 255

imagemErodida = np.zeros((A + borda, B + borda), dtype=np.uint8)

for i in range(iBorda, A + iBorda):
        for j in range(iBorda, B + iBorda):
            somatorio = 0
            index = 0
            
            for y in range(-iBorda, (iBorda + 1)):
                for x in range(-iBorda, (iBorda + 1)):
                    if novaImagem[i + x][j + y] == matriz[index]:
                        somatorio += 1
                    index += 1

            if somatorio == destino:
                imagemErodida[i - iBorda][j - iBorda] = 255
            else: imagemErodida[i - iBorda][j - iBorda] = 0


cv2.imshow("Imagem Final", imagemErodida)
cv2.waitKey(0)

imagemFinal = np.zeros((A + borda, B + borda), dtype=np.uint8)

for i in range(A + borda):
    for j in range(B + borda):
        valor = int(novaImagem[i][j]) - int(imagemErodida[i][j])
        
        if valor < 0:
            valor = 0

        imagemFinal[i][j] = valor

cv2.imshow("Imagem Final", imagemFinal)
cv2.waitKey(0)