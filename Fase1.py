import pygame, sys
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from pygame import mixer
import random
import move



def Fase1(state):
    pygame.init()
    fonte = pygame.font.Font('freesansbold.ttf', 45)
    clock = pygame.time.Clock()
    janela_largura = 1200
    janela_altura = 675
    janela = pygame.display.set_mode((janela_largura, janela_altura))
    pygame.display.set_caption('One soul for another')

    player_rect = pygame.Rect(1000, 400, 87, 100)
    cenario = pygame.image.load("cenario (2).jpg")
    cenario = pygame.transform.scale(cenario,(1200, 675))
    tile_tamanho = 50

    #Musica
    mixer.music.load("musicafase1.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)

    # Sons
    Sompulo = pygame.mixer.Sound("jump.mp3")
    Somespada = pygame.mixer.Sound("espadada2.mp3")
    Somdano = pygame.mixer.Sound("Kaorimorrendo.mp3")
    Sominimigo = pygame.mixer.Sound("goblin.mp3")
    Sommorte = pygame.mixer.Sound("mortesound.mp3")
    Sommorte.set_volume(0.3)
    #Load Images

    frase_portao = pygame.image.load('Corraportao.png')
    frase_portao = pygame.transform.scale(frase_portao,(600, 100))

    pause_img = pygame.image.load("pauseimg.png")

    #Parte Grama
    chao_voador = pygame.image.load("chãos.png")
    chao_voador2 = pygame.image.load("chãos.png")
    chao_voador2 = pygame.transform.scale(chao_voador2,(150,120))
    chao_voador3 = pygame.image.load("chaovoador2.png")
    chao_voador3 = pygame.transform.scale(chao_voador3, (655, 433))
    chao_voador4 = pygame.image.load("chãos.png")
    chao_voador4 = pygame.transform.scale(chao_voador4, (200, 170))
    morte_mapa = pygame.image.load("parede.png")
    vila = pygame.image.load("vilarejo.png")
    vila = pygame.transform.scale(vila, (900,675))
    casa = pygame.image.load("casavila.png")
    casa = pygame.transform.scale(casa, (264, 300))
    cerca = pygame.image.load("cerca.png")
    cerca2 = pygame.image.load("cercadireita.png")
    chao_cidade = pygame.image.load("chaocidade.jpg")
    chao_cidade2 = pygame.image.load("chaocidade2.jpg")
    chao_cidade3 = pygame.image.load("chaocidade3.jpg")
    chao_cidade4 = pygame.image.load("chaocidade4.jpg")
    carruagem = pygame.image.load("carruagem.png")
    carruagem = pygame.transform.scale(carruagem, (170, 140))
    parede = pygame.image.load("parede.png")
    monstro_rect = pygame.image.load("parede.png")
    monstro_rect = pygame.transform.scale(monstro_rect,(60,70))
    arvore = pygame.image.load("Arvore.png")
    arvore = pygame.transform.scale(arvore,(300, 262))
    chao_padrao_img = pygame.image.load("chão padrão.png")
    chao_pedra1_img = pygame.image.load("chão pedra 1.jpg")
    chao_pedra2_img = pygame.image.load("chão pedra 2.jpg")
    chao_padrao_final0_img = pygame.image.load("chao_padrao_final0.png")
    chao_padrao_final1_img = pygame.image.load("chao_padrao_final1.png")
    chao_padrao_final2_img = pygame.image.load("chao_padrao_final2.png")
    chao_padrao_final3_img = pygame.image.load("chao_padrao_final3.png")

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
    global somrodando
    global musicarodando
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

    for i in range(5):
        vida = pygame.image.load('Vida.png')
        listavida.append(vida)


    world_data = [[0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,21,12,12,12,12,12,12,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,24,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,24,24,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,12,12,12,12,12,12,12,21,12,12,12,12,12,12,12,12,12,22,12,12,12,12,12,12,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,12,12,12,12,12,12,22,12,21,12,12,12,12,12,12,12,23,12,12,12,12,12,12,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,8,1,1,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,12,12,12,12,12,12,23,12,22,12,12,12,12,12,12,12,12,12,12,12,12,12,12,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,8,1,2,2,2,2,2,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,12,12,12,12,12,12,12,12,12,22,12,12,12,12,12,12,12,12,12,12,12,12,12,12,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,24,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,24,24,24,24,24,24,24,24,24,24,24,24,0,0,0,0,24,24,24,0,0,0,0,0,0,0,0,0,0,0,0,0,10,2,2,2,2,2,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,12,12,12,12,12,12,12,12,12,12,23,12,12,12,12,12,12,12,12,12,12,12,12,12,12,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,24,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,24,24,24,24,24,24,24,24,24,24,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,3,2,2,2,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,2,2,2,2,2,2,2,2,],
                  [26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,27,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,0,0,0,0,0,0,0,0,24,24,0,0,0,0,0,0,0,0,0,24,24,0,0,0,0,0,0,0,0,0,0,0,24,24,24,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,8,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,2,2,2,2,2,2,2,2,],
                  [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,29,2,2,2,2,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,2,3,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,3,2,2,2,2,2,2,2,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,],
                  [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,29,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,29,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,29,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,3,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,3,2,7,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,11,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,2,2,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,3,2,2,2,2,3,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],]

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

    def load_animations_monstro_morte (path,frame_duration):
        global animation_olho_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (129, 100))
            animation_olho_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def load_animations_monstro_ataque (path,frame_duration):
        global animation_olho_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (167, 100))
            animation_olho_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def chance_action_monstro(action_var, frame, new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var,frame

    animation_olho_database = {}

    animation_olho_database['correndo'] = load_animations_monstro('Monstro_OlhoVoador_animations/Olhocorrendo',[3,3,3,3,3,3,3,3])
    animation_olho_database['morrendo'] = load_animations_monstro_morte('Monstro_OlhoVoador_animations/Olhomorrendo', [4,4,4,300])
    animation_olho_database['atacando'] = load_animations_monstro_ataque('Monstro_OlhoVoador_animations/Olhoatacando',[2,2,2,2,2,2,2,2])

    monstro_flip = True

    monstro_action0 = 'correndo'
    monstro_frame0 = 0

    monstro_action1 = 'correndo'
    monstro_frame1 = 0

    monstro_action2 = 'correndo'
    monstro_frame2 = 0

    monstro_action3 = 'correndo'
    monstro_frame3 = 0

    monstro_action4 = 'correndo'
    monstro_frame4 = 0

    monstro_action5 = 'correndo'
    monstro_frame5 = 0

    monstro_action6 = 'correndo'
    monstro_frame6 = 0

    while True:
        true_scroll[0] += (player_rect.x - true_scroll[0] - 600) / 10
        true_scroll[1] += (player_rect.y - true_scroll[1] - 335) / 10
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        janela.fill((146,244,255))
        janela.blit(cenario,(0,0))
        janela.blit(vila,(0 - scroll[0],-170 - scroll[1]))

        v = 1000
        for c in range(19):
            cerca = pygame.transform.scale(cerca, (tile_tamanho, 40))
            janela.blit(cerca, (v - scroll[0], 463 - scroll[1]))
            v += 32
        cerca2 = pygame.transform.scale(cerca2, (tile_tamanho, 40))
        janela.blit(cerca2,(1608 - scroll[0], 463 - scroll[1]))
        janela.blit(casa,(870 - scroll[0],210 - scroll[1]))
        janela.blit(carruagem,(495 - scroll[0],370 - scroll[1]))


        z = 8450
        k = 8350
        for tile_bug in range(28):
            fundo_caverna_img = pygame.transform.scale(fundo_caverna_img, (tile_tamanho, tile_tamanho))
            janela.blit(fundo_caverna_img,(z - scroll[0],100 - scroll[1]))
            janela.blit(fundo_caverna_img, (k - scroll[0], 500 - scroll[1]))
            z += 50
            k += 50


        janela.blit(arvore, (1200 - scroll[0], 240 - scroll[1]))
        janela.blit(arvore, (2600 - scroll[0], 240 - scroll[1]))
        janela.blit(arvore, (6600 - scroll[0], 240 - scroll[1]))

        tile_rects = []
        morte_rects = []

        y=0
        for linha in world_data:
            x=0
            for tile in linha:
                if tile == 1:
                    chao_padrao_img = pygame.transform.scale(chao_padrao_img, (tile_tamanho, tile_tamanho))
                    janela.blit(chao_padrao_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 2:
                    chao_pedra1_img = pygame.transform.scale(chao_pedra1_img, (tile_tamanho, tile_tamanho))
                    janela.blit(chao_pedra1_img,(x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 3:
                    chao_pedra2_img = pygame.transform.scale(chao_pedra2_img, (tile_tamanho, tile_tamanho))
                    janela.blit(chao_pedra2_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 4:
                    chao_padrao_final0_img = pygame.transform.scale(chao_padrao_final0_img, (tile_tamanho, tile_tamanho))
                    janela.blit(chao_padrao_final0_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 5:
                    chao_padrao_final1_img = pygame.transform.scale(chao_padrao_final1_img, (tile_tamanho, tile_tamanho))
                    janela.blit(chao_padrao_final1_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 6:
                    chao_padrao_final2_img = pygame.transform.scale(chao_padrao_final2_img, (tile_tamanho, tile_tamanho))
                    janela.blit(chao_padrao_final2_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 7:
                    chao_padrao_final3_img = pygame.transform.scale(chao_padrao_final3_img, (tile_tamanho, tile_tamanho))
                    janela.blit(chao_padrao_final3_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 8:
                    chao_padrao_final4_img = pygame.transform.scale(chao_padrao_final0_img, (tile_tamanho, tile_tamanho))
                    chao_padrao_final4_img = pygame.transform.flip(chao_padrao_final4_img, True, False)
                    janela.blit(chao_padrao_final4_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 9:
                    chao_padrao_final5_img = pygame.transform.scale(chao_padrao_final1_img, (tile_tamanho, tile_tamanho))
                    chao_padrao_final5_img = pygame.transform.flip(chao_padrao_final5_img, True, False)
                    janela.blit(chao_padrao_final5_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 10:
                    chao_padrao_final6_img = pygame.transform.scale(chao_padrao_final2_img, (tile_tamanho, tile_tamanho))
                    chao_padrao_final6_img = pygame.transform.flip(chao_padrao_final6_img, True, False)
                    janela.blit(chao_padrao_final6_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 11:
                    chao_padrao_final7_img = pygame.transform.scale(chao_padrao_final3_img, (tile_tamanho, tile_tamanho))
                    chao_padrao_final7_img = pygame.transform.flip(chao_padrao_final7_img, True, False)
                    janela.blit(chao_padrao_final7_img, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 24:
                    parede = pygame.transform.scale(parede,(tile_tamanho, tile_tamanho))
                    janela.blit(parede, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 25:
                    morte_mapa = pygame.transform.scale(morte_mapa,(tile_tamanho, tile_tamanho))
                    janela.blit(morte_mapa, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    morte_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 26:
                    chao_cidade = pygame.transform.scale(chao_cidade,(tile_tamanho, tile_tamanho))
                    janela.blit(chao_cidade, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 27:
                    chao_cidade2 = pygame.transform.scale(chao_cidade2,(tile_tamanho, tile_tamanho))
                    janela.blit(chao_cidade2, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 28:
                    chao_cidade3 = pygame.transform.scale(chao_cidade3,(tile_tamanho, tile_tamanho))
                    janela.blit(chao_cidade3, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                if tile == 29:
                    chao_cidade4 = pygame.transform.scale(chao_cidade4,(tile_tamanho, tile_tamanho))
                    janela.blit(chao_cidade4, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))

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

        janela.blit(chao_voador, (2150 - scroll[0], 280 - scroll[1]))
        janela.blit(chao_voador, (4400 - scroll[0], 480 - scroll[1]))
        janela.blit(chao_voador, (4950 - scroll[0], 480 - scroll[1]))
        janela.blit(chao_voador2, (2350 - scroll[0], 174 - scroll[1]))
        janela.blit(chao_voador4, (6300 - scroll[0], 174 - scroll[1]))
        janela.blit(chao_voador2, (6300 - scroll[0], 375 - scroll[1]))
        janela.blit(chao_voador3, (5440 - scroll[0], 375 - scroll[1]))

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
        if monstro_frame0 >= len(animation_olho_database[monstro_action0]):
            monstro_frame0 = 0
        monstro_image_id0 = animation_olho_database[monstro_action0][monstro_frame0]
        monstro0 = animation_olho_frames[monstro_image_id0]

        monstro_frame1 += 1
        if monstro_frame1 >= len(animation_olho_database[monstro_action1]):
            monstro_frame1 = 0
        monstro_image_id1 = animation_olho_database[monstro_action1][monstro_frame1]
        monstro1 = animation_olho_frames[monstro_image_id1]

        monstro_frame2 += 1
        if monstro_frame2 >= len(animation_olho_database[monstro_action2]):
            monstro_frame2 = 0
        monstro_image_id2 = animation_olho_database[monstro_action2][monstro_frame2]
        monstro2 = animation_olho_frames[monstro_image_id2]

        monstro_frame3 += 1
        if monstro_frame3 >= len(animation_olho_database[monstro_action3]):
            monstro_frame3 = 0
        monstro_image_id3 = animation_olho_database[monstro_action3][monstro_frame3]
        monstro3 = animation_olho_frames[monstro_image_id3]

        monstro_frame4 += 1
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
        monstro6 = animation_olho_frames[monstro_image_id]

        contador_hit += 1
        #Ataque e perda de vida do Monstro 0
        if monstro_death_0 == False:
            if contadormonstro0 != 1:
                num_monstros += 1
                contadormonstro0 = 1
            if contador0 == 0 and bater_monstro0 == False:
                monstro_action0, monstro_frame0 = chance_action_monstro(monstro_action0, monstro_frame0, 'correndo')

            janela.blit(pygame.transform.flip(monstro0, monstro_flip, False), (2000 - scroll[0] + movimento_monstro0, 425 - scroll[1] - 15))
            monstro_rect0 = monstro_rect.get_rect()
            monstro_rect0.x = 2040 + movimento_monstro0
            monstro_rect0.y = 440
            if player_rect.colliderect(monstro_rect0) and contador_hit >= 100 and bater == False and game_over == False and morreu0 == False:
                bater_monstro0 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect0) and contador_hit >= 100 and bater == True and bater_monstro0 == False:
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
                monstro_action1, monstro_frame1 = chance_action_monstro(monstro_action1, monstro_frame1, 'correndo')
            janela.blit(pygame.transform.flip(monstro1, monstro_flip, False), (3180 - scroll[0] + movimento_monstro1, 275 - scroll[1] - 15))
            monstro_rect1 = monstro_rect.get_rect()
            monstro_rect1.x = 3220 + movimento_monstro1
            monstro_rect1.y = 290

            if player_rect.colliderect(monstro_rect1) and contador_hit >= 100 and bater == False and game_over == False and morreu1 == False:
                bater_monstro1 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect1) and contador_hit >= 100 and bater == True and bater_monstro1 == False:
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
                monstro_action2, monstro_frame2 = chance_action_monstro(monstro_action2, monstro_frame2, 'correndo')
            janela.blit(pygame.transform.flip(monstro2, monstro_flip, False), (2870 - scroll[0] + movimento_monstro2, 425 - scroll[1] - 15))
            monstro_rect2 = monstro_rect.get_rect()
            monstro_rect2.x = 2910 + movimento_monstro2
            monstro_rect2.y = 440
            contador_hit += 1
            if player_rect.colliderect(monstro_rect2) and contador_hit >= 100 and bater == False and game_over == False and morreu2 == False:
                bater_monstro2 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect2) and contador_hit >= 100 and bater == True and bater_monstro2 == False:
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
                monstro_action3, monstro_frame3 = chance_action_monstro(monstro_action3, monstro_frame3, 'correndo')
            janela.blit(pygame.transform.flip(monstro3, monstro_flip, False), (3560 - scroll[0] + movimento_monstro3, 425 - scroll[1] - 15))
            monstro_rect3 = monstro_rect.get_rect()
            monstro_rect3.x = 3600 + movimento_monstro3
            monstro_rect3.y = 440

            if player_rect.colliderect(monstro_rect3) and contador_hit >= 100 and bater == False and game_over == False and morreu3 == False:
                bater_monstro3 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect3) and contador_hit >= 100 and bater == True and bater_monstro3 == False:
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

        # Ataque e perda de vida do Monstro 4
        if monstro_death_4 == False:
            if contadormonstro4 != 1:
                num_monstros += 1
                contadormonstro4 = 1
            if contador4 == 0 and bater_monstro4 == False:
                monstro_action4, monstro_frame4 = chance_action_monstro(monstro_action4, monstro_frame4, 'correndo')
            janela.blit(pygame.transform.flip(monstro4, monstro_flip, False), (5700 - scroll[0] + movimento_monstro4, 325 - scroll[1] - 15))
            monstro_rect4 = monstro_rect.get_rect()
            monstro_rect4.x = 5740 + movimento_monstro4
            monstro_rect4.y = 340

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
                monstro_action4, monstro_frame4 = chance_action_monstro(monstro_action4, monstro_frame4, 'morrendo')
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
                monstro_action4, monstro_frame4 = chance_action_monstro(monstro_action4, monstro_frame4, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro4 = False

        # Ataque e perda de vida do Monstro 5
        if monstro_death_5 == False:
            if contadormonstro5 != 1:
                num_monstros += 1
                contadormonstro5 = 1
            if contador5 == 0 and bater_monstro5 == False:
                monstro_action5, monstro_frame5 = chance_action_monstro(monstro_action5, monstro_frame5, 'correndo')
            janela.blit(pygame.transform.flip(monstro5, monstro_flip, False), (6600 - scroll[0] + movimento_monstro5, 425 - scroll[1] - 15))
            monstro_rect5 = monstro_rect.get_rect()
            monstro_rect5.x = 6640 + movimento_monstro5
            monstro_rect5.y = 440

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
                monstro_action5, monstro_frame5 = chance_action_monstro(monstro_action5, monstro_frame5, 'morrendo')
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
                monstro_action5, monstro_frame5 = chance_action_monstro(monstro_action5, monstro_frame5, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro5 = False
        # Ataque e perda de vida do Monstro 6
        if monstro_death_6 == False:
            if contadormonstro6 != 1:
                num_monstros += 1
                contadormonstro6 = 1
            if contador6 == 0 and bater_monstro6 == False:
                monstro_action6, monstro_frame6 = chance_action_monstro(monstro_action6, monstro_frame6, 'correndo')
            janela.blit(pygame.transform.flip(monstro6, monstro_flip, False), (7750 - scroll[0] + movimento_monstro6, 425 - scroll[1] - 15))
            monstro_rect6 = monstro_rect.get_rect()
            monstro_rect6.x = 7790 + movimento_monstro6
            monstro_rect6.y = 440
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
                monstro_action6, monstro_frame6 = chance_action_monstro(monstro_action6, monstro_frame6, 'morrendo')
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
                monstro_action6, monstro_frame6 = chance_action_monstro(monstro_action6, monstro_frame6, 'atacando')
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
            restartvermelho = pygame.image.load('recomecar_restartvermelho.png')
            restartvermelho = pygame.transform.scale(restartvermelho, (230, 109))

            voltar_menu = pygame.image.load('voltar_ao_menu_restart.png')
            voltar_menu = pygame.transform.scale(voltar_menu, (230, 109))
            voltar_menuvermelho = pygame.image.load('voltar_ao_menu_restartvermelho.png')
            voltar_menuvermelho = pygame.transform.scale(voltar_menuvermelho, (230, 109))

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
                mouseposic = pygame.mouse.get_pos()
                if mouseposic[0] >= 600 and mouseposic[0] <= 800 and mouseposic[1] >= 550 and mouseposic[1] <= 650:
                    janela.blit(voltar_menuvermelho, (600, 550))

                if mouseposic[0] >= 350 and mouseposic[0] <= 550 and mouseposic[1] >= 550 and mouseposic[1] <= 650:
                    janela.blit(restartvermelho, (350, 550))

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
                            state = "Fase1"
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
            janela.blit(frase_portao, (350, 20))
            portao = pygame.image.load('Portao_aberto.png')
            portao = pygame.transform.scale(portao, (125, 157))
            portao_rect = portao.get_rect()
            portao_rect.x = 9523
            portao_rect.y = 400
            if player_rect.colliderect(portao_rect):
                state = "Fase2"
                return state

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
                            print(somrodando , musicarodando)
                            janela3 = janela.blit(pause_img, (0, 0))
                            mouseposic = pygame.mouse.get_pos()
                            voltarmenuon = pygame.image.load("voltarmenupause.png")
                            reiniciaron = pygame.image.load("reiniciarfasepause.png")
                            voltarjogo = pygame.image.load("voltaraojogopause.png")
                            mx = 0
                            my = 0
                            if mouseposic[0] >= 360 and mouseposic[0] <= 860 and mouseposic[1] >= 480 and mouseposic[1] <= 580 :
                                janela.blit(voltarmenuon, (0, 0))

                            if mouseposic[0] >= 360 and mouseposic[0] <= 860 and mouseposic[1] >= 360 and mouseposic[1] <= 460 :
                                janela.blit(reiniciaron, (0, 0))

                            if mouseposic[0] >= 360 and mouseposic[0] <= 860 and mouseposic[1] >= 110 and mouseposic[1] <= 210 :
                                janela.blit(voltarjogo, (0, 0))

                            if musicarodando == True:
                                musica = pygame.image.load("colcheiaoff.png")
                                janela.blit(musica, (430, 250))
                                if mouseposic[0] >= 430 and mouseposic[0] <= 500 and mouseposic[1] >= 250 and mouseposic[1] <= 420:
                                    musica1 = pygame.image.load("colcheiaoffvermelha.png")
                                    janela.blit(musica1,(430, 250))

                            elif musicarodando == False:
                                musica = pygame.image.load("colcheia.png")
                                janela.blit(musica, (525, 250))
                                if mouseposic[0] >= 525 and mouseposic[0] <= 595 and mouseposic[1] >= 250 and mouseposic[1] <= 420:
                                    musica1 = pygame.image.load("colcheiavermelha.png")
                                    janela.blit(musica1,(525, 250))

                            if somrodando == True:
                                som = pygame.image.load("somoff.png")
                                janela.blit(som, (665, 250))
                                if mouseposic[0] >= 665 and mouseposic[0] <= 735 and mouseposic[1] >= 250 and mouseposic[1] <= 420:
                                    musica1 = pygame.image.load("somoffvermelho.png")
                                    janela.blit(musica1,(665, 250))

                            elif somrodando == False:
                                som = pygame.image.load("somon.png")
                                janela.blit(som, (765, 250))
                                if mouseposic[0] >= 765 and mouseposic[0] <= 835 and mouseposic[1] >= 250 and mouseposic[1] <= 420:
                                    musica1 = pygame.image.load("somonvermelho.png")
                                    janela.blit(musica1,(765, 250))

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
                                        state = "Fase1"
                                        return state

                                    if mx >= 360 and mx <= 860 and my >= 110 and my <= 210:
                                        varpause = False
                            pygame.display.update()
        clock.tick(300)
        print("clock.tick:", clock.tick())
        print("clock.get_fps", clock.get_fps())
        pygame.display.update()

