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
def Historia(state):
    pergaminho = pygame.image.load('Pergaminho.png')
    press_enter = pygame.image.load('Press_enter.png')
    pergaminho_altura = 690

    mixer.music.load("musicapergaminho.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(1)

    while True:
        janela.fill((0, 0, 0))
        janela.blit(pergaminho, (150, pergaminho_altura))
        if pergaminho_altura > - 1000:
            pergaminho_altura -= 2
        else:
            janela.blit(press_enter,(225, 450))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        state = 'Fase1'
                        return state

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()