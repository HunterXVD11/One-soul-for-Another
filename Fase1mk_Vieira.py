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

    player_rect = pygame.Rect(100, 400, 87, 100)
    cenario = pygame.image.load("cenario.png")
    tile_tamanho = 50

    #Musica
    mixer.music.load("musicafase1.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)

    # Sons
    pygame.mixer.init()
    Sompulo = pygame.mixer.Sound("jump.mp3")
    Somespada = pygame.mixer.Sound("espadada2.mp3")
    Somdano = pygame.mixer.Sound("Kaorimorrendo.mp3")

    #Load Images

    frase_portao = pygame.image.load('Corra_portao.png')
    frase_portao = pygame.transform.scale(frase_portao,(600, 102))

    pause_img = pygame.image.load("pauseimg.png")

    chao_padrao_img = pygame.image.load("chão padrão.png")

    chao_pedra1_img = pygame.image.load("chão pedra 1.jpg")

    chao_pedra2_img = pygame.image.load("chão pedra 2.jpg")

    monstro = pygame.image.load("olhovoador.png")
    monstro = pygame.transform.scale(monstro, (120,100))

    contador_monstro = pygame.image.load("contador_monstros.png")
    contador_monstro = pygame.transform.scale(contador_monstro, (95, 52))

    portao = pygame.image.load("Portao_fechado.png")
    portao = pygame.transform.scale(portao, (125, 157))

    vitoria = pygame.image.load("WIN.png")
    vitoria = pygame.transform.scale(vitoria, (500, 387))

    somrodando = True
    musicarodando = True
    movimento_direita = False
    movimento_esquerda = False
    monstro_flip = False
    bater = False
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
    movimento_monstro = 0
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

    for i in range(5):
        vida = pygame.image.load('Vida.png')
        listavida.append(vida)


    world_data = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,3,3,3,3,3,3,3,3,2,2,2,2,2,3,3,2,3,3,3,2,2,2,2,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,],
                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,3,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,],
                  [0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,3,2,2,2,2,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,],
                  [2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,3,2,2,2,2,2,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,],
                  [2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,2,2,2,2,2,2,3,3,2,2,2,3,2,2,2,3,2,2,3,3,3,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,],
                  [2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,3,2,3,2,2,2,2,3,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,],
                  [2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,3,2,2,2,2,2,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]]

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

    player_action = 'idle'
    player_frame = 0
    player_flip = True

    while True:
        true_scroll[0] += (player_rect.x - true_scroll[0] - 600) / 10
        true_scroll[1] += (player_rect.y - true_scroll[1] - 335) / 10
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        janela.fill((146,244,255))
        janela.blit(cenario,(0, 0))
        tile_rects = []

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
                bater_time[0] += 10
            if direction == 0:
                bater_time[0] -= 10

        if bater_time[0] > 0:
            player_action, player_frame = chance_action(player_action, player_frame, 'atacando')
            player_flip = False
        if bater_time[0] < 0:
            player_action, player_frame = chance_action(player_action, player_frame, 'atacando')
            player_flip = True
        if movimento_player[0] > 0 and bater == False:
            player_action,player_frame = chance_action(player_action,player_frame,'correndo')
            player_flip = False
        if movimento_player[0] == 0 and bater == False:
            player_action, player_frame = chance_action(player_action, player_frame, 'parada')
        if movimento_player[0] < 0 and bater == False:
            player_action,player_frame = chance_action(player_action,player_frame,'correndo')
            player_flip = True
        if tempo_no_ar > 40 and bater == False:
            player_action,player_frame = chance_action(player_action,player_frame,'caindo')
        if 3 < tempo_no_ar <= 40 and bater == False:
            player_action,player_frame = chance_action(player_action,player_frame,'pulando')

        player_rect, collisions = move.move(player_rect, movimento_player, tile_rects)

        if collisions['bottom'] == True:
            movimento_vertical = 0
            tempo_no_ar = 0
        else:
            tempo_no_ar += 1

        if collisions['top'] == True:
            movimento_vertical = 0

        contador_hit += 1
        #Ataque e perda de vida do Monstro 0
        if monstro_death_0 == False:
            if contadormonstro0 != 1:
                num_monstros += 1
                contadormonstro0 = 1
            janela.blit(pygame.transform.flip(monstro, monstro_flip, False), (1680 - scroll[0] + movimento_monstro, 275 - scroll[1] - 15))
            monstro_rect0 = monstro.get_rect()
            monstro_rect0.x = 1680 + movimento_monstro
            monstro_rect0.y = 275

            if player_rect.colliderect(monstro_rect0) and contador_hit >= 100 and bater == False:
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect0) and contador_hit >= 100 and bater == True:
                monstro_death_0 = True
                if contadormonstromorte0 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte0 = 0

        #Ataque e perda de vida do Monstro 1
        if monstro_death_1 == False:
            if contadormonstro1 != 1:
                num_monstros += 1
                contadormonstro1 = 1
            janela.blit(pygame.transform.flip(monstro, monstro_flip, False), (500 - scroll[0] + movimento_monstro, 425 - scroll[1] - 15))
            monstro_rect1 = monstro.get_rect()
            monstro_rect1.x = 500 + movimento_monstro
            monstro_rect1.y = 425

            if player_rect.colliderect(monstro_rect1) and contador_hit >= 100 and bater == False:
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect1) and contador_hit >= 100 and bater == True:
                monstro_death_1 = True
                if contadormonstromorte1 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte1 = 0

        # Ataque e perda de vida do Monstro 2
        if monstro_death_2 == False:
            if contadormonstro2 != 1:
                num_monstros += 1
                contadormonstro2 = 1
            janela.blit(pygame.transform.flip(monstro, monstro_flip, False), (1370 - scroll[0] + movimento_monstro, 425 - scroll[1] - 15))
            monstro_rect2 = monstro.get_rect()
            monstro_rect2.x = 1370 + movimento_monstro
            monstro_rect2.y = 425
            contador_hit += 1
            if player_rect.colliderect(monstro_rect2) and contador_hit >= 100 and bater == False:
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect2) and contador_hit >= 100 and bater == True:
                monstro_death_2 = True
                if contadormonstromorte2 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte2 = 0
        # Ataque e perda de vida do Monstro 3
        if monstro_death_3 == False:
            if contadormonstro3 != 1:
                num_monstros += 1
                contadormonstro3 = 1
            janela.blit(pygame.transform.flip(monstro, monstro_flip, False), (2060 - scroll[0] + movimento_monstro, 425 - scroll[1] - 15))
            monstro_rect3 = monstro.get_rect()
            monstro_rect3.x = 2060 + movimento_monstro
            monstro_rect3.y = 425

            if player_rect.colliderect(monstro_rect3) and contador_hit >= 100 and bater == False:
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect3) and contador_hit >= 100 and bater == True:
                monstro_death_3 = True
                if contadormonstromorte3 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte3 = 0
        # Ataque e perda de vida do Monstro 4
        if monstro_death_4 == False:
            if contadormonstro4 != 1:
                num_monstros += 1
                contadormonstro4 = 1
            janela.blit(pygame.transform.flip(monstro, monstro_flip, False), (4200 - scroll[0] + movimento_monstro, 325 - scroll[1] - 15))
            monstro_rect4 = monstro.get_rect()
            monstro_rect4.x = 4200 + movimento_monstro
            monstro_rect4.y = 325

            if player_rect.colliderect(monstro_rect4) and contador_hit >= 100 and bater == False:
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect4) and contador_hit >= 100 and bater == True:
                monstro_death_4 = True
                if contadormonstromorte4 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte4 = 0
        # Ataque e perda de vida do Monstro 5
        if monstro_death_5 == False:
            if contadormonstro5 != 1:
                num_monstros += 1
                contadormonstro5 = 1
            janela.blit(pygame.transform.flip(monstro, monstro_flip, False), (5100 - scroll[0] + movimento_monstro, 425 - scroll[1] - 15))
            monstro_rect5 = monstro.get_rect()
            monstro_rect5.x = 5100 + movimento_monstro
            monstro_rect5.y = 425

            if player_rect.colliderect(monstro_rect5) and contador_hit >= 100 and bater == False:
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect5) and contador_hit >= 100 and bater == True:
                monstro_death_5 = True
                if contadormonstromorte5 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte5 = 0
        # Ataque e perda de vida do Monstro 6
        if monstro_death_6 == False:
            if contadormonstro6 != 1:
                num_monstros += 1
                contadormonstro6 = 1
            janela.blit(pygame.transform.flip(monstro, monstro_flip, False), (6250 - scroll[0] + movimento_monstro, 425 - scroll[1] - 15))
            monstro_rect6 = monstro.get_rect()
            monstro_rect6.x = 6250 + movimento_monstro
            monstro_rect6.y = 425
            if player_rect.colliderect(monstro_rect6) and contador_hit >= 100 and bater == False:
                vidas -= 1
                listavida.pop(-1)
                contador_hit = 0
                if somrodando == True:
                    Somdano.play()
            if player_rect.colliderect(monstro_rect6) and contador_hit >= 100 and bater == True:
                monstro_death_6 = True
                if contadormonstromorte6 != 1:
                    num_monstros_mortos += 1
                    contadormonstromorte6 = 0

        if contador < 100:
            contador += 1
            movimento_monstro += 3
            monstro_flip = False
        if contador >= 100:
            contador += 1
            movimento_monstro -= 3
            monstro_flip = True
        if contador == 200:
            contador = 0

        player_frame += 1
        if player_frame >= len(animation_database[player_action]):
            player_frame = 0
        player_image_id = animation_database[player_action][player_frame]
        player_image = animation_frames[player_image_id]

        janela.blit(portao, (8013 - scroll[0], 350 - scroll[1]))
        janela.blit(pygame.transform.flip(player_image, player_flip, False),(player_rect.x - scroll[0], player_rect.y - scroll[1]))

        # Desenha portão
        if num_monstros_mortos == 7:
            janela.blit(frase_portao, (300, 20))
            portao = pygame.image.load('Portao_aberto.png')
            portao = pygame.transform.scale(portao, (125, 157))
            portao_rect = portao.get_rect()
            portao_rect.x = 8023
            portao_rect.y = 400
            if player_rect.colliderect(portao_rect):
                janela.blit(vitoria, (350, 200))

        print(player_rect.x)
        print(player_rect.y)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    movimento_direita = True
                if event.key == K_a:
                    movimento_esquerda = True
                if event.key == K_p :
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
                if event.key == K_p:
                    bater = False
                if event.key == K_l:
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
                                    pygame.display.update()
                                    somrodando = False

                                if somrodando == False and mx >= 765 and mx <= 835 and my >= 250 and my <= 420:
                                    pygame.display.update()
                                    somrodando = True

                                if mx >= 360 and mx <= 860 and my >= 480 and my <= 580:
                                    mixer.music.unload()
                                    mixer.music.load("musicamenu.mp3")
                                    mixer.music.play(-1)
                                    mixer.music.set_volume(0.5)
                                    state = "Menu"
                                    return state

                                # if mx >= 360 and mx <= 860 and my >= 360 and my <= 460:
                                # reiniciar fase

                                if mx >= 360 and mx <= 860 and my >= 110 and my <= 210:
                                    varpause = False
                            pygame.display.update()

        pygame.display.update()
        clock.tick(60)