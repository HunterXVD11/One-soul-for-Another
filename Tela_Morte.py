import pygame, sys
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from pygame import mixer

def Tela_Morte(self):
    pygame.init()

    fontefrase = pygame.font.Font('freesansbold.ttf', 15)
    fontenome = pygame.font.Font('freesansbold.ttf', 10)
    clock = pygame.time.Clock()
    janela_largura = 1200
    janela_altura = 675
    janela = pygame.display.set_mode((janela_largura, janela_altura))
    pygame.display.set_caption('One soul for another')

    #load images
    arvore = pygame.image.load('arvoremorte.png')
    arvore = pygame.transform.scale(arvore,(600, 650))

    morte = pygame.image.load('Player_animations/Kaorimorrendo/Kaorimorrendo11.png')
    morte = pygame.transform.scale(morte,(130, 120))

    restart = pygame.image.load('recomecar_restart.png')
    restart = pygame.transform.scale(restart,(230, 109))

    voltar_menu = pygame.image.load('voltar_ao_menu_restart.png')
    voltar_menu = pygame.transform.scale(voltar_menu,(230, 109))

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
        return action_var,frame
    animation_database = {}

    animation_database['parada'] = load_animations('Morte_animations/Morteparada',[15,15,15])

    morte_action = 'idle'
    morte_frame = 0
    morte_flip = False

    textofrase = fontefrase.render("Ou se morre como herói, ou vive-se o bastante para se tornar o vilão.",True, (255, 255, 255))
    textonome = fontenome.render("Harvey Dent.",True, (255, 255, 255))

    while True:
        janela.fill((25, 33, 23))
        janela.blit(arvore, (300, -50))
        janela.blit(morte,(550,330))
        janela.blit(restart,(350,550))
        janela.blit(voltar_menu,(600,550))
        janela.blit(textofrase,(350,500))
        janela.blit(textonome,(760,530))

        morte_action, morte_frame = chance_action(morte_action, morte_frame, 'parada')

        morte_frame += 1
        if morte_frame >= len(animation_database[morte_action]):
            morte_frame = 0
        morte_image_id = animation_database[morte_action][morte_frame]
        morte_image = animation_frames[morte_image_id]

        janela.blit(pygame.transform.flip(morte_image, morte_flip, False),(470, 300))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()