import pygame
from pygame import mixer
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random
varpause = False
pygame.init()
janela_largura = 1200
janela_altura = 675
janela = pygame.display.set_mode((janela_largura, janela_altura))
pause_img = pygame.image.load("menupausa.png")
def Fase1(state):
    while True :
        clouds_img = pygame.image.load("clouds.png")
        sky_img = pygame.image.load("sky.jpg")
        sea_img = pygame.image.load("sea.png")
        far_ground_img = pygame.image.load("far-grounds.png")
        janela2 = pygame.display.set_mode((janela_largura, janela_altura))
        janela2.blit(sky_img, (0, 0))
        janela2.blit(clouds_img, (0, -10))
        janela2.blit(sea_img, (0, 100))
        janela2.blit(far_ground_img, (0, 410))

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            mixer.music.unload()
            mixer.music.load("musicamenu.mp3")
            mixer.music.play(-1)
            mixer.music.set_volume(0.5)
            state = "Menu"
            return state

        if key[pygame.K_l]:
            varpause = True
            while varpause:
                janela3 = janela.blit(pause_img, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            mixer.music.pause()
                        if event.key == pygame.K_n:
                            mixer.music.unpause()
                        if event.key == pygame.K_ESCAPE:
                            mixer.music.unload()
                            mixer.music.load("musicamenu.mp3")
                            mixer.music.play(-1)
                            mixer.music.set_volume(0.5)
                            state = "Menu"
                            return state
                        if event.key == pygame.K_p:
                            varpause = False
                    pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

    # olhosvoadores_g.draw(janela)
    # olhosvoadores_g.update()
