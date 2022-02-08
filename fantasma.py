import pygame

from elementos_jogo import ElementosJogo


class Fantasma(ElementosJogo):
    def __init__(self, cor, tamanho):
        self.coluna = 6.0
        self.linha = 8.0
        self.tamanho = tamanho
        self.cor = cor

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho),
                    (px + fatia * 2, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho),
                    ]
        pygame.draw.polygon(tela, self.cor, contorno, 0)

    def calcular_regras(self):
        pass

    def processar_eventos(self, eventos):
        pass
