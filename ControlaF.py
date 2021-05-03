import pygame
from pygame import mixer
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random
import Menu
import Fase1Teste
import menucontroles
import Historia
import Fase1
import Creditos
import Tela_Morte

state = "Menu"

def controla_Fase(state):

    if state == "Menu":
        state = Menu.Menu("Menu")

    if state == "menucontroles":
        state = menucontroles.menucontroles("menucontroles")

    if state == "creditos":
        state = Creditos.Creditos("creditos")

    if state == "Historia":
        state = Historia.Historia("Historia")

    if state == "Fase1":
        Fase1.Fase1("Fase1")

    if state == "Tela_Morte":
        Tela_Morte.Tela_Morte("Tela_Morte")

run = True

while run:
    controla_Fase(state)


