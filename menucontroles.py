import pygame
from pygame import mixer
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

clock = pygame.time.Clock()
pygame.init()
janela_largura = 1200
janela_altura = 675
janela = pygame.display.set_mode((janela_largura, janela_altura))

def menucontroles(state):
    controlesimg = pygame.image.load("menutempcontroles.png")
    janela.blit(controlesimg, (0, 0))
    setinha = pygame.image.load("setinha.png")
    setinhaon = pygame.image.load("setinhaon.png")

    while True:
        print("clock.tick:", clock.tick())
        print("clock.get_fps", clock.get_fps())
        clock.tick(60)
        pygame.display.update()
        mouseposic = pygame.mouse.get_pos()
        janela.blit(setinha ,(1040, 0))
        if mouseposic[0] >= 1085 and mouseposic[0] <= 1200 and mouseposic[1] >= 0 and mouseposic[1] < 75:
            janela.blit(setinhaon, (1040, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "Menu"
                    return state
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= 1085 and mx <= 1200 and my >= 0 and my <= 75:
                    state = "Menu"
                    return state