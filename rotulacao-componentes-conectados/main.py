import cv2
import numpy

nomeImagem = 'imagem.jpg'
imagem = cv2.imread(nomeImagem)

cinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
pretoBranco = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)

imgComRotulos = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=int)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        cor = (imagem[i][j].sum()) // 3
        cinza[i][j] = cor
        if cor > 80:
            pretoBranco[i][j] = 255

rotuloAtual = 1

for i in range(1, pretoBranco.shape[0]):
    for j in range(1, pretoBranco.shape[1]):
        if pretoBranco[i][j] != 255:
            
            esquerda = imgComRotulos[i][j - 1]
            cima = imgComRotulos[i - 1][j]
            
            if esquerda != 0:
                imgComRotulos[i][j] = esquerda
                if cima != 0 and cima != esquerda:
                    for x in range(pretoBranco.shape[0]):
                        for y in range(pretoBranco.shape[1]):
                            if imgComRotulos[x][y] == cima:
                                imgComRotulos[x][y] = esquerda
            elif cima != 0:
                imgComRotulos[i][j] = cima
            else:
                imgComRotulos[i][j] = rotuloAtual
                rotuloAtual += 1

lista_contagem = []

imgExibicao = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)

for i in range(imgComRotulos.shape[0]):
    for j in range(imgComRotulos.shape[1]):
        valor_pixel = imgComRotulos[i][j]
        if valor_pixel != 0:
            if valor_pixel not in lista_contagem:
                lista_contagem.append(valor_pixel)
            imgExibicao[i][j] = (valor_pixel * 35) % 255
        else:
            imgExibicao[i][j] = 255

print("Componentes: " + str(len(lista_contagem)))

cv2.imshow("Preto e Branco", pretoBranco)
cv2.imshow("Componentes Rotulados", imgExibicao)
cv2.waitKey(0)
