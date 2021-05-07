import pygame
from pygame import mixer
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random
#import menucontroles


pygame.init()
janela_largura = 1200
janela_altura = 675
janela = pygame.display.set_mode((janela_largura, janela_altura))
mixer.music.load("musicamenu.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.1)
jogar = pygame.image.load("jogar.png")
jogaron = pygame.image.load("jogaron.png")
controles = pygame.image.load("controles.png")
controleson = pygame.image.load("controleson.png")
creditos = pygame.image.load("creditos.png")
creditoson = pygame.image.load("creditoson.png")
sair = pygame.image.load("sair.png")
sairon = pygame.image.load("sairon.png")
clock = pygame.time.Clock()

def Menu(state):
    while True:
        fundo_menu_img = pygame.image.load("FundoMenuTeste.jpg")
        janela.blit(fundo_menu_img, (0, 0))
        janela.blit(jogar, (0, 350))
        janela.blit(controles, (0, 425))
        janela.blit(creditos, (0, 500))
        janela.blit(sair, (0, 575))
        mx = 0
        my = 0
        mouseposic = pygame.mouse.get_pos()
        if mouseposic[0] >= 0 and mouseposic[0] <= 300 and mouseposic[1] >= 350 and mouseposic[1] < 425:
            janela.blit(jogaron, (0, 350))
        if mouseposic[0] >= 0 and mouseposic[0] <= 300 and mouseposic[1] >= 425 and mouseposic[1] < 500:
            janela.blit(controleson, (0 ,425))
        if mouseposic[0] >= 0 and mouseposic[0] <= 300 and mouseposic[1] >= 500 and mouseposic[1] < 575 :
            janela.blit(creditoson, (0, 500))
        if mouseposic[0] >= 0 and mouseposic[0] <= 300 and mouseposic[1] >= 575 and mouseposic[1] < 650 :
            janela.blit(sairon, (0 , 575))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if mx >= 0 and mx <= 300 and my >= 350 and my < 425:
                    mixer.music.unload()
                    mixer.music.load("musicafase1.mp3")
                    mixer.music.play(-1)
                    mixer.music.set_volume(0.5)
                    state = "Historia"
                    pygame.display.update()
                    return state

                if mx >= 0 and mx<= 300 and my >= 425 and my < 500:
                    state = "menucontroles"
                    pygame.display.update()
                    return state

                if mx >= 0 and mx<= 300 and my >= 500 and my < 575:
                    state = "creditos"
                    pygame.display.update()
                    return state
                if mx >= 0 and mx<= 300 and my >= 575 and my < 650:
                    pygame.quit()
        clock.tick(60)
        pygame.display.update()
