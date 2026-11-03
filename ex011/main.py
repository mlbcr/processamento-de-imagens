# erosão
import cv2
import numpy as np

from utils import binarizar, erosao, dilatacao, gradienteMorfologico

imagem = cv2.imread(
    '../imagens/contorno.png',
    cv2.IMREAD_GRAYSCALE
)

imagem = binarizar(imagem)

elemento = np.ones((3, 3), dtype=np.uint8)

imagemErodida = erosao(imagem, elemento)
imagemDilatada = dilatacao(imagem, elemento)
imagemGradiente = gradienteMorfologico(imagem, elemento)

cv2.imshow("Original", imagem)
cv2.imshow("Erosao", imagemErodida)
cv2.imshow("Dilatacao", imagemDilatada)
cv2.imshow("Gradiente", imagemGradiente)

cv2.waitKey(0)
cv2.destroyAllWindows()