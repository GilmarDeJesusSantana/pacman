import pygame

from cenario import Cenario
from constantes import VERMELHO, PRETO, BRANCO, CIANO, LARANJA, ROSA
from fantasma import Fantasma
from pacman import Pacman

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont('arial', 24, True, False)

size = 600 // 30
pacman = Pacman(size)
blinky = Fantasma(VERMELHO, BRANCO, PRETO, size)
inky = Fantasma(CIANO, BRANCO, PRETO, size)
clyde = Fantasma(LARANJA, BRANCO, PRETO, size)
pinky = Fantasma(ROSA, BRANCO, PRETO, size)
cenario = Cenario(size, pacman, fonte)
cenario.adicionar_movivel(pacman)
cenario.adicionar_movivel(blinky)
cenario.adicionar_movivel(clyde)
cenario.adicionar_movivel(inky)
cenario.adicionar_movivel(pinky)

while True:
    # Calcular as regras
    pacman.calcular_regras()
    blinky.calcular_regras()
    inky.calcular_regras()
    clyde.calcular_regras()
    pinky.calcular_regras()
    cenario.calcular_regras()

    # Pintar a tela
    screen.fill(PRETO)
    cenario.pintar(screen)
    blinky.pintar(screen)
    inky.pintar(screen)
    clyde.pintar(screen)
    pinky.pintar(screen)
    pacman.pintar(screen)
    pygame.display.update()
    pygame.time.delay(100)

    # Captura os eventos
    eventos = pygame.event.get()
    cenario.processar_eventos(eventos)
    pacman.processar_eventos(eventos)
