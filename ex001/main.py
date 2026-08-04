import cv2
import numpy

imagem = cv2.imread('mimikyu.jpg')
print(imagem)

cv2.imshow("Mimikyu", imagem)
cv2.waitKey(0)

cv2.imwrite("saida-mimikyu.jpg", imagem)