import cv2
import numpy as np

imagem = cv2.imread('../imagens/mimikyu.png')
print(imagem)

print(f"Largura em pixels: {imagem.shape[1]}")
print(f"Altura em pixels: {imagem.shape[0]}")
print(f"Canais: {imagem.shape[2]}")

cv2.imshow("Mimikyu", imagem)
cv2.waitKey(0)

cv2.imwrite("saida/mimikyu.png", imagem)

# canalBlue = np.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=np.uint8)
# canalGreen = np.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=np.uint8)
# canalRed = np.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=np.uint8)

canalBlue = np.zeros((imagem.shape[0], imagem.shape[1]), dtype=np.uint8)
canalGreen = np.zeros((imagem.shape[0], imagem.shape[1]), dtype=np.uint8)
canalRed = np.zeros((imagem.shape[0], imagem.shape[1]), dtype=np.uint8)


# canalBlue[:, :, 0] = imagem[:, :, 0]
# canalGreen[:, :, 1] = imagem[:, :, 1]
# canalRed[:, :, 2] = imagem[:, :, 2]

cv2.imshow("Canal Blue", canalBlue)
cv2.imshow("Canal Green", canalGreen)
cv2.imshow("Canal Red", canalRed)
cv2.waitKey(0)