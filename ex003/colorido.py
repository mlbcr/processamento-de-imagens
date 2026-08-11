import numpy as np
import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('../imagens/bandeira-brasil.jpg')

if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

histogramaB = [0] * 256
histogramaG = [0] * 256
histogramaR = [0] * 256

pixel = [i for i in range(256)]

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):

        b = int(imagem[i][j][0])
        g = int(imagem[i][j][1])
        r = int(imagem[i][j][2])

        histogramaB[b] += 1
        histogramaG[g] += 1
        histogramaR[r] += 1
plt.figure()
plt.plot(pixel, histogramaB, color='blue')
plt.plot(pixel, histogramaG, color='green')
plt.plot(pixel, histogramaR, color='red')

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma')
plt.show()


imagemMultinivel = np.zeros(
    (imagem.shape[0], imagem.shape[1], 3),
    dtype=np.uint8
)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):

        b = int(imagem[i][j][0])
        g = int(imagem[i][j][1])
        r = int(imagem[i][j][2])

        if g > r * 1.2 and g > b * 1.1:
            imagemMultinivel[i][j] = [0, 255, 0]

        elif b > r * 1.2 and b > g * 1.1:
            imagemMultinivel[i][j] = [255, 0, 0]

        elif r > 100 and g > 100 and b < 100:
            imagemMultinivel[i][j] = [0, 255, 255]

        elif r > 180 and g > 180 and b > 180:
            imagemMultinivel[i][j] = [255, 255, 255]

        else:
            imagemMultinivel[i][j] = [0, 0, 0]


cv2.imshow("Imagem", imagem)
cv2.imshow("Limiarizacao", imagemMultinivel)

cv2.waitKey(0)

