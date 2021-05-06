import pygame, sys
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from pygame import mixer
import random
import move

def Fase2(state,listavida):
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
    Sommorte = pygame.mixer.Sound("mortesound.mp3")
    Sommorte.set_volume(0.3)
    Somesqueleto = pygame.mixer.Sound("morteesqueleto.mp3")
    Somslime = pygame.mixer.Sound("slimemorte.mp3")
    Somcobra = pygame.mixer.Sound("cobramorte.mp3")
    Somtiroesqueleto = pygame.mixer.Sound("tiroesqueleto.mp3")
    Somtiroesqueleto.set_volume(1)
    Somporradaboss = pygame.mixer.Sound("fireball.mp3")
    Somminhoca = pygame.mixer.Sound("somminhoca.mp3")

    #Load Images

    frase_portao = pygame.image.load('Corraportao.png')
    frase_portao = pygame.transform.scale(frase_portao,(600, 102))
    pause_img = pygame.image.load("pauseimg.png")
    barra_hp = pygame.image.load("barra_HP.png")
    barra_hp = pygame.transform.scale(barra_hp,(350,39))
    barra_hp_boss = pygame.image.load("Barra_hp_boss.png")
    barra_hp_boss = pygame.transform.scale(barra_hp_boss, (624, 39))
    nome_boss = pygame.image.load("nome_boss.png")
    nome_boss = pygame.transform.scale(nome_boss, (250, 89))
    superjump = pygame.image.load("superjumpmini.png")
    v = pygame.image.load("V.png")

    castelo = pygame.image.load("castelo.png")
    castelo = pygame.transform.scale(castelo,(1200,476))
    entrada = pygame.image.load("entrada.png")
    entrada = pygame.transform.scale(entrada, (251, 335))
    morte_mapa = pygame.image.load("parede.png")
    parede = pygame.image.load("parede.png")
    monstro_rect = pygame.image.load("parede.png")
    monstro_rect = pygame.transform.scale(monstro_rect,(110,80))
    minhoca_rect = pygame.image.load("parede.png")
    minhoca_rect = pygame.transform.scale(minhoca_rect, (73, 63))
    minhoca_rect_dano = pygame.transform.scale(minhoca_rect, (35, 63))
    boss_rect = pygame.image.load("Rectboss.png")
    boss_rect = pygame.transform.scale(boss_rect,(90, 105))
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
    chaocastelo = pygame.image.load("chaocastelo.png")

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
    bater_monstro7 = False
    bater_monstro8 = False
    bater_monstro9 = False
    bater_monstro10 = False
    bater_monstro11 = False
    bater_monstro12 = False
    bater_monstro13 = False
    bater_monstro14 = False
    bater_monstro15 = False
    monstro_death_0 = False
    monstro_death_1 = False
    monstro_death_2 = False
    monstro_death_3 = False
    monstro_death_4 = False
    monstro_death_5 = False
    monstro_death_6 = False
    monstro_death_7 = False
    monstro_death_8 = False
    monstro_death_9 = False
    monstro_death_10 = False
    monstro_death_11 = False
    monstro_death_12 = False
    monstro_death_13 = False
    monstro_death_14 = False
    monstro_death_15 = False
    movimento_vertical = 0
    tempo_no_ar = 0
    direction = 1
    vidas = 5
    x = 100
    movimento_monstro0 = 0
    movimento_monstro1 = 0
    movimento_monstro2 = 0
    movimento_monstro3 = 0
    movimento_monstro4 = 0
    movimento_monstro5 = 0
    movimento_monstro6 = 0
    movimento_monstro7 = 0
    movimento_monstro8 = 0
    movimento_monstro9 = 0
    movimento_monstro10 = 0
    movimento_monstro11 = 0
    movimento_monstro12 = 0
    movimento_monstro13 = 0
    movimento_monstro14 = 0
    movimento_monstro15 = 0
    contador = 0
    contador_2 = 0
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
    contadormonstro7 = 0
    contadormonstro8 = 0
    contadormonstro9 = 0
    contadormonstro10 = 0
    contadormonstro11 = 0
    contadormonstro12 = 0
    contadormonstro13 = 0
    contadormonstro14 = 0
    contadormonstro15 = 0
    contadormonstromorte0 = 0
    contadormonstromorte1 = 0
    contadormonstromorte2 = 0
    contadormonstromorte3 = 0
    contadormonstromorte4 = 0
    contadormonstromorte5 = 0
    contadormonstromorte6 = 0
    contadormonstromorte7 = 0
    contadormonstromorte8 = 0
    contadormonstromorte9 = 0
    contadormonstromorte10 = 0
    contadormonstromorte11 = 0
    contadormonstromorte12 = 0
    contadormonstromorte13 = 0
    contadormonstromorte14 = 0
    contadormonstromorte15 = 0
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
    contador7 = 0
    contador8 = 0
    contador9 = 0
    contador10 = 0
    contador11 = 0
    contador12 = 0
    contador13 = 0
    contador14 = 0
    contador15 = 0
    contadorM0 = 0
    contadorM1 = 0
    contadorM2 = 0
    contadorM3 = 0
    contadorM4 = 0
    contadorM5 = 0
    contadorM6 = 0
    contadorM7 = 0
    contadorM8 = 0
    contadorM9 = 0
    contadorM10 = 0
    contadorM11 = 0
    contadorM12 = 0
    contadorM13 = 0
    contadorM14 = 0
    contadorM15 = 0
    contadorhit_player = 0
    contadorbater_monstro = 0
    morreu0 = False
    morreu1 = False
    morreu2 = False
    morreu3 = False
    morreu4 = False
    morreu5 = False
    morreu6 = False
    morreu7 = False
    morreu8 = False
    morreu9 = False
    morreu10 = False
    morreu11 = False
    morreu12 = False
    morreu13 = False
    morreu14 = False
    morreu15 = False
    contadordisparo_slime1 = True
    contadordisparo_slime2 = True
    contadordisparo_slime3 = True
    contadordisparo_slime4 = True
    movimentotiro = 0
    movimentotiro1 = 0
    movimentotiro2 = 0
    movimentotiro5 = 0

    contadortiro = 0
    contadortiro2 = 0
    contadortiro3 = 0
    contadortiro4 = 0
    contadortiro5 = 0
    contadoresq1 = 0
    contadoreslm = 0
    contadormin1 = 0
    contadormin2 = 0
    contadormin3 = 0
    contadormin4 = 0
    tiroesq1 = False
    tiroesq2 = False
    tiroesq3 = False
    contadorboss = 0
    contadorhitboss = 0
    listavidaboss = []

    for i in range(8):
        hp = pygame.image.load('HP.png')
        hp = pygame.transform.scale(hp, (35, 39))
        listavida.append(hp)


    for i in range(25):
        hp = pygame.image.load('hp_boss.png')
        hp = pygame.transform.scale(hp, (35, 39))
        listavidaboss.append(hp)



    world_data =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2,2],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,4,9,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,9,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,0,0,0,0,4,2,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,9,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,0,0,0,0,4,2,2,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,2,2,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,7,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,5,5,6,0,0,0,0,0,9,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,9,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,9,2,2,1,1,1,3,0,0,4,1,1,3,0,0,4,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,3,0,0,0,7,2,2,2,2,2,8,0,0,9,2,2,8,0,0,9,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,5,1,1,3,0,4,1,3,0,4,1,3,0,4,1,3,0,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,7,2,2,2,2,8,0,0,9,2,2,8,0,0,9,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,5,6,0,7,5,6,0,7,5,6,0,7,5,6,0,7,5,6,0,7,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0,7,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,1,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,2,2,2,2,2,2,2,2,2,2,22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,7,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,10,10,10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                 [0,0,0,0,0,0,0,0,0,0,0,0,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],]

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
    global animation_minhoca_frames
    animation_minhoca_frames = {}
    global animation_cobra_frames
    animation_cobra_frames = {}
    global animation_boss_frames
    animation_boss_frames = {}


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

    def load_animations_minhoca (path,frame_duration):
        global animation_minhoca_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (110, 101))
            animation_minhoca_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def load_animations_cobra(path,frame_duration):
        global animation_cobra_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (110, 101))
            animation_cobra_frames[animation_frame_id] = imagem_animacao.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def load_animations_boss(path,frame_duration):
        global animation_boss_frames
        nome_animacao = path.split('/')[-1]
        animation_frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = nome_animacao + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            imagem_animacao = pygame.image.load(img_loc)
            imagem_animacao = pygame.transform.scale(imagem_animacao, (241, 160))
            animation_boss_frames[animation_frame_id] = imagem_animacao.copy()
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
    animation_minhoca_database = {}
    animation_cobra_database = {}
    animation_boss_database = {}

    animation_morcego_database['parado'] = load_animations_monstro('Slime_Animations/Slimeparado', [4, 4, 4, 4])
    animation_morcego_database['morrendo'] = load_animations_monstro('Slime_Animations/Slimemorrendo', [4, 4, 4, 300])
    animation_morcego_database['atacando'] = load_animations_monstro('Slime_Animations/Slimecuspindo',[2, 2, 2, 2, 2, ])
    animation_slimeT_database['tiro'] = load_animations_slime_tiro('Disparos_animations/SlimeT',[2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    animation_esqueleto_database['parado'] = load_animations_esqueleto('Esqueleto_animations/Esqueletoparado',[2,2,2,2])
    animation_esqueleto_database['morrendo'] = load_animations_esqueleto('Esqueleto_animations/Esqueletomorrendo',[9,9,9,9])
    animation_esqueleto_database['atacando'] = load_animations_esqueleto('Esqueleto_animations/Esqueletoatacando',[4,4,4,4,4,4])
    animation_espada_database['atacando'] = load_animations_esqueleto_tiro('Disparos_animations/Espada',[2,2,2])
    animation_minhoca_database['atacando'] = load_animations_minhoca('Minhoca_Animations/Minhocaatacando', [2,2,2,2,2,2,2,2])
    animation_minhoca_database['hit'] = load_animations_minhoca('Minhoca_Animations/Minhocahit', [2,2,2])
    animation_minhoca_database['parado'] = load_animations_minhoca('Minhoca_Animations/Minhocaparada', [2,2,2,2,2,2,2,2])
    animation_cobra_database['parado'] = load_animations_cobra('Cobra_Animations/Cobraparada', [2,2,2,2,2,2,2,2,2])
    animation_cobra_database['andando'] = load_animations_cobra('Cobra_Animations/Cobraandando', [2, 2, 2, 2, 2, 2])
    animation_cobra_database['atacando'] = load_animations_cobra('Cobra_Animations/Cobraatacando', [2, 2, 2, 2, 2, 2])
    animation_cobra_database['hit'] = load_animations_cobra('Cobra_Animations/Cobrahit', [6, 6, 6])
    animation_boss_database['andando'] = load_animations_boss('Ladino_Animations/Andando', [2,2,2,2,2,2,2,2])
    animation_boss_database['atacando'] = load_animations_boss('Ladino_Animations/Atacando', [2,2,2,2,2,2,2,2,2,2])
    animation_boss_database['atirando'] = load_animations_boss('Ladino_Animations/Atirando', [4,4,4,4,4,4,4,4,4])
    animation_boss_database['hit'] = load_animations_boss('Ladino_Animations/hit', [2,2,2])
    animation_boss_database['morrendo'] = load_animations_boss('Ladino_Animations/Morrendo', [2,2,2,2,2,2,2,2,2,2])
    animation_boss_database['parado'] = load_animations_boss('Ladino_Animations/Parado', [2,2,2,2,2,2,2,2])

    boss_action = 'parado'
    boss_frame = 0

    cobra_action1 = 'parado'
    cobra_frame1 = 0

    cobra_action2 = 'parado'
    cobra_frame2 = 0

    cobra_action3 = 'parado'
    cobra_frame3 = 0

    cobra_action4 = 'parado'
    cobra_frame4 = 0

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
    monstro_flip_cobra = False

    monstro_action0 = 'parado'
    monstro_frame0 = 0

    monstro_action1 = 'parado'
    monstro_frame1 = 0

    monstro_action2 = 'parado'
    monstro_frame2 = 0

    monstro_action3 = 'parado'
    monstro_frame3 = 0

    minhoca_action0 = 'parado'
    minhoca_frame0 = 0

    minhoca_action1 = 'parado'
    minhoca_frame1 = 0

    minhoca_action2 = 'parado'
    minhoca_frame2 = 0

    minhoca_action3 = 'parado'
    minhoca_frame3 = 0

    while True:

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
        janela.blit(castelo,(3500 - scroll[0],2250 - scroll[1]))

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
                if tile == 10:
                    chaocastelo = pygame.transform.scale(chaocastelo, (tile_tamanho, tile_tamanho))
                    janela.blit(chaocastelo, (x * tile_tamanho - scroll[0], y * tile_tamanho - scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_tamanho, y * tile_tamanho, tile_tamanho, tile_tamanho))
                x+=1
            y+= 1

        janela.blit(barra_hp,(20,25))
        janela.blit(superjump,(380,20))
        janela.blit(v,(197,30))


        #Desenha Vidas
        x = 55
        for vida in listavida:
            janela.blit(vida,(x, 25))
            x += 35

        #Desenha numero de Monstros a serem derrotados
        janela.blit(contador_monstro, (70, 70))
        texto = fonte.render(str(num_monstros_mortos) + " / " + str(num_monstros),True, (0, 0, 0))
        janela.blit(texto, (150, 77))

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

        janela.blit(portao, (5043 - scroll[0], 2500 - scroll[1]))
        janela.blit(pygame.transform.flip(player_image, player_flip, False),(player_rect.x - scroll[0], player_rect.y - scroll[1]))

        janela.blit(entrada,(3415 - scroll[0],2325 - scroll[1]))
        janela.blit(entrada, (4550 - scroll[0], 2325 - scroll[1]))
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

        minhoca_frame0 += 1
        if minhoca_frame0 >= len(animation_minhoca_database[minhoca_action0]):
            minhoca_frame0 = 0
        minhoca_image_id0 = animation_minhoca_database[minhoca_action0][minhoca_frame0]
        minhoca0 = animation_minhoca_frames[minhoca_image_id0]

        minhoca_frame1 += 1
        if minhoca_frame1 >= len(animation_minhoca_database[minhoca_action1]):
            minhoca_frame1 = 0
        minhoca_image_id1 = animation_minhoca_database[minhoca_action1][minhoca_frame1]
        minhoca1 = animation_minhoca_frames[minhoca_image_id1]

        minhoca_frame2 += 1
        if minhoca_frame2 >= len(animation_minhoca_database[minhoca_action2]):
            minhoca_frame2 = 0
        minhoca_image_id2 = animation_minhoca_database[minhoca_action2][minhoca_frame2]
        minhoca2 = animation_minhoca_frames[minhoca_image_id2]

        minhoca_frame3 += 1
        if minhoca_frame3 >= len(animation_minhoca_database[minhoca_action3]):
            minhoca_frame3 = 0
        minhoca_image_id3 = animation_minhoca_database[minhoca_action3][minhoca_frame3]
        minhoca3 = animation_minhoca_frames[minhoca_image_id3]

        cobra_frame1 += 1
        if cobra_frame1 >= len(animation_cobra_database[cobra_action1]):
            cobra_frame1 = 0
        cobra_image_id1 = animation_cobra_database[cobra_action1][cobra_frame1]
        cobra1 = animation_cobra_frames[cobra_image_id1]

        cobra_frame2 += 1
        if cobra_frame2 >= len(animation_cobra_database[cobra_action2]):
            cobra_frame2 = 0
        cobra_image_id2 = animation_cobra_database[cobra_action2][cobra_frame2]
        cobra2 = animation_cobra_frames[cobra_image_id2]

        cobra_frame3 += 1
        if cobra_frame3 >= len(animation_cobra_database[cobra_action3]):
            cobra_frame3 = 0
        cobra_image_id3 = animation_cobra_database[cobra_action3][cobra_frame3]
        cobra3 = animation_cobra_frames[cobra_image_id3]

        cobra_frame4 += 1
        if cobra_frame4 >= len(animation_cobra_database[cobra_action4]):
            cobra_frame4 = 0
        cobra_image_id4 = animation_cobra_database[cobra_action4][cobra_frame4]
        cobra4 = animation_cobra_frames[cobra_image_id4]

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

        boss_frame += 1
        if boss_frame >= len(animation_boss_database[boss_action]):
            boss_frame = 0
        boss_image_id = animation_boss_database[boss_action][boss_frame]
        boss = animation_boss_frames[boss_image_id]

        contadoresq1 += 1
        contadoreslm += 1
        contador_hit += 1
        #Ataque e perda de vida do Monstro 0
        if monstro_death_0 == False:
            if contadormonstro0 != 1:
                num_monstros += 1
                contadormonstro0 = 1
            if contador0 == 0 and bater_monstro0 == False:
                monstro_action0, monstro_frame0 = chance_action_monstro(monstro_action0, monstro_frame0, 'parado')
            if contador0 == 0 and bater_monstro0 == False and contadoreslm > 10:
                monstro_action0, monstro_frame0 = chance_action_monstro(monstro_action0, monstro_frame0,'atacando')
                tiroslm = True
            #if contador0 == 0 and bater_monstro0 == False and contadoreslm > 17:
                #contadoreslm = 0
                #Somtiroslime.play()
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
                if contadortiro >= 80:
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
                        Somslime.play()
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
            if contador1 == 0 and bater_monstro1 == False and contadoreslm > 10:
                monstro_action1, monstro_frame1 = chance_action_monstro(monstro_action1, monstro_frame1,'atacando')
                tiroslm = True
            #if contador1 == 0 and bater_monstro1 == False and contadoreslm > 17:
                #contadoreslm = 0
                #Somtiroslime.play()
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
                        Somslime.play()
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
            if contador2 == 0 and bater_monstro2 == False and contadoreslm > 10:
                monstro_action2, monstro_frame2 = chance_action_monstro(monstro_action2, monstro_frame2,'atacando')
                tiroslm= True
            #if contador2 == 0 and bater_monstro2 == False and contadoreslm > 17:
                #contadoreslm = 0
                #Somtiroslime.play()
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
                        Somslime.play()
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
            if contador3 == 0 and bater_monstro3 == False and contadoreslm > 10:
                monstro_action3, monstro_frame3 = chance_action_monstro(monstro_action3, monstro_frame3,'atacando')
            if contador3 == 0 and bater_monstro3 == False and contadoreslm > 17:
                contadoreslm = 0

                #Somtiroslime.play()

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
                        Somslime.play()
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
            if contador4 == 0 and bater_monstro4 == False and contadoresq1 <= 100:
                esqueleto_action1, esqueleto_frame1 = chance_action_monstro(esqueleto_action1, esqueleto_frame1, 'parado')
            if contador4 == 0 and bater_monstro4 == False and contadoresq1 > 100:
                esqueleto_action1, esqueleto_frame1 = chance_action_monstro(esqueleto_action1, esqueleto_frame1,'atacando')
                tiroesq1 = True
            if contador4 == 0 and bater_monstro4 == False and contadoresq1 > 113:
                contadoresq1 = 0
                if musicarodando == True and player_rect.x >= 650 and player_rect.x <= 2300 and player_rect.y >= 1200 and player_rect.y <= 1850:
                    Somtiroesqueleto.play()
            if tiroesq1 == True and morreu4 == False:
                movimentotiro5 += 3
                janela.blit(espada, (650 + movimentotiro5 - scroll[0], 1565 - scroll[1] - 15))
                tiro_rect1 = espada.get_rect()
                tiro_rect1.x = 650 + movimentotiro5
                tiro_rect1.y = 1565
                contadortiro5 += 1
                if player_rect.colliderect(tiro_rect1) and contador_hit >= 20 and len(listavida) > 0:
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
                if contadortiro5 >= 200:
                    movimentotiro5 = 0
                    tiroesq1 = False
            if tiroesq1 == False:
                movimentotiro5 = 0
                contadortiro5 = 0
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
                        Somesqueleto.play()
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
                if musicarodando == True and player_rect.x >= 650 and player_rect.x <= 2300 and player_rect.y >= 1200 and player_rect.y <= 1850:
                    Somtiroesqueleto.play()
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
                        Somesqueleto.play()
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
                if musicarodando == True and player_rect.x >= 650 and player_rect.x <= 2300 and player_rect.y >= 1200 and player_rect.y <= 1850:
                    Somtiroesqueleto.play()
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
                        Somesqueleto.play()
                if contadorM6 >= 30:
                    monstro_death_6 = True
            if bater_monstro6 == True:
                esqueleto_action3, esqueleto_frame3 = chance_action_monstro(esqueleto_action3, esqueleto_frame3, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro6 = False
            contadormin1 += 1
            contadormin2 += 1
            contadormin3 += 1
            contadormin4 += 1
        # Ataque e perda de vida do Monstro 7
        if monstro_death_7 == False:
            if contadormonstro7 != 1:
                num_monstros += 1
                contadormonstro7 = 1

            if contador7 == 0 and bater_monstro7 == False and contadormin1 <= 70:
                minhoca_action0, minhoca_frame0 = chance_action_monstro(minhoca_action0, minhoca_frame0,'parado')
            if contador7 == 0 and bater_monstro7 == False and contadormin1 > 70:
                minhoca_action0, minhoca_frame0 = chance_action_monstro(minhoca_action0, minhoca_frame0,'atacando')
                tiroesq3 = True
            if contador7 == 0 and bater_monstro7 == False and contadormin1 > 83:
                contadormin1 = 0

            janela.blit(pygame.transform.flip(minhoca0, monstro_flip, False), (4360 - scroll[0], 2165 - scroll[1] - 15))
            monstro_rect7_dano = minhoca_rect_dano.get_rect()
            monstro_rect7_dano.x = 4398
            monstro_rect7_dano.y = 2203
            if minhoca_action0 == 'atacando':
                monstro_rect7 = minhoca_rect.get_rect()
                monstro_rect7.x = 4360 + movimento_monstro7
                monstro_rect7.y = 2203
                pygame.draw.rect(janela,(255,255,255),monstro_rect7)
                if player_rect.colliderect(monstro_rect7) and contador_hit >= 50 and bater == False and game_over == False and morreu7 == False:
                    bater_monstro7 = True
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
            if player_rect.colliderect(monstro_rect7_dano) and contador_hit >= 100 and bater == True and bater_monstro7 == False:
                contador7 = 1
                morreu7 = True
                minhoca_action0, minhoca_frame0 = chance_action_monstro(minhoca_action0, minhoca_frame0,'hit')
                if contadormonstromorte7 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte7 = 1
            if morreu7 == True:
                contadorM7 += 1
                if contadorM7 == 8:
                    if somrodando == True:
                        Somminhoca.play()
                if contadorM7 >= 30:
                    monstro_death_7 = True
            if bater_monstro7 == True:
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro7 = False

        # Ataque e perda de vida do Monstro 8
        if monstro_death_8 == False:
            if contadormonstro8 != 1:
                num_monstros += 1
                contadormonstro8 = 1

            if contador8 == 0 and bater_monstro8 == False and contadormin2 <= 70:
                minhoca_action1, minhoca_frame1 = chance_action_monstro(minhoca_action1, minhoca_frame1,'parado')
            if contador8 == 0 and bater_monstro8 == False and contadormin2 > 70:
                minhoca_action1, minhoca_frame1 = chance_action_monstro(minhoca_action1, minhoca_frame1,'atacando')
                tiroesq3 = True
            if contador8 == 0 and bater_monstro8 == False and contadormin2 > 83:
                contadormin2 = 0

            janela.blit(pygame.transform.flip(minhoca1, monstro_flip, False),(3850 - scroll[0], 2165 - scroll[1] - 15))
            monstro_rect8_dano = minhoca_rect_dano.get_rect()
            monstro_rect8_dano.x = 3888
            monstro_rect8_dano.y = 2203
            if minhoca_action1 == 'atacando':
                monstro_rect8 = minhoca_rect.get_rect()
                monstro_rect8.x = 3850 + movimento_monstro8
                monstro_rect8.y = 2203
                pygame.draw.rect(janela, (255, 255, 255), monstro_rect8)
                if player_rect.colliderect(monstro_rect8) and contador_hit >= 50 and bater == False and game_over == False and morreu8 == False:
                    bater_monstro8 = True
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
            if player_rect.colliderect(monstro_rect8_dano) and contador_hit >= 100 and bater == True and bater_monstro8 == False:
                contador8 = 1
                morreu8 = True
                minhoca_action1, minhoca_frame1 = chance_action_monstro(minhoca_action1, minhoca_frame1,'hit')
                if contadormonstromorte8 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte8 = 1
            if morreu8 == True:
                contadorM8 += 1
                if contadorM8 == 8:
                    if somrodando == True:
                        Somminhoca.play()
                if contadorM8 >= 30:
                    monstro_death_8 = True
            if bater_monstro8 == True:
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro8 = False

        # Ataque e perda de vida do Monstro 9
        if monstro_death_9 == False:
            if contadormonstro9 != 1:
                num_monstros += 1
                contadormonstro9 = 1

            if contador9 == 0 and bater_monstro9 == False and contadormin3 <= 70:
                minhoca_action2, minhoca_frame2 = chance_action_monstro(minhoca_action2, minhoca_frame2,'parado')
            if contador9 == 0 and bater_monstro9 == False and contadormin3 > 70:
                minhoca_action2, minhoca_frame2 = chance_action_monstro(minhoca_action2, minhoca_frame2,'atacando')
                tiroesq3 = True
            if contador9 == 0 and bater_monstro9 == False and contadormin3 > 83:
                contadormin3 = 0

            janela.blit(pygame.transform.flip(minhoca2, monstro_flip, False),(3210 - scroll[0], 2165 - scroll[1] - 15))
            monstro_rect9_dano = minhoca_rect_dano.get_rect()
            monstro_rect9_dano.x = 3248
            monstro_rect9_dano.y = 2203
            if minhoca_action2 == 'atacando':
                monstro_rect9 = minhoca_rect.get_rect()
                monstro_rect9.x = 3210 + movimento_monstro9
                monstro_rect9.y = 2203
                pygame.draw.rect(janela, (255, 255, 255), monstro_rect9)
                if player_rect.colliderect(monstro_rect9) and contador_hit >= 50 and bater == False and game_over == False and morreu9 == False:
                    bater_monstro9 = True
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
            if player_rect.colliderect(monstro_rect9_dano) and contador_hit >= 100 and bater == True and bater_monstro9 == False:
                contador9 = 1
                morreu9 = True
                minhoca_action2, minhoca_frame2 = chance_action_monstro(minhoca_action2, minhoca_frame2,'hit')
                if contadormonstromorte9 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte9 = 1
            if morreu9 == True:
                contadorM9 += 1
                if contadorM9 == 8:
                    if somrodando == True:
                        Somminhoca.play()
                if contadorM9 >= 30:
                    monstro_death_9 = True
            if bater_monstro9 == True:
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro9 = False

        # Ataque e perda de vida do Monstro 10
        if monstro_death_10 == False:
            if contadormonstro10 != 1:
                num_monstros += 1
                contadormonstro10 = 1

            if contador10 == 0 and bater_monstro10 == False and contadormin4 <= 70:
                minhoca_action3, minhoca_frame3 = chance_action_monstro(minhoca_action3, minhoca_frame3,'parado')
            if contador10 == 0 and bater_monstro10 == False and contadormin4 > 70:
                minhoca_action3, minhoca_frame3 = chance_action_monstro(minhoca_action3, minhoca_frame3,'atacando')
                tiroesq3 = True
            if contador10 == 0 and bater_monstro10 == False and contadormin4 > 83:
                contadormin4 = 0

            janela.blit(pygame.transform.flip(minhoca3, monstro_flip, False),(2490 - scroll[0], 2165 - scroll[1] - 15))
            monstro_rect10_dano = minhoca_rect_dano.get_rect()
            monstro_rect10_dano.x = 2528
            monstro_rect10_dano.y = 2203
            if minhoca_action3 == 'atacando':
                monstro_rect10 = minhoca_rect.get_rect()
                monstro_rect10.x = 2490 + movimento_monstro10
                monstro_rect10.y = 2203
                pygame.draw.rect(janela, (255, 255, 255), monstro_rect10)
                if player_rect.colliderect(monstro_rect10) and contador_hit >= 50 and bater == False and game_over == False and morreu7 == False:
                    bater_monstro10 = True
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
            if player_rect.colliderect(monstro_rect10_dano) and contador_hit >= 100 and bater == True and bater_monstro10 == False:
                contador10 = 1
                morreu10 = True
                minhoca_action3, minhoca_frame3 = chance_action_monstro(minhoca_action3, minhoca_frame3,'hit')
                if contadormonstromorte10 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte10 = 1
            if morreu10 == True:
                contadorM10 += 1
                if contadorM10 == 8:
                    if somrodando == True:
                        Somminhoca.play()
                if contadorM10 >= 30:
                    monstro_death_10 = True
            if bater_monstro10 == True:
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro10 = False

        # Ataque e perda de vida do Monstro 11
        if monstro_death_11 == False:
            if contadormonstro11 != 1:
                num_monstros += 1
                contadormonstro11 = 1
            if contador11 == 0 and bater_monstro11 == False:
                cobra_action1, cobra_frame1 = chance_action_monstro(cobra_action1, cobra_frame1,'parado')
            janela.blit(pygame.transform.flip(cobra1,monstro_flip_cobra,False),(2840 - scroll[0] + movimento_monstro11, 370 - scroll[1] - 15))
            monstro_rect11 = cobra1.get_rect()
            monstro_rect11.x = 2840 + movimento_monstro11
            monstro_rect11.y = 370

            if -500 <= player_rect.x - monstro_rect11.x <= 0 and player_rect.y + 20 == monstro_rect11.y:
                movimento_monstro11 -= 3
                monstro_flip_cobra = True
            if 500 >= player_rect.x - monstro_rect11.x > 0 and player_rect.y + 20 == monstro_rect11.y:
                movimento_monstro11 += 3
                monstro_flip_cobra = False
            if player_rect.colliderect(monstro_rect11) and contador_hit >= 100 and bater == False and game_over == False and morreu0 == False:
                bater_monstro11 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect11) and contador_hit >= 100 and bater == True and bater_monstro11 == False:
                contador11 = 1
                morreu11 = True
                cobra_action1, cobra_frame1 = chance_action_monstro(cobra_action1, cobra_frame1,'hit')

                if contadormonstromorte11 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte11 = 1
            if morreu11 == True:
                contadorM11 += 1
                if contadorM11 == 8:
                    if somrodando == True:
                        Somcobra.play()
                if contadorM11 >= 10:
                    monstro_death_11 = True

            if bater_monstro11 == True:
                cobra_action1, cobra_frame1 = chance_action_monstro(cobra_action1, cobra_frame1,'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro11 = False
        # Ataque e perda de vida do Monstro 12
        if monstro_death_12 == False:
            if contadormonstro12 != 1:
                num_monstros += 1
                contadormonstro12 = 1
            if contador12 == 0 and bater_monstro12 == False:
                cobra_action2, cobra_frame2 = chance_action_monstro(cobra_action2, cobra_frame2, 'parado')
            janela.blit(pygame.transform.flip(cobra2, monstro_flip_cobra, False),(3040- scroll[0] + movimento_monstro12, 920 - scroll[1] - 15))
            monstro_rect12 = cobra2.get_rect()
            monstro_rect12.x = 3040 + movimento_monstro12
            monstro_rect12.y = 920

            if -500 <= player_rect.x - monstro_rect12.x <= 0 and player_rect.y + 20 == monstro_rect12.y:
                movimento_monstro12 -= 3
                monstro_flip_cobra = True
            if 500 >= player_rect.x - monstro_rect12.x > 0 and player_rect.y + 20 == monstro_rect12.y:
                movimento_monstro12 += 3
                monstro_flip_cobra = False
            if player_rect.colliderect(monstro_rect12) and contador_hit >= 100 and bater == False and game_over == False and morreu0 == False:
                bater_monstro12 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect12) and contador_hit >= 100 and bater == True and bater_monstro11 == False:
                contador12 = 1
                morreu12 = True
                cobra_action2, cobra_frame2 = chance_action_monstro(cobra_action2, cobra_frame2, 'hit')

                if contadormonstromorte12 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte12 = 1
            if morreu12 == True:
                contadorM12 += 1
                if contadorM12 == 8:
                    if somrodando == True:
                        Somcobra.play()
                if contadorM12 >= 10:
                    monstro_death_12 = True

            if bater_monstro12 == True:
                cobra_action2, cobra_frame2 = chance_action_monstro(cobra_action2, cobra_frame2, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro12 = False

        # Ataque e perda de vida do Monstro 13
        if monstro_death_13 == False:
            if contadormonstro13 != 1:
                num_monstros += 1
                contadormonstro13 = 1
            if contador13 == 0 and bater_monstro13 == False:
                cobra_action3, cobra_frame3 = chance_action_monstro(cobra_action3, cobra_frame3,'parado')
            janela.blit(pygame.transform.flip(cobra3, monstro_flip_cobra, False),(910 - scroll[0] + movimento_monstro13, 770 - scroll[1] - 15))
            monstro_rect13 = cobra1.get_rect()
            monstro_rect13.x = 910 + movimento_monstro13
            monstro_rect13.y = 770

            if -500 <= player_rect.x - monstro_rect13.x <= 0 and player_rect.y + 20 == monstro_rect13.y:
                movimento_monstro13 -= 3
                monstro_flip_cobra = True
            if 500 >= player_rect.x - monstro_rect13.x > 0 and player_rect.y + 20 == monstro_rect13.y:
                movimento_monstro13 += 3
                monstro_flip_cobra = False
            if player_rect.colliderect(monstro_rect13) and contador_hit >= 100 and bater == False and game_over == False and morreu0 == False:
                bater_monstro13 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect13) and contador_hit >= 100 and bater == True and bater_monstro13 == False:
                contador13 = 1
                morreu13 = True
                cobra_action3, cobra_frame3 = chance_action_monstro(cobra_action3, cobra_frame3, 'hit')

                if contadormonstromorte13 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte13 = 1
            if morreu13 == True:
                contadorM13 += 1
                if contadorM13 == 8:
                    if somrodando == True:
                        Somcobra.play()
                if contadorM13 >= 10:
                    monstro_death_13 = True

            if bater_monstro13 == True:
                cobra_action3, cobra_frame3 = chance_action_monstro(cobra_action3, cobra_frame3,'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro13 = False
        # Ataque e perda de vida do Monstro 14
        if monstro_death_14 == False:
            if contadormonstro14 != 1:
                num_monstros += 1
                contadormonstro14 = 1
            if contador14 == 0 and bater_monstro14 == False:
                cobra_action4, cobra_frame4 = chance_action_monstro(cobra_action4, cobra_frame4, 'parado')
            janela.blit(pygame.transform.flip(cobra4, monstro_flip_cobra, False),(3070 - scroll[0] + movimento_monstro14, 1220 - scroll[1] - 15))
            monstro_rect14 = cobra1.get_rect()
            monstro_rect14.x = 3070 + movimento_monstro14
            monstro_rect14.y = 1220
            if -500 <= player_rect.x - monstro_rect14.x <= 0 and player_rect.y + 20 == monstro_rect14.y:
                movimento_monstro14 -= 3
                monstro_flip_cobra = True
            if 500 >= player_rect.x - monstro_rect14.x > 0 and player_rect.y + 20 == monstro_rect14.y:
                movimento_monstro14 += 3
                monstro_flip_cobra = False
            if player_rect.colliderect(monstro_rect14) and contador_hit >= 100 and bater == False and game_over == False and morreu0 == False:
                bater_monstro14 = True
                tomar_hit = True
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect14) and contador_hit >= 100 and bater == True and bater_monstro14 == False:
                contador14 = 1
                morreu14 = True
                cobra_action4, cobra_frame4 = chance_action_monstro(cobra_action4, cobra_frame4, 'hit')

                if contadormonstromorte14 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte14 = 1
            if morreu14 == True:
                contadorM14 += 1
                if contadorM14 == 8:
                    if somrodando == True:
                        Somcobra.play()
                if contadorM14 >= 10:
                    monstro_death_14 = True

            if bater_monstro14 == True:
                cobra_action4, cobra_frame4 = chance_action_monstro(cobra_action4, cobra_frame4, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro14 = False
        # Ataque e perda de vida do Monstro 15
        if monstro_death_15 == False:
            if 1650 <= player_rect.x <= 1990 and player_rect.y == 2300:
                mixer.music.unload()
                mixer.music.load("bossfight.mp3")
                mixer.music.play(-1)
            if contadormonstro15 != 1:
                num_monstros += 1
                contadormonstro15 = 1
            contador15 += 1
            if 0 < contador15 <= 200 and bater_monstro15 == False and morreu15 == False:
                boss_action, boss_frame = chance_action_monstro(boss_action, boss_frame, 'andando')
            if 200 <contador15 <= 300 and bater_monstro15 == False and morreu15 == False:
                boss_action, boss_frame = chance_action_monstro(boss_action, boss_frame, 'atirando')
                contadorboss += 1
                if contadorboss >= 100:
                    contador15 = 1
                    contadorboss = 0
            if 3200 <= player_rect.x <= 4700 and 2350 <= player_rect.y <= 2550:
                janela.blit(nome_boss, (280, 520))
                janela.blit(barra_hp_boss, (300, 570))
                x = 330
                for vida in listavidaboss:
                    janela.blit(vida, (x, 570))
                    x += 22

            janela.blit(pygame.transform.flip(boss, monstro_flip_cobra, False), (4200 - scroll[0] + movimento_monstro15, 2510 - scroll[1] - 15))
            monstro_rect15 = boss_rect.get_rect()
            monstro_rect15.x = 4350 + movimento_monstro15
            monstro_rect15.y = 2550
            print(player_rect.x)
            print(monstro_rect15.x)
            print(player_rect.y)
            print(monstro_rect15.y)
            #pygame.draw.rect(janela,(255,255,255,255),player_rect,2)
            #pygame.draw.rect(janela, (255, 255, 255, 255), monstro_rect15, 2)
            if boss_action == 'andando':
                if  player_rect.x - monstro_rect15.x <= 0 and player_rect.y == monstro_rect15.y:
                    movimento_monstro15 -= 3
                    monstro_flip_cobra = False
                if player_rect.x - monstro_rect15.x > 0 and player_rect.y == monstro_rect15.y:
                    movimento_monstro15 += 3
                    monstro_flip_cobra = True
                if player_rect.colliderect(monstro_rect15) and contador_hit >= 100 and bater == False and game_over == False and morreu0 == False:
                    bater_monstro15 = True
                    tomar_hit = True
                    vidas -= 1
                    listavida.pop(-1)
                    contador_hit = 0
                    if somrodando == True:
                        Somdano.play()
            contadorhitboss += 1
            if boss_action == 'atirando' and len(listavidaboss) > 0:
                if player_rect.colliderect(monstro_rect15) and contador_hit >= 100 and bater == True and bater_monstro15 == False and contadorhitboss >= 20:
                    listavidaboss.pop(-1)
                    boss_action, boss_frame = chance_action_monstro(boss_action, boss_frame, 'hit')
                    contadorhitboss = 0
            if len(listavidaboss) == 0:
                boss_action, boss_frame = chance_action_monstro(boss_action, boss_frame, 'morrendo')
                morreu15 = True
                if contadormonstromorte15 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte15 = 1

            if morreu15 == True:
                contadorM15 += 1
                if contadorM15 == 8:
                    if somrodando == True:
                        Somcobra.play()
                if contadorM15 >= 15:
                    monstro_death_15 = True

            if bater_monstro15 == True:
                boss_action, boss_frame = chance_action_monstro(boss_action, boss_frame, 'atacando')
                contadorbater_monstro += 1
                if contadorbater_monstro >= 10:
                    contadorbater_monstro = 0
                    bater_monstro15 = False
                if contadorbater_monstro == 5:
                    Somporradaboss.play()
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
        if contador_2 < 70:
            contador_2 += 1
            if contador7 == 0:
                movimento_monstro7 = 72
            if contador8 == 0:
                movimento_monstro8 = 72
            if contador9 == 0:
                movimento_monstro9 = 72
            if contador10 == 0:
                movimento_monstro10 = 72
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
        if contador_2 >= 70:
            contador_2 += 1
            if contador7 == 0:
                movimento_monstro7 = -20
            if contador8 == 0:
                movimento_monstro8 = -20
            if contador9 == 0:
                movimento_monstro9 = -20
            if contador10 == 0:
                movimento_monstro10 = -20
            monstro_flip = True
        if contador == 200:
            contador = 0
        if contador_2 == 140:
            contador_2 = 0

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
                            state = "Fase2"
                            return state,listavida
                        if zx >= 600 and zx <= 800 and zy >= 550 and zy <= 650:
                            state = "Menu"
                            mixer.music.unload()
                            mixer.music.load("musicamenu.mp3")
                            mixer.music.play(-1)
                            mixer.music.set_volume(0.5)
                            return state,listavida

                pygame.display.update()
        # Desenha portão
        if num_monstros_mortos == 16:
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
                    if event.key == K_v:
                        if tempo_no_ar < 6:
                            movimento_vertical = -18
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
                            print(somrodando, musicarodando)
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
                                        return state,listavida

                                    if mx >= 360 and mx <= 860 and my >= 360 and my <= 460:
                                        state = "Fase1"
                                        return state,listavida

                                    if mx >= 360 and mx <= 860 and my >= 110 and my <= 210:
                                        varpause = False
                            pygame.display.update()
        clock.tick(300)
        pygame.display.update()

