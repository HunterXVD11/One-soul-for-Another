import pygame, sys
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from pygame import mixer
import random

clock = pygame.time.Clock()
janela_largura = 1200
janela_altura = 675
janela = pygame.display.set_mode((janela_largura, janela_altura))
pygame.display.set_caption('One soul for another')
def Creditos(state):
    credito = pygame.image.load('creditosimg.png')
    credito_altura = 690
    while True:
        mx = 0
        my = 0
        janela.fill((0, 0, 0))
        janela.blit(credito, (150, credito_altura))
        if credito_altura > - 1250:
            credito_altura -= 2
        else:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx >= 750 and mx <= 1100 and my >= 570 and my <= 670:
                        state = "Menu"
                        return state
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        state = 'Menu'
                        return state

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
