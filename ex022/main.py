import cv2
import numpy

imagem = cv2.imread('../imagens/mimikyu.png')

cinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
embaçado = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
mascara_detalhes = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
imagem_final = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        cinza[i][j] = imagem[i][j].sum() // 3

for i in range(1, cinza.shape[0] - 1):
    for j in range(1, cinza.shape[1] - 1):
        soma = 0
        for linha in range(-1, 2):
            for coluna in range(-1, 2):
                soma += int(cinza[i + linha][j + coluna])
        embaçado[i][j] = soma // 9

for i in range(cinza.shape[0]):
    for j in range(cinza.shape[1]):
        valor = int(cinza[i][j]) - int(embaçado[i][j])
        if valor < 0:
            mascara_detalhes[i][j] = 0
        else:
            mascara_detalhes[i][j] = valor

for i in range(cinza.shape[0]):
    for j in range(cinza.shape[1]):
        valor = int(cinza[i][j]) + 2 * int(mascara_detalhes[i][j])
        if valor > 255:
            imagem_final[i][j] = 255
        else:
            imagem_final[i][j] = valor

cv2.imshow("Original", cinza)
cv2.imshow("Embaçado", embaçado)
cv2.imshow("Mascara", mascara_detalhes)
cv2.imshow("Final Nitidez", imagem_final)
cv2.waitKey(0)
