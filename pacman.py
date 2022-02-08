import pygame

from constantes import AMARELO, PRETO, VELOCIDADE, PARAR
from elementos_jogo import ElementosJogo


class Pacman(ElementosJogo):
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def calcular_regras(self):
        self.coluna_intencao += self.velocidade_x
        self.linha_intencao += self.velocidade_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def pintar(self, tela):
        # Desenha o corpo do Pacman
        pygame.draw.circle(
            tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0
        )

        # Desenho da boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Olho do Pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def processar_eventos(self, eventos_key):
        for acoes in eventos_key:
            if acoes.type == pygame.KEYDOWN:
                if acoes.key == pygame.K_RIGHT:
                    self.velocidade_x = VELOCIDADE
                elif acoes.key == pygame.K_LEFT:
                    self.velocidade_x = -VELOCIDADE
                elif acoes.key == pygame.K_UP:
                    self.velocidade_y = -VELOCIDADE
                elif acoes.key == pygame.K_DOWN:
                    self.velocidade_y = VELOCIDADE

            elif acoes.type == pygame.KEYUP:
                if acoes.key == pygame.K_RIGHT:
                    self.velocidade_x = PARAR
                elif acoes.key == pygame.K_LEFT:
                    self.velocidade_x = PARAR
                elif acoes.key == pygame.K_UP:
                    self.velocidade_y = PARAR
                elif acoes.key == pygame.K_DOWN:
                    self.velocidade_y = PARAR

    def processar_eventos_mouse(self, eventos_mouse):
        delay = 100
        for ponteiro in eventos_mouse:
            if ponteiro.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = ponteiro.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay

    def aceitar_movimento(self):
        self.coluna = self.coluna_intencao
        self.linha = self.linha_intencao
