# dilatação
# erosão
import cv2
import numpy as np

from utils import binarizar, dilatacao

imagem = cv2.imread('../imagens/contorno.png')

imagemCinza = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = imagem[i][j].sum() / 3

imagem = binarizar(imagemCinza)

elemento = np.ones((3, 3), dtype=np.uint8)

imagemErodida = erosao(imagem, elemento)
imagemDilatada = dilatacao(imagem, elemento)
cv2.imshow("Original", imagem)
cv2.imshow("Erosao", imagemDilatada)

cv2.waitKey(0)
cv2.destroyAllWindows()