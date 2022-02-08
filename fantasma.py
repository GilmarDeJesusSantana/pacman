import pygame

from elementos_jogo import ElementosJogo


class Fantasma(ElementosJogo):
    def __init__(self, cor, cor_externa, cor_interna, tamanho):
        self.coluna = 6.0
        self.linha = 8.0
        self.tamanho = tamanho
        self.cor = cor
        self.cor_extrana = cor_externa
        self.cor_interna = cor_interna

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

        olho_raio_externo = fatia
        olho_raio_interno = fatia // 2

        olho_esquerdo_x = int(px + fatia * 2.5)
        olho_esquerdo_y = int(py + fatia * 2.5)

        olho_direito_x = int(px + fatia * 5.5)
        olho_direito_y = int(py + fatia * 2.5)

        pygame.draw.circle(
            tela, self.cor_extrana,
            (olho_esquerdo_x,olho_esquerdo_y),
            olho_raio_externo, 0
        )

        pygame.draw.circle(
            tela, self.cor_interna,
            (olho_esquerdo_x,olho_esquerdo_y),
            olho_raio_interno, 0
        )

        pygame.draw.circle(
            tela, self.cor_extrana,
            (olho_direito_x, olho_direito_y),
            olho_raio_externo, 0
        )

        pygame.draw.circle(
            tela, self.cor_interna,
            (olho_direito_x,olho_direito_y),
            olho_raio_interno, 0
        )

    def calcular_regras(self):
        pass

    def processar_eventos(self, eventos):
        pass
