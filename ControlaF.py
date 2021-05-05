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

<<<<<<< HEAD
state = "Menu"
=======
state = "Fase2"
>>>>>>> 970dcec87e87eb889eb0d3ca700ba75a29dbe00a

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
        state = Fase1.Fase1("Fase1")

    elif state == "Fase2":
        state = Fase2.Fase2("Fase2")