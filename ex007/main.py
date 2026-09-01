import numpy as np
import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('../imagens/neve.jpg')


imagemCinza = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = imagem[i][j].sum() / 3


histograma = [0] * 256

for i in range(imagemCinza.shape[0]):
    for j in range(imagemCinza.shape[1]):
        histograma[imagemCinza[i][j]] += 1


totalPixels = imagemCinza.shape[0] * imagemCinza.shape[1]
histogramaNormalizado = [0] * 256

for i in range(256):
    histogramaNormalizado[i] = histograma[i] / totalPixels


cdf = [0] * 256
pixel = range(256)
cdf[0] = histogramaNormalizado[0]

for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histogramaNormalizado[i]

novaImagem = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(imagemCinza.shape[0]):
    for j in range(imagemCinza.shape[1]):
        novaImagem[i][j] = round(cdf[imagemCinza[i][j]] * 255)


histogramaEqualizado = [0] * 256

for i in range(novaImagem.shape[0]):
    for j in range(novaImagem.shape[1]):
        histogramaEqualizado[novaImagem[i][j]] += 1



cv2.imshow("Imagem original", imagemCinza)
cv2.imshow("Imagem equalizada", novaImagem)


plt.figure(figsize=(15, 8))

plt.subplot(2, 2, 1)
plt.bar(pixel, histograma, color="red")
plt.title("Histograma original")


plt.subplot(2, 2, 2)
plt.bar(pixel, histogramaNormalizado, color="blue")
plt.title("Histograma normalizado")

plt.subplot(2, 2, 3)
plt.bar(pixel, cdf, color="green")
plt.title("Histograma acumulado")

plt.subplot(2, 2, 4)
plt.bar(pixel, histogramaEqualizado, color="purple")
plt.title("Histograma imagem especificado")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
