import numpy as np
import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('../imagens/mimikyu.png')

novaImagem = np.zeros((imagem.shape[0], imagem.shape[1]), dtype=np.uint8)
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        b = int(imagem[i][j][0])
        g = int(imagem[i][j][1])
        r = int(imagem[i][j][2])
        novaImagem[i][j] = (b + r + g) // 3

# cv2.imshow("Canal Blue", canalBlue)
# cv2.imshow("Canal Green", canalGreen)
# cv2.imshow("Canal Red", canalRed)

pixel = 256 * [0]
histograma = 256 * [0]
blue = 256 * [0]
green = 256 * [0]
red = 256 * [0]

for i in range(256):
    pixel[i] = i

plt.xlabel('Pixel')
plt.ylabel('Quantidade')

plt.title('Histograma da Imagem em Tons de Cinza')


for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
            histograma[novaImagem[i][j]] += 1
            blue[imagem[i][j][0]] += 1
            green[imagem[i][j][1]] += 1
            red[imagem[i][j][2]] += 1

plt.bar(pixel, histograma, color='black')
plt.bar(pixel, red, color='red')
plt.bar(pixel, blue, color='blue')
plt.bar(pixel, green, color='green')
plt.show()


cv2.imshow("Canal Cinza", novaImagem)
cv2.waitKey(0)

