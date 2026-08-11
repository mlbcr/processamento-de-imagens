import numpy as np
import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('../imagens/bandeira-brasil.jpg')

pixel = [i for i in range(256)]
histograma = [0] * 256

novaImagem = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        novaImagem[i][j] = imagem[i][j].sum() / 3
        histograma[novaImagem[i][j]] += 1


cv2.imshow("Canal Cinza", novaImagem)

plt.figure()
plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da Bandeira do Brasil')
plt.bar(pixel, histograma, color='blue')
plt.show()


imagemMultinivel = np.zeros((imagem.shape[0], imagem.shape[1]), dtype=np.uint8)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        valor = novaImagem[i][j]

        if valor <= 70 or valor >= 90:
            imagemMultinivel[i][j] = 255

        else:
            imagemMultinivel[i][j] = novaImagem[i][j]
            


cv2.imshow("Imagem", imagemMultinivel)

cv2.waitKey(0)
cv2.destroyAllWindows()