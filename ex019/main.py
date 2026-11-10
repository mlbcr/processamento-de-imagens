# filtro de media

import numpy as np
import cv2

imagem = cv2.imread('../imagens/mimikyu.png')

imagemCinza = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = imagem[i][j].sum() / 3

kernel = np.ones((3, 3), dtype=np.float32) / 9

novaImagem = np.zeros(
    (imagem.shape[0], imagem.shape[1]),
    dtype=np.uint8
)

for i in range(1, imagemCinza.shape[0] - 1):
    for j in range(1, imagemCinza.shape[1] - 1):
        regiao = imagemCinza[i-1:i+2, j-1:j+2]

        novaImagem[i][j] = np.sum(regiao * kernel)

cv2.imshow("Imagem filtrada", novaImagem)

cv2.waitKey(0)
cv2.destroyAllWindows()