
import numpy as np
import cv2


def binarizar(imagem, limite=150):
    """Transforma a imagem em preto e branco."""
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
