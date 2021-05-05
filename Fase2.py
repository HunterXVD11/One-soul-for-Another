import pygame, sys
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from pygame import mixer
import random
import move

def Fase2(state):
    pygame.init()

    fonte = pygame.font.Font('freesansbold.ttf', 45)
    clock = pygame.time.Clock()
    janela_largura = 1200
    janela_altura = 675
    janela = pygame.display.set_mode((janela_largura, janela_altura))
    pygame.display.set_caption('One soul for another')

    player_rect = pygame.Rect(1000, 400, 87, 100)
    cenario = pygame.image.load("FundoFase2.jpg")
    cenario = pygame.transform.scale(cenario,(1200, 675))
    tile_tamanho = 50

    #Musica
    mixer.music.load("somcaverna.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)

    # Sons
    Sompulo = pygame.mixer.Sound("jump.mp3")
    Somespada = pygame.mixer.Sound("espadada2.mp3")
    Somdano = pygame.mixer.Sound("Kaorimorrendo.mp3")
    Sominimigo = pygame.mixer.Sound("goblin.mp3")
    Sommorte = pygame.mixer.Sound("mortesound.mp3")

    #Load Images

    frase_portao = pygame.image.load('Corra_portao.png')
    frase_portao = pygame.transform.scale(frase_portao,(600, 102))

    pause_img = pygame.image.load("pauseimg.png")

    #Parte Grama
    morte_mapa = pygame.image.load("parede.png")
    parede = pygame.image.load("parede.png")
    monstro_rect = pygame.image.load("parede.png")
    monstro_rect = pygame.transform.scale(monstro_rect,(110,80))
    arvore = pygame.image.load("Arvore.png")
    arvore = pygame.transform.scale(arvore,(300, 262))
    chao_padrao_img = pygame.image.load("chão padrão.png")
    chaosupmeio = pygame.image.load("Fase2_Tiles/chaosupmeio.png")
    chaosupdireita = pygame.image.load("Fase2_Tiles/chaosupdireita.png")
    chaosupesquerda = pygame.image.load("Fase2_Tiles/chaosupesquerda.png")
    chaomeiomeio = pygame.image.load("Fase2_Tiles/chaomeiomeio.jpg")
    chaomeiodireita = pygame.image.load("Fase2_Tiles/chaomeiodireita.png")
    chaomeioesquerda = pygame.image.load("Fase2_Tiles/chaomeioesquerda.png")
    chaoinferiormeio = pygame.image.load("Fase2_Tiles/chaoinferiormeio.png")
    chaoinferiordireita = pygame.image.load("Fase2_Tiles/chaoinferiordireita.png")
    chaoinferioresquerda = pygame.image.load("Fase2_Tiles/chaoinferioresquerda.png")

    #Parte Caverna
    fundo_caverna_img = pygame.image.load('fundo_caverna.jpg')
    fundo_caverna2_img = pygame.image.load('fundo_caverna2.png')
    fundo_caverna3_img = pygame.image.load('fundo_caverna3.png')
    fundo_caverna4_img = pygame.image.load('fundo_caverna4.png')
    fundo_caverna5_img = pygame.image.load('fundocaverna5.png')
    fundo_caverna6_img = pygame.image.load('fundocaverna6.png')

    tetocaverna1 = pygame.image.load("tetocaverna1.png")
    tetocaverna2 = pygame.image.load("tetocaverna2.png")
    tetocaverna3 = pygame.image.load("tetocaverna3.png")
    tetocaverna4 = pygame.image.load("tetocaverna4.png")
    tetocaverna5 = pygame.image.load("tetocaverna5.jpg")
    tetocaverna6 = pygame.image.load("tetocaverna6.png")

    contador_monstro = pygame.image.load("contador_monstros.png")
    contador_monstro = pygame.transform.scale(contador_monstro, (95, 52))

    portao = pygame.image.load("Portao_fechado.png")
    portao = pygame.transform.scale(portao, (125, 157))

    vitoria = pygame.image.load("WIN.png")
    vitoria = pygame.transform.scale(vitoria, (500, 387))

    alma_monstro = pygame.image.load('alma_monstro.png')
    alma_monstro = pygame.transform.scale(alma_monstro, (50, 77))
    somrodando = True
    musicarodando = True
    movimento_direita = False
    movimento_esquerda = False
    monstro_flip = False
    bater = False
    tomar_hit = False
    tela_gameover = False
    bater_monstro0 = False
    bater_monstro1 = False
    bater_monstro2 = False
    bater_monstro3 = False
    bater_monstro4 = False
    bater_monstro5 = False
    bater_monstro6 = False
    monstro_death_0 = False
    monstro_death_1 = False
    monstro_death_2 = False
    monstro_death_3 = False
    monstro_death_4 = False
    monstro_death_5 = False
    monstro_death_6 = False
    movimento_vertical = 0
    tempo_no_ar = 0
    direction = 1
    vidas = 5
    listavida = []
    x = 100
    movimento_monstro0 = 0
    movimento_monstro1 = 0
    movimento_monstro2 = 0
    movimento_monstro3 = 0
    movimento_monstro4 = 0
    movimento_monstro5 = 0
    movimento_monstro6 = 0
    contador = 0
    contador_hit = 100
    num_monstros = 0
    num_monstros_mortos = 0
    contadormonstro0 = 0
    contadormonstro1 = 0
    contadormonstro2 = 0
    contadormonstro3 = 0
    contadormonstro4 = 0
    contadormonstro5 = 0
    contadormonstro6 = 0
    contadormonstromorte0 = 0
    contadormonstromorte1 = 0
    contadormonstromorte2 = 0
    contadormonstromorte3 = 0
    contadormonstromorte4 = 0
    contadormonstromorte5 = 0
    contadormonstromorte6 = 0
    true_scroll = [0,0]
    game_over = False
    contador_restart = 0
    contador0 = 0
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    contador6 = 0
    contadorM0 = 0
    contadorM1 = 0
    contadorM2 = 0
    contadorM3 = 0
    contadorM4 = 0
    contadorM5 = 0
    contadorM6 = 0
    contadorhit_player = 0
    contadorbater_monstro = 0
    morreu0 = False
    morreu1 = False
    morreu2 = False
    morreu3 = False
    morreu4 = False
    morreu5 = False
    morreu6 = False
    contadordisparo_slime1 = True
    contadordisparo_slime2 = True
    contadordisparo_slime3 = True
    contadordisparo_slime4 = True
    movimentotiro = 0
    movimentotiro1 = 0
    movimentotiro2 = 0

    contadortiro = 0
    contadortiro2 = 0
    contadortiro3 = 0
    contadortiro4 = 0
    contadoresq1 = 0
    tiroesq1 = False
    tiroesq2 = False
    tiroesq3 = False

    for i in range(5):
        vida = pygame.image.load('Vida.png')
        listavida.append(vida)


    world_data =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,4,],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,9,],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,0,0,0,0,4,2,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,9,],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,0,0,0,0,4,2,2,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,2,2,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,7,],
                 [0,0,0,0,0,0,0,0,2,2,2,2,2,5,5,6,0,0,0,0,0,9,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,9,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,9,2,2,1,1,1,3,0,0,4,1,1,3,0,0,4,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,3,0,0,0,7,2,2,2,2,2,8,0,0,9,2,2,8,0,0,9,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,5,1,1,3,0,4,1,3,0,4,1,3,0,4,1,3,0,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,8,0,0,0,0,7,2,2,2,2,8,0,0,9,2,2,8,0,0,9,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,5,6,0,7,5,6,0,7,5,6,0,7,5,6,0,7,5,6,0,7,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,1,0,0,0,0,7,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,2,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,1,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,2,2,2,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,7,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],]

    global animation_frames
    animation_frames = {}

    def load_animations (path,frame_duration):
        global animation_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (87, 100))
            animation_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def load_animationsmorte (path,frame_duration):
        global animation_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (125, 100))
            animation_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def chance_action(action_var, frame, new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var,frame
    animation_database = {}

    animation_database['correndo'] = load_animations('Player_animations/Kaoricorrendo',[4,4,4,4,4,4,4,4])
    animation_database['parada'] = load_animations('Player_animations/Kaoriparada',[2,2,2,2,2,2,2,2,2,2,2])
    animation_database['pulando'] = load_animations('Player_animations/Kaoripulando',[7,7,7])
    animation_database['caindo'] = load_animations('Player_animations/Kaoricaindo',[7,7,7])
    animation_database['atacando'] = load_animations('Player_animations/Kaoriatacando',[2,2,2,2,2,2,2])
    animation_database['morrendo'] = load_animationsmorte('Player_animations/Kaorimorrendo', [4,4,4,4,4,4,4,4,4,4,300])
    animation_database['hit'] = load_animations('Player_animations/Kaorihit', [4,4,4,4])

    player_action = 'idle'
    player_frame = 0
    player_flip = True

    global animation_olho_frames
    animation_olho_frames = {}
    global animation_esqueleto_frames
    animation_esqueleto_frames = {}


    def load_animations_monstro (path,frame_duration):
        global animation_olho_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (120, 100))
            animation_olho_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def load_animations_esqueleto (path,frame_duration):
        global animation_esqueleto_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (110, 101))
            animation_esqueleto_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data


    global animation_slime_frames
    animation_slime_frames = {}
    global animation_espada_frames
    animation_espada_frames = {}

    def load_animations_slime_tiro(path, frame_duration):
        global animation_slime_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (19, 63))
            animation_slime_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def load_animations_esqueleto_tiro(path, frame_duration):
        global animation_espada_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (40, 40))
            animation_espada_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def chance_action_monstro(action_var, frame, new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var,frame

    animation_morcego_database = {}
    animation_slimeT_database = {}
    animation_esqueleto_database = {}
    animation_espada_database = {}

    animation_morcego_database['parado'] = load_animations_monstro('Slime_Animations/Slimeparado', [4, 4, 4, 4])
    animation_morcego_database['morrendo'] = load_animations_monstro('Slime_Animations/Slimemorrendo', [4, 4, 4, 300])
    animation_morcego_database['atacando'] = load_animations_monstro('Slime_Animations/Slimecuspindo',[2, 2, 2, 2, 2, ])
    animation_slimeT_database['tiro'] = load_animations_slime_tiro('Disparos_animations/SlimeT',[2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    animation_esqueleto_database['parado'] = load_animations_esqueleto('Esqueleto_animations/Esqueletoparado',[2,2,2,2])
    animation_esqueleto_database['morrendo'] = load_animations_esqueleto('Esqueleto_animations/Esqueletomorrendo',[9,9,9,9])
    animation_esqueleto_database['atacando'] = load_animations_esqueleto('Esqueleto_animations/Esqueletoatacando',[4,4,4,4,4,4])
    animation_espada_database['atacando'] = load_animations_esqueleto_tiro('Disparos_animations/Espada',[2,2,2])

    espada_action = 'atacando'
    espada_frame = 0

    esqueleto_action1 = 'parado'
    esqueleto_frame1 = 0

    esqueleto_action2 = 'parado'
    esqueleto_frame2 = 0

    esqueleto_action3 = 'parado'
    esqueleto_frame3 = 0

    tiro_action = 'tiro'
    tiro_frame = 0

    monstro_flip = True

    monstro_action0 = 'parado'
    monstro_frame0 = 0

    monstro_action1 = 'parado'
    monstro_frame1 = 0

    monstro_action2 = 'parado'
    monstro_frame2 = 0

    monstro_action3 = 'parado'
    monstro_frame3 = 0

    monstro_action4 = 'correndo'
    monstro_frame4 = 0

    monstro_action5 = 'correndo'
    monstro_frame5 = 0

    monstro_action6 = 'correndo'
    monstro_frame6 = 0

    while True:
        clock.tick(60)
        print("clock.tick:", clock.tick())
        print("clock.get_fps", clock.get_fps())
        print(player_rect.x)
        print(player_rect.y)
        true_scroll[0] += (player_rect.x - true_scroll[0] - 600) / 10
        true_scroll[1] += (player_rect.y - true_scroll[1] - 335) / 10
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        janela.blit(cenario,(0,0))

        tile_rects = []
        morte_rects = []

        y=0
        for linha in world_data:
            x=0
            for tile in linha:
                if tile == 1:
                    chaosupmeio = pygame.transform.scale(chaosupmeio, (tile_tamanho, tile_tamanho))
                    janela.blit(chaosupmeio, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 2:
                    chaomeiomeio = pygame.transform.scale(chaomeiomeio, (tile_tamanho, tile_tamanho))
                    janela.blit(chaomeiomeio, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 3:
                    chaosupdireita = pygame.transform.scale(chaosupdireita, (tile_tamanho, tile_tamanho))
                    janela.blit(chaosupdireita, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 4:
                    chaosupesquerda = pygame.transform.scale(chaosupesquerda, (tile_tamanho, tile_tamanho))
                    janela.blit(chaosupesquerda, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 5:
                    chaoinferiormeio = pygame.transform.scale(chaoinferiormeio, (tile_tamanho, tile_tamanho))
                    janela.blit(chaoinferiormeio, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 6:
                    chaoinferiordireita = pygame.transform.scale(chaoinferiordireita, (tile_tamanho, tile_tamanho))
                    janela.blit(chaoinferiordireita, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 7:
                    chaoinferioresquerda = pygame.transform.scale(chaoinferioresquerda, (tile_tamanho, tile_tamanho))
                    janela.blit(chaoinferioresquerda, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 8:
                    chaomeiodireita = pygame.transform.scale(chaomeiodireita, (tile_tamanho, tile_tamanho))
                    janela.blit(chaomeiodireita, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 9:
                    chaomeioesquerda = pygame.transform.scale(chaomeioesquerda, (tile_tamanho, tile_tamanho))
                    janela.blit(chaomeioesquerda, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 24:
                    parede = pygame.transform.scale(parede,(tile_tamanho, tile_tamanho))
                    janela.blit(parede, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 25:
                    morte_mapa = pygame.transform.scale(morte_mapa,(tile_tamanho, tile_tamanho))
                    janela.blit(morte_mapa, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    morte_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))

                #Parte Caverna
                if tile == 12:
                    fundo_caverna_img = pygame.transform.scale(fundo_caverna_img, (tile_tamanho, tile_tamanho))
                    janela.blit(fundo_caverna_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                if tile == 13:
                    tetocaverna1 = pygame.transform.scale(tetocaverna1, (tile_tamanho, tile_tamanho))
                    janela.blit(tetocaverna1, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 14:
                    tetocaverna2 = pygame.transform.scale(tetocaverna2, (tile_tamanho, tile_tamanho))
                    janela.blit(tetocaverna2, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 15:
                    tetocaverna3 = pygame.transform.scale(tetocaverna3, (tile_tamanho, tile_tamanho))
                    janela.blit(tetocaverna3, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 16:
                    tetocaverna4 = pygame.transform.scale(tetocaverna4, (tile_tamanho, tile_tamanho))
                    janela.blit(tetocaverna4, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 17:
                    tetocaverna5 = pygame.transform.scale(tetocaverna5, (tile_tamanho, tile_tamanho))
                    janela.blit(tetocaverna5, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 18:
                    tetocaverna6 = pygame.transform.scale(tetocaverna6, (tile_tamanho, tile_tamanho))
                    janela.blit(tetocaverna6, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 19:
                    fundo_caverna2_img = pygame.transform.scale(fundo_caverna2_img, (tile_tamanho, tile_tamanho))
                    janela.blit(fundo_caverna2_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                if tile == 20:
                    fundo_caverna3_img = pygame.transform.scale(fundo_caverna3_img, (tile_tamanho, tile_tamanho))
                    janela.blit(fundo_caverna3_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                if tile == 21:
                    fundo_caverna4_img = pygame.transform.scale(fundo_caverna4_img, (tile_tamanho, tile_tamanho))
                    janela.blit(fundo_caverna4_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                if tile == 22:
                    fundo_caverna5_img = pygame.transform.scale(fundo_caverna5_img, (tile_tamanho, tile_tamanho))
                    janela.blit(fundo_caverna5_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                if tile == 23:
                    fundo_caverna6_img = pygame.transform.scale(fundo_caverna6_img, (tile_tamanho, tile_tamanho))
                    janela.blit(fundo_caverna6_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                x+=1
            y+= 1

        #Desenha Vidas
        x = 20
        for vida in listavida:
            janela.blit(vida,(x, 25))
            x += 20

        #Desenha numero de Monstros a serem derrotados
        janela.blit(contador_monstro, (145, 20))
        texto = fonte.render(str(num_monstros_mortos) + " / " + str(num_monstros),True, (0, 0, 0))
        janela.blit(texto, (225, 27))

        bater_time = [0,0]
        movimento_player = [0,0]
        if movimento_direita:
            movimento_player[0] += 10
            direction = 1
        if movimento_esquerda:
            movimento_player[0] -= 10
            direction = 0
        movimento_player[1] += movimento_vertical
        movimento_vertical += 0.4
        if movimento_vertical > 6:
            movimento_vertical = 6
        if bater:
            if direction == 1:
                bater_time[0] = 100
            if direction == 0:
                bater_time[0] = -100
        if game_over == False:
            if bater_time[0] > 0 and tomar_hit == False:
                player_action, player_frame = chance_action(player_action, player_frame, 'atacando')
                player_flip = False
                bater_time[0] -= 1
            if bater_time[0] < 0 and tomar_hit == False:
                player_action, player_frame = chance_action(player_action, player_frame, 'atacando')
                player_flip = True
                bater_time[0] += 1
            if movimento_player[0] > 0 and bater == False and tomar_hit == False:
                player_action,player_frame = chance_action(player_action,player_frame,'correndo')
                player_flip = False
            if movimento_player[0] == 0 and bater == False and tomar_hit == False:
                player_action, player_frame = chance_action(player_action, player_frame, 'parada')
            if movimento_player[0] < 0 and bater == False and tomar_hit == False:
                player_action,player_frame = chance_action(player_action,player_frame,'correndo')
                player_flip = True
            if tempo_no_ar > 40 and bater == False and tomar_hit == False:
                player_action,player_frame = chance_action(player_action,player_frame,'caindo')
            if 3 < tempo_no_ar <= 40 and bater == False and tomar_hit == False:
                player_action,player_frame = chance_action(player_action,player_frame,'pulando')
            if tomar_hit == True:
                player_action, player_frame = chance_action(player_action, player_frame, 'hit')
                contadorhit_player += 1
                if contadorhit_player >= 10:
                    contadorhit_player = 0
                    tomar_hit = False
        else:
            player_action, player_frame = chance_action(player_action, player_frame, 'morrendo')
            movimento_player[0] = 0
        player_rect, collisions = move.move(player_rect, movimento_player, tile_rects)

        if collisions['bottom'] == True:
            movimento_vertical = 0
            tempo_no_ar = 0
        else:
            tempo_no_ar += 1

        if collisions['top'] == True:
            movimento_vertical = 0

        player_frame += 1
        if player_frame >= len(animation_database[player_action]):
            player_frame = 0
        player_image_id = animation_database[player_action][player_frame]
        player_image = animation_frames[player_image_id]

        janela.blit(portao, (9513 - scroll[0], 350 - scroll[1]))
        janela.blit(pygame.transform.flip(player_image, player_flip, False),(player_rect.x - scroll[0], player_rect.y - scroll[1]))

        monstro_frame0 += 1
        if monstro_frame0 >= len(animation_morcego_database[monstro_action0]):
            monstro_frame0 = 0
        monstro_image_id0 = animation_morcego_database[monstro_action0][monstro_frame0]
        monstro0 = animation_olho_frames[monstro_image_id0]

        monstro_frame1 += 1
        if monstro_frame1 >= len(animation_morcego_database[monstro_action1]):
            monstro_frame1 = 0
        monstro_image_id1 = animation_morcego_database[monstro_action1][monstro_frame1]
        monstro1 = animation_olho_frames[monstro_image_id1]

        monstro_frame2 += 1
        if monstro_frame2 >= len(animation_morcego_database[monstro_action2]):
            monstro_frame2 = 0
        monstro_image_id2 = animation_morcego_database[monstro_action2][monstro_frame2]
        monstro2 = animation_olho_frames[monstro_image_id2]

        monstro_frame3 += 1
        if monstro_frame3 >= len(animation_morcego_database[monstro_action3]):
            monstro_frame3 = 0
        monstro_image_id3 = animation_morcego_database[monstro_action3][monstro_frame3]
        monstro3 = animation_olho_frames[monstro_image_id3]

        '''monstro_frame4 += 1
        if monstro_frame4 >= len(animation_olho_database[monstro_action4]):
            monstro_frame4 = 0
        monstro_image_id4 = animation_olho_database[monstro_action4][monstro_frame4]
        monstro4 = animation_olho_frames[monstro_image_id4]

        monstro_frame5 += 1
        if monstro_frame5 >= len(animation_olho_database[monstro_action5]):
            monstro_frame5 = 0
        monstro_image_id5 = animation_olho_database[monstro_action5][monstro_frame5]
        monstro5 = animation_olho_frames[monstro_image_id5]

        monstro_frame6 += 1
        if monstro_frame6 >= len(animation_olho_database[monstro_action6]):
            monstro_frame6 = 0
        monstro_image_id = animation_olho_database[monstro_action6][monstro_frame6]
        monstro6 = animation_olho_frames[monstro_image_id]'''

        tiro_frame += 1
        if tiro_frame >= len(animation_slimeT_database[tiro_action]):
            tiro_frame = 0
        tiro_image_id = animation_slimeT_database[tiro_action][tiro_frame]
        tiro = animation_slime_frames[tiro_image_id]

        esqueleto_frame1 += 1
        if esqueleto_frame1 >= len(animation_esqueleto_database[esqueleto_action1]):
            esqueleto_frame1 = 0
        esqueleto_image_id1 = animation_esqueleto_database[esqueleto_action1][esqueleto_frame1]
        esqueleto1 = animation_esqueleto_frames[esqueleto_image_id1]

        esqueleto_frame2 += 1
        if esqueleto_frame2 >= len(animation_esqueleto_database[esqueleto_action2]):
            esqueleto_frame2 = 0
        esqueleto_image_id2 = animation_esqueleto_database[esqueleto_action2][esqueleto_frame2]
        esqueleto2 = animation_esqueleto_frames[esqueleto_image_id2]

        esqueleto_frame3 += 1
        if esqueleto_frame3 >= len(animation_esqueleto_database[esqueleto_action3]):
            esqueleto_frame3 = 0
        esqueleto_image_id3 = animation_esqueleto_database[esqueleto_action3][esqueleto_frame3]
        esqueleto3 = animation_esqueleto_frames[esqueleto_image_id3]

        espada_frame += 1
        if espada_frame >= len(animation_espada_database[espada_action]):
            espada_frame = 0
        espada_image_id = animation_espada_database[espada_action][espada_frame]
        espada = animation_espada_frames[espada_image_id]

        contador_hit += 1
        #Ataque e perda de vida do Monstro 0
        if monstro_death_0 == False:
            if contadormonstro0 != 1:
                num_monstros += 1
                contadormonstro0 = 1
            if contador0 == 0 and bater_monstro0 == False:
                monstro_action0, monstro_frame0 = chance_action_monstro(monstro_action0, monstro_frame0, 'parado')
            if contadordisparo_slime1 == True:
                movimentotiro += 3
                janela.blit(tiro, (4065 - scroll[0], 1660 + movimentotiro - scroll[1] - 15))
                tiro_rect = tiro.get_rect()
                tiro_rect.x = 4065
                tiro_rect.y = 1660 + movimentotiro
                contadortiro += 1
                if player_rect.colliderect(tiro_rect) and contador_hit >= 20 and len(listavida) > 0:
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
                if contadortiro >= 100:
                    movimentotiro = 0
                    contadordisparo_slime1 = False
            if contadordisparo_slime1 == False:
                movimentotiro = 0
                contadortiro = 0
                contadortiro2 += 1
                if contadortiro2 >= 320:
                    contadordisparo_slime1 = True

            janela.blit(pygame.transform.flip(monstro0, monstro_flip, False), (4028 - scroll[0], 1575 - scroll[1] - 15))
            monstro_rect0 = monstro_rect.get_rect()
            monstro_rect0.x = 4038
            monstro_rect0.y = 1550
            if player_rect.colliderect(monstro_rect0) and contador_hit >= 100 and bater == False and game_over == False and morreu0 == False:
                bater_monstro0 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(
                    monstro_rect0) and contador_hit >= 100 and bater == True and bater_monstro0 == False:
                contador0 = 1
                morreu0 = True
                monstro_action0, monstro_frame0 = chance_action_monstro(monstro_action0, monstro_frame0, 'morrendo')

                if contadormonstromorte0 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte0 = 1
            if morreu0 == True:
                contadorM0 += 1
                if contadorM0 == 8:
                    if somrodando == True:
                        Sominimigo.play()
                if contadorM0 >= 30:
                    monstro_death_0 = True

            if bater_monstro0 == True:
                monstro_action0, monstro_frame0 = chance_action_monstro(monstro_action0, monstro_frame0, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro0 = False
        #Ataque e perda de vida do Monstro 1
        if monstro_death_1 == False:
            if contadormonstro1 != 1:
                num_monstros += 1
                contadormonstro1 = 1
            if contador1 == 0 and bater_monstro1 == False:
                monstro_action1, monstro_frame1 = chance_action_monstro(monstro_action1, monstro_frame1, 'parado')
            if contadordisparo_slime2 == True:
                movimentotiro += 3
                janela.blit(tiro, (3865 - scroll[0], 1660 + movimentotiro - scroll[1] - 15))
                tiro_rect = tiro.get_rect()
                tiro_rect.x = 3865
                tiro_rect.y = 1660 + movimentotiro
                contadortiro += 1
                if player_rect.colliderect(tiro_rect) and contador_hit >= 20 and len(listavida) > 0:
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
                if contadortiro >= 100:
                    movimentotiro = 0
                    contadordisparo_slime2 = False
            if contadordisparo_slime2 == False:
                movimentotiro = 0
                contadortiro = 0
                contadortiro += 1
                if contadortiro >= 320:
                    contadordisparo_slime2 = True

            janela.blit(pygame.transform.flip(monstro1, monstro_flip, False), (3830 - scroll[0], 1575 - scroll[1] - 15))
            monstro_rect1 = monstro_rect.get_rect()
            monstro_rect1.x = 3840
            monstro_rect1.y = 1575
            if player_rect.colliderect(
                    monstro_rect1) and contador_hit >= 100 and bater == False and game_over == False and morreu1 == False:
                bater_monstro1 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(
                    monstro_rect1) and contador_hit >= 100 and bater == True and bater_monstro1 == False:
                contador1 = 1
                morreu1 = True
                monstro_action1, monstro_frame1 = chance_action_monstro(monstro_action1, monstro_frame1, 'morrendo')
                if contadormonstromorte1 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte1 = 1
            if morreu1 == True:
                contadorM1 += 1
                if contadorM1 == 8:
                    if somrodando == True:
                        Sominimigo.play()
                if contadorM1 >= 30:
                    monstro_death_1 = True
            if bater_monstro1 == True:
                monstro_action1, monstro_frame1 = chance_action_monstro(monstro_action1, monstro_frame1, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro1 = False
        # Ataque e perda de vida do Monstro 2
        if monstro_death_2 == False:
            if contadormonstro2 != 1:
                num_monstros += 1
                contadormonstro2 = 1
            if contador2 == 0 and bater_monstro2 == False:
                monstro_action2, monstro_frame2 = chance_action_monstro(monstro_action2, monstro_frame2, 'parado')
            if contadordisparo_slime3 == True:
                movimentotiro += 3
                janela.blit(tiro, (3665 - scroll[0], 1660 + movimentotiro - scroll[1] - 15))
                tiro_rect = tiro.get_rect()
                tiro_rect.x = 3665
                tiro_rect.y = 1660 + movimentotiro
                contadortiro += 1
                if player_rect.colliderect(tiro_rect) and contador_hit >= 20 and len(listavida) > 0:
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
                if contadortiro >= 100:
                    movimentotiro = 0
                    contadordisparo_slime3 = False
            if contadordisparo_slime3 == False:
                movimentotiro = 0
                contadortiro = 0
                contadortiro2 += 1
                if contadortiro2 >= 320:
                    contadordisparo_slime3 = True

            janela.blit(pygame.transform.flip(monstro2, monstro_flip, False), (3630 - scroll[0], 1575 - scroll[1] - 15))
            monstro_rect2 = monstro_rect.get_rect()
            monstro_rect2.x = 3640
            monstro_rect2.y = 1575
            if player_rect.colliderect(
                    monstro_rect2) and contador_hit >= 100 and bater == False and game_over == False and morreu2 == False:
                bater_monstro2 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(
                    monstro_rect2) and contador_hit >= 100 and bater == True and bater_monstro2 == False:
                contador2 = 1
                morreu2 = True
                monstro_action2, monstro_frame2 = chance_action_monstro(monstro_action2, monstro_frame2, 'morrendo')
                if contadormonstromorte2 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte2 = 1
            if morreu2 == True:
                contadorM2 += 1
                if contadorM2 == 8:
                    if somrodando == True:
                        Sominimigo.play()
                if contadorM2 >= 30:
                    monstro_death_2 = True
            if bater_monstro2 == True:
                monstro_action2, monstro_frame2 = chance_action_monstro(monstro_action2, monstro_frame2, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro2 = False
        # Ataque e perda de vida do Monstro 3
        if monstro_death_3 == False:
            if contadormonstro3 != 1:
                num_monstros += 1
                contadormonstro3 = 1
            if contador3 == 0 and bater_monstro3 == False:
                monstro_action3, monstro_frame3 = chance_action_monstro(monstro_action3, monstro_frame3, 'parado')

            if contadordisparo_slime1 == True and morreu3 == False:
                movimentotiro += 3
                janela.blit(tiro, (3455 - scroll[0], 1660 + movimentotiro - scroll[1] - 15))
                tiro_rect = tiro.get_rect()
                tiro_rect.x = 3455
                tiro_rect.y = 1660 + movimentotiro
                contadortiro += 1
                if player_rect.colliderect(tiro_rect) and contador_hit >= 20 and len(listavida) > 0:
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
                if contadortiro >= 100:
                    movimentotiro = 0
                    contadordisparo_slime4 = False
            if contadordisparo_slime4 == False:
                movimentotiro = 0
                contadortiro = 0
                contadortiro2 += 1
                if contadortiro2 >= 100:
                    contadordisparo_slime4 = True
                    contadortiro2 = 0
            janela.blit(pygame.transform.flip(monstro3, monstro_flip, False), (3420 - scroll[0], 1575 - scroll[1] - 15))
            monstro_rect3 = monstro_rect.get_rect()
            monstro_rect3.x = 3430
            monstro_rect3.y = 1575
            if player_rect.colliderect(monstro_rect3) and contador_hit >= 100 and bater == False and game_over == False and morreu3 == False:
                bater_monstro3 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(
                    monstro_rect3) and contador_hit >= 100 and bater == True and bater_monstro3 == False:
                contador3 = 1
                morreu3 = True
                monstro_action3, monstro_frame3 = chance_action_monstro(monstro_action3, monstro_frame3, 'morrendo')
                if contadormonstromorte3 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte3 = 1
            if morreu3 == True:
                contadorM3 += 1
                if contadorM3 == 8:
                    if somrodando == True:
                        Sominimigo.play()
                if contadorM3 >= 30:
                    monstro_death_3 = True
            if bater_monstro3 == True:
                monstro_action3, monstro_frame3 = chance_action_monstro(monstro_action3, monstro_frame3, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro3 = False

        contadoresq1 += 1
        # Ataque e perda de vida do Monstro 4
        if monstro_death_4 == False:
            if contadormonstro4 != 1:
                num_monstros += 1
                contadormonstro4 = 1
            if contador4 == 0 and bater_monstro4 == False and contadoresq1 <= 100:
                esqueleto_action1, esqueleto_frame1 = chance_action_monstro(esqueleto_action1, esqueleto_frame1, 'parado')
            if contador4 == 0 and bater_monstro4 == False and contadoresq1 > 100:
                esqueleto_action1, esqueleto_frame1 = chance_action_monstro(esqueleto_action1, esqueleto_frame1,'atacando')
                tiroesq1 = True
            if contador4 == 0 and bater_monstro4 == False and contadoresq1 > 113:
                contadoresq1 = 0
            if tiroesq1 == True and morreu4 == False:
                movimentotiro += 3
                janela.blit(espada, (650 + movimentotiro - scroll[0], 1565 - scroll[1] - 15))
                tiro_rect1 = espada.get_rect()
                tiro_rect1.x = 650 + movimentotiro
                tiro_rect1.y = 1565
                contadortiro += 1
                if player_rect.colliderect(tiro_rect1) and contador_hit >= 20 and len(listavida) > 0:
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
                if contadortiro >= 100:
                    movimentotiro = 0
                    tiroesq1 = False
            if tiroesq1 == False:
                movimentotiro = 0
                contadortiro = 0
            janela.blit(esqueleto1, (650 - scroll[0], 1565 - scroll[1] - 15))
            monstro_rect4 = monstro_rect.get_rect()
            monstro_rect4.x = 650
            monstro_rect4.y = 1565

            if player_rect.colliderect(monstro_rect4) and contador_hit >= 100 and bater == False and game_over == False and morreu4 == False:
                bater_monstro4 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect4) and contador_hit >= 100 and bater == True and bater_monstro4 == False:
                contador4 = 1
                morreu4 = True
                esqueleto_action1, esqueleto_frame1 = chance_action_monstro(esqueleto_action1, esqueleto_frame1, 'morrendo')
                if contadormonstromorte4 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte4 = 1
            if morreu4 == True:
                contadorM4 += 1
                if contadorM4 == 8:
                    if somrodando == True:
                        Sominimigo.play()
                if contadorM4 >= 30:
                    monstro_death_4 = True
            if bater_monstro4 == True:
                esqueleto_action1, esqueleto_frame1 = chance_action_monstro(esqueleto_action1, esqueleto_frame2, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro4 = False

        # Ataque e perda de vida do Monstro 5
        if monstro_death_5 == False:
            if contadormonstro5 != 1:
                num_monstros += 1
                contadormonstro5 = 1
            if contador5 == 0 and bater_monstro5 == False and contadoresq1 <= 100:
                esqueleto_action2, esqueleto_frame2 = chance_action_monstro(esqueleto_action2, esqueleto_frame2,'parado')
            if contador5 == 0 and bater_monstro5 == False and contadoresq1 > 100:
                esqueleto_action2, esqueleto_frame2 = chance_action_monstro(esqueleto_action2, esqueleto_frame2,'atacando')
                tiroesq2 = True
            if contador5 == 0 and bater_monstro5 == False and contadoresq1 > 113:
                contadoresq1 = 0
            if tiroesq2 == True and morreu5 == False:
                movimentotiro1 += 20
                janela.blit(espada, (650 + movimentotiro1 - scroll[0], 1865 - scroll[1] - 15))
                tiro_rect2 = espada.get_rect()
                tiro_rect2.x = 650 + movimentotiro1
                tiro_rect2.y = 1865
                contadortiro3 += 1
                if player_rect.colliderect(tiro_rect2) and contador_hit >= 20 and len(listavida) > 0:
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
                if contadortiro3 >= 100:
                    movimentotiro1 = 0
                    tiroesq2 = False
            if tiroesq2 == False:
                movimentotiro1 = 0
                contadortiro3 = 0

            janela.blit(esqueleto2, (650 - scroll[0], 1865 - scroll[1] - 15))
            monstro_rect5 = monstro_rect.get_rect()
            monstro_rect5.x = 650
            monstro_rect5.y = 1865

            if player_rect.colliderect(monstro_rect5) and contador_hit >= 100 and bater == False and game_over == False and morreu5 == False:
                bater_monstro5 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect5) and contador_hit >= 100 and bater == True and bater_monstro5 == False:
                contador5 = 1
                morreu5 = True
                esqueleto_action2, esqueleto_frame2 = chance_action_monstro(esqueleto_action2, esqueleto_frame2, 'morrendo')
                if contadormonstromorte5 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte5 = 1
            if morreu5 == True:
                contadorM5 += 1
                if contadorM5 == 8:
                    if somrodando == True:
                        Sominimigo.play()
                if contadorM5 >= 30:
                    monstro_death_5 = True
            if bater_monstro5 == True:
                esqueleto_action2, esqueleto_frame2 = chance_action_monstro(esqueleto_action2, esqueleto_frame2, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro5 = False

        # Ataque e perda de vida do Monstro 6
        if monstro_death_6 == False:
            if contadormonstro6 != 1:
                num_monstros += 1
                contadormonstro6 = 1

            if contador6 == 0 and bater_monstro6 == False and contadoresq1 <= 100:
                esqueleto_action3, esqueleto_frame3 = chance_action_monstro(esqueleto_action3, esqueleto_frame3,'parado')
            if contador6 == 0 and bater_monstro6 == False and contadoresq1 > 100:
                esqueleto_action3, esqueleto_frame3 = chance_action_monstro(esqueleto_action3, esqueleto_frame3,'atacando')
                tiroesq3 = True
            if contador6 == 0 and bater_monstro6 == False and contadoresq1 > 113:
                contadoresq1 = 0
            if tiroesq3 == True and morreu6 == False:
                movimentotiro2 += 20
                janela.blit(espada, (1200 + movimentotiro2 - scroll[0], 1515 - scroll[1] - 15))
                tiro_rect2 = espada.get_rect()
                tiro_rect2.x = 1200 + movimentotiro2
                tiro_rect2.y = 1515
                contadortiro4 += 1
                if player_rect.colliderect(tiro_rect2) and contador_hit >= 20 and len(listavida) > 0:
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
                if contadortiro4 >= 100:
                    movimentotiro2 = 0
                    tiroesq3 = False
            if tiroesq2 == False:
                movimentotiro2 = 0
                contadortiro4 = 0
            janela.blit(esqueleto3, (1200 - scroll[0], 1515 - scroll[1] - 15))
            monstro_rect6 = monstro_rect.get_rect()
            monstro_rect6.x = 1200
            monstro_rect6.y = 1515
            if player_rect.colliderect(monstro_rect6) and contador_hit >= 100 and bater == False and game_over == False and morreu6 == False:
                bater_monstro6 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect6) and contador_hit >= 100 and bater == True and bater_monstro6 == False:
                contador6 = 1
                morreu6 = True
                esqueleto_action3, esqueleto_frame3 = chance_action_monstro(esqueleto_action3, esqueleto_frame3, 'morrendo')
                if contadormonstromorte6 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte6 = 1
            if morreu6 == True:
                contadorM6 += 1
                if contadorM6 == 8:
                    if somrodando == True:
                        Sominimigo.play()
                if contadorM6 >= 30:
                    monstro_death_6 = True
            if bater_monstro6 == True:
                esqueleto_action3, esqueleto_frame3 = chance_action_monstro(esqueleto_action3, esqueleto_frame3, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro6 = False

        if contador < 100:
            contador += 1
            if contador0 == 0:
                movimento_monstro0 += 3
            if contador1 == 0:
                movimento_monstro1 += 3
            if contador2 == 0:
                movimento_monstro2 += 3
            if contador3 == 0:
                movimento_monstro3 += 3
            if contador4 == 0:
                movimento_monstro4 += 3
            if contador5 == 0:
                movimento_monstro5 += 3
            if contador6 == 0:
                movimento_monstro6 += 3
            monstro_flip = False
        if contador >= 100:
            contador += 1
            if contador0 == 0:
                movimento_monstro0 -= 3
            if contador1 == 0:
                movimento_monstro1 -= 3
            if contador2 == 0:
                movimento_monstro2 -= 3
            if contador3 == 0:
                movimento_monstro3 -= 3
            if contador4 == 0:
                movimento_monstro4 -= 3
            if contador5 == 0:
                movimento_monstro5 -= 3
            if contador6 == 0:
                movimento_monstro6 -= 3
            monstro_flip = True
        if contador == 200:
            contador = 0

        for tile in morte_rects:
            if player_rect.colliderect(tile):
                tela_gameover = True

        if len(listavida) == 0:
            game_over = True
            if contador_restart > 100:
                tela_gameover = True
            else:
                contador_restart += 1

        if tela_gameover == True:
            pygame.init()
            pygame.mixer.music.unload()

            fontefrase = pygame.font.Font('freesansbold.ttf', 15)
            fontenome = pygame.font.Font('freesansbold.ttf', 10)
            janela_largura = 1200
            janela_altura = 675
            janela = pygame.display.set_mode((janela_largura, janela_altura))
            pygame.display.set_caption('One soul for another')
            if somrodando == True:
                Sommorte.play()
            # load images
            arvore = pygame.image.load('arvoremorte.png')
            arvore = pygame.transform.scale(arvore, (600, 650))

            morte = pygame.image.load('Player_animations/Kaorimorrendo/Kaorimorrendo11.png')
            morte = pygame.transform.scale(morte, (130, 120))

            restart = pygame.image.load('recomecar_restart.png')
            restart = pygame.transform.scale(restart, (230, 109))

            voltar_menu = pygame.image.load('voltar_ao_menu_restart.png')
            voltar_menu = pygame.transform.scale(voltar_menu, (230, 109))

            animation_frames
            animation_frames = {}

            def load_animations(path, frame_duration):
                global animation_frames
                nome_animacao = path.split('/')[-1]
                animation_frame_data = []
                n = 1
                for frame in frame_duration:
                    animation_frame_id = nome_animacao + str(n)
                    img_loc = path + '/' + animation_frame_id + '.png'
                    imagem_animacao = pygame.image.load(img_loc)
                    imagem_animacao = pygame.transform.scale(imagem_animacao, (137, 150))
                    animation_frames[animation_frame_id] = imagem_animacao.copy()
                    for i in range(frame):
                        animation_frame_data.append(animation_frame_id)
                    n += 1
                return animation_frame_data

            def chance_action(action_var, frame, new_value):
                if action_var != new_value:
                    action_var = new_value
                    frame = 0
                return action_var, frame

            animation_database = {}

            animation_database['parada'] = load_animations('Morte_animations/Morteparada', [15, 15, 15])

            morte_action = 'idle'
            morte_frame = 0
            morte_flip = False

            textofrase = fontefrase.render("Ou se morre como herói, ou vive-se o bastante para se tornar o vilão.",
                                           True, (255, 255, 255))
            textonome = fontenome.render("Harvey Dent.", True, (255, 255, 255))

            while True:
                janela.fill((25, 33, 23))
                janela.blit(arvore, (300, -50))
                janela.blit(morte, (550, 330))
                janela.blit(restart, (350, 550))
                janela.blit(voltar_menu, (600, 550))
                janela.blit(textofrase, (350, 500))
                janela.blit(textonome, (760, 530))

                morte_action, morte_frame = chance_action(morte_action, morte_frame, 'parada')

                morte_frame += 1
                if morte_frame >= len(animation_database[morte_action]):
                    morte_frame = 0
                morte_image_id = animation_database[morte_action][morte_frame]
                morte_image = animation_frames[morte_image_id]
                zx = 0
                zy = 0
                janela.blit(pygame.transform.flip(morte_image, morte_flip, False), (470, 300))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        zx, zy = pygame.mouse.get_pos()
                        if zx >= 350 and zx <= 550 and zy >= 550 and zy <= 650:
                            state = "Fase2"
                            return state
                        if zx >= 600 and zx <= 800 and zy >= 550 and zy <= 650:
                            state = "Menu"
                            mixer.music.unload()
                            mixer.music.load("musicamenu.mp3")
                            mixer.music.play(-1)
                            mixer.music.set_volume(0.5)
                            return state

                pygame.display.update()
        # Desenha portão
        if num_monstros_mortos == 7:
            janela.blit(frase_portao, (300, 20))
            portao = pygame.image.load('Portao_aberto.png')
            portao = pygame.transform.scale(portao, (125, 157))
            portao_rect = portao.get_rect()
            portao_rect.x = 9523
            portao_rect.y = 400
            if player_rect.colliderect(portao_rect):
                janela.blit(vitoria, (350, 200))

        if game_over == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_d:
                        movimento_direita = True
                    if event.key == K_a:
                        movimento_esquerda = True
                    if event.key == K_k:
                        bater = True
                        if somrodando == True:
                            Somespada.play()
                    if event.key == K_SPACE:
                        if tempo_no_ar < 6:
                            movimento_vertical = -13
                            if somrodando == True:
                                Sompulo.play()

                if event.type == KEYUP:
                    if event.key == K_d:
                        movimento_direita = False
                    if event.key == K_a:
                        movimento_esquerda = False
                    if event.key == K_k:
                        bater = False
                    if event.key == K_ESCAPE:
                        varpause = True
                        while varpause:
                            janela3 = janela.blit(pause_img, (0, 0))
                            mx = 0
                            my = 0
                            if musicarodando == True:
                                musica = pygame.image.load("colcheiaoff.png")
                                janela.blit(musica, (430, 250))

                            elif musicarodando == False:
                                musica = pygame.image.load("colcheia.png")
                                janela.blit(musica, (525, 250))

                            if somrodando == True:
                                som = pygame.image.load("somoff.png")
                                janela.blit(som, (665, 250))

                            elif somrodando == False:
                                som = pygame.image.load("somon.png")
                                janela.blit(som, (765, 250))

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    mx, my = pygame.mouse.get_pos()
                                    if musicarodando == True and mx >= 430 and mx <= 500 and my >= 250 and my <= 420:
                                        mixer.music.pause()
                                        pygame.display.update()
                                        musicarodando = False

                                    if musicarodando == False and mx >= 525 and mx <= 595 and my >= 250 and my <= 420:
                                        mixer.music.unpause()
                                        pygame.display.update()
                                        musicarodando = True

                                    if somrodando == True and mx >= 665 and mx <= 735 and my >= 250 and my <= 420:
                                        somrodando = False

                                    if somrodando == False and mx >= 765 and mx <= 835 and my >= 250 and my <= 420:
                                        somrodando = True

                                    if mx >= 360 and mx <= 860 and my >= 480 and my <= 580:
                                        mixer.music.unload()
                                        mixer.music.load("musicamenu.mp3")
                                        mixer.music.play(-1)
                                        mixer.music.set_volume(0.5)
                                        state = "Menu"
                                        return state

                                    if mx >= 360 and mx <= 860 and my >= 360 and my <= 460:
                                        state = "Fase2"
                                        return state

                                    if mx >= 360 and mx <= 860 and my >= 110 and my <= 210:
                                        varpause = False
                            pygame.display.update()

        pygame.display.update()

