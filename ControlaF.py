import pygame
from pygame import mixer
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random
import Menu
import menucontroles
import Historia
import Fase1
import Creditos
import Fase2
import Fase3


state = "Fase2"

listavida = []
while True:

    if state == "Menu":
        state = Menu.Menu("Menu")

    elif state == "menucontroles":
        state = menucontroles.menucontroles("menucontroles")

    elif state == "creditos":
        state = Creditos.Creditos("creditos")

    elif state == "Historia":
        state = Historia.Historia("Historia")

    elif state == "Fase1":
        state,listavida = Fase1.Fase1("Fase1")

    elif state == "Fase2":
        state,listavida = Fase2.Fase2("Fase2",listavida)

    elif state == "Fase3":
        state,listavida = Fase3.Fase3("Fase3",listavida)