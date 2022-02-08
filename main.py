import pygame

from cenario import Cenario
from constantes import VERMELHO, PRETO, BRANCO
from fantasma import Fantasma
from pacman import Pacman

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont('arial', 24, True, False)

size = 600 // 30
pacman = Pacman(size)
blinky = Fantasma(VERMELHO, BRANCO, PRETO, size)
cenario = Cenario(size, pacman, fonte)

while True:
    # Calcular as regras
    pacman.calcular_regras()
    cenario.calcular_regras()

    # Pintar a tela
    screen.fill(PRETO)
    cenario.pintar(screen)
    blinky.pintar(screen)
    pacman.pintar(screen)
    pygame.display.update()
    pygame.time.delay(100)

    # Captura os eventos
    eventos = pygame.event.get()
    cenario.processar_eventos(eventos)
    pacman.processar_eventos(eventos)
