
import numpy as np
import cv2


def binarizar(imagem, limite=150):
    resultado = np.where(imagem >= limite, 255, 0)
    return resultado.astype(np.uint8)


def operacaoMorfologica(imagem, elemento, operacao):
    altura, largura = imagem.shape
    linhas, colunas = elemento.shape

    centroY = linhas // 2
    centroX = colunas // 2

    imagemBordas = np.pad(
        imagem,
        ((centroY, centroY), (centroX, centroX)),
        mode='constant',
        constant_values=0
    )

    resultado = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):

            pixels = []

            for y in range(linhas):
                for x in range(colunas):

                    if elemento[y][x] == 0:
                        continue

                    pixel = imagemBordas[i + y][j + x]
                    pixels.append(pixel)

            if operacao == "erosao":
                if all(pixel == 255 for pixel in pixels):
                    resultado[i][j] = 255

            elif operacao == "dilatacao":
                if any(pixel == 255 for pixel in pixels):
                    resultado[i][j] = 255

            else:
                raise ValueError("Operação inválida")

    return resultado


def erosao(imagem, elemento):
    return operacaoMorfologica(imagem, elemento, "erosao")


def dilatacao(imagem, elemento):
    return operacaoMorfologica(imagem, elemento, "dilatacao")


def gradienteMorfologico(imagem, elemento):
    imagemErodida = erosao(imagem, elemento)
    return cv2.subtract(imagem, imagemErodida)

def extrairComponenteConectado(imagem, elemento, pontoInicial):

    altura, largura = imagem.shape
    X = np.zeros((altura, largura), dtype=np.uint8)

    linha, coluna = pontoInicial

    X[linha][coluna] = 255

    while True:
        dilatada = dilatacao(X, elemento)
        novaImagem = cv2.bitwise_and(dilatada, imagem)

        if np.array_equal(novaImagem, X):
            break

        X = novaImagem

    return X

def esqueletizacao(imagem, elemento):
    altura, largura = imagem.shape

    imagemAtual = imagem.copy()
    esqueleto = np.zeros((altura, largura), dtype=np.uint8)

    while True:
        temPixel = False

        for i in range(altura):
            for j in range(largura):
                if imagemAtual[i][j] == 255:
                    temPixel = True
                    break
            if temPixel:
                break

        if not temPixel:
            break

        imagemErodida = erosao(imagemAtual, elemento)
        imagemAberta = dilatacao(imagemErodida, elemento)

        diferenca = np.zeros((altura, largura), dtype=np.uint8)

        for i in range(altura):
            for j in range(largura):
                if imagemAtual[i][j] == 255 and imagemAberta[i][j] == 0:
                    diferenca[i][j] = 255

        for i in range(altura):
            for j in range(largura):
                if diferenca[i][j] == 255:
                    esqueleto[i][j] = 255

        imagemAtual = imagemErodida

    return esqueleto