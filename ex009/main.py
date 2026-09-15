# convolução

import numpy as np
import cv2

imagem = cv2.imread('../imagens/mimikyu.png')

imagemCinza = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = imagem[i][j].sum() / 3

kernel = np.array([
    [0, 0, 1, 1, 0],
    [1, 1, -10, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0]
])
matriz_final = np.zeros((imagemCinza.shape[0] - (kernel.shape[0] + 1), imagemCinza.shape[1] - (kernel.shape[1] + 1)))

for m in range(matriz_final.shape[0]):
    for n in range(matriz_final.shape[1]):
        resultado = 0
        for i in range(kernel.shape[0]):
            for j in range(kernel.shape[1]):

                mult = imagemCinza[i + m][j + n] * kernel[i][j]
                resultado += mult

        if resultado > 255:
            matriz_final[m][n] = 255
        elif resultado < 0:
            matriz_final[m][n] = 0
        else:
            matriz_final[m][n] = resultado

print(matriz_final)

cv2.imshow("Imagem original", imagemCinza)
cv2.imshow("Matriz final", matriz_final)
cv2.waitKey(0)
cv2.destroyAllWindows()