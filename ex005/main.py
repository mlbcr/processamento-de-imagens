# r2 = rmax, s1 = r1 = 0 e s2 = r2 = 255
# r = valor original (entrada)
# s = valor novo do pixel (saída)

import numpy as np
import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('../imagens/neve.jpg')

pixel = [i for i in range(256)]
histograma = [0] * 256

imagemCinza = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = imagem[i][j].sum() / 3
        histograma[imagemCinza[i][j]] += 1

cv2.imshow("Imagem original", imagemCinza)

novaImagem = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

# r1 = imagemCinza.min()
# r2 = imagemCinza.max()
r1 = 155
r2 = 237

histogramaNova = [0] * 256

print(f"Valor mínimo: {r1}")
print(f"Valor máximo: {r2}")

for i in range(imagemCinza.shape[0]):
    for j in range(imagemCinza.shape[1]):
        r = imagemCinza[i][j]

        # se r <= r1
        if r <= r1:
            s = 0

        # se r1 < r < r2
        elif r < r2:
            s = 255 * ((r - r1) / (r2 - r1))

        # se r >= r2
        else:
            s = 255

        novaImagem[i][j] = s
        histogramaNova[novaImagem[i][j]] += 1


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(pixel, histograma)
plt.title("Histograma original")

plt.subplot(1, 2, 2)
plt.bar(pixel, histogramaNova)
plt.title("Histograma 2")

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
