
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

histogramaNormalizado = [0] * 256

for i in range(256):
    totalPixels = imagemCinza.shape[0] * imagemCinza.shape[1]
    histogramaNormalizado[i] = histograma[i] / totalPixels

cdf = [0] * 256

cdf[0] = histogramaNormalizado[0]

for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histogramaNormalizado[i]

for i in range(imagemCinza.shape[0]):
    for j in range(imagemCinza.shape[1]):
        pixelAtual = imagemCinza[i][j]
        novaImagem[i][j] = int(cdf[pixelAtual] * 255)

cv2.imshow("Nova imagem", novaImagem)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(pixel, histograma, color="red")
plt.title("Histograma comum")

plt.subplot(1, 2, 2)
plt.bar(pixel, histogramaNormalizado, color="blue")
plt.title("Histograma normalizado")


plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
