# contornos destacados

import cv2
import numpy as np
import matplotlib.pyplot as plt

from utils import binarizar, gradienteMorfologico


imagemColorida = cv2.imread('../imagens/contorno.png')

imagem = cv2.cvtColor(imagemColorida, cv2.COLOR_BGR2GRAY)
imagem = binarizar(imagem, 150)

elemento = np.ones((3, 3), dtype=np.uint8)
contornos = gradienteMorfologico(imagem, elemento)
imagemResultado = imagemColorida.copy()

imagemResultado[contornos == 255] = [0, 0, 255]

cv2.imshow("Contornos destacados", imagemResultado)
cv2.waitKey(0)
cv2.destroyAllWindows()