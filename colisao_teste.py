import pygame, sys
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from pygame import mixer
import random

pygame.init()

def colisao_teste(rect,tiles):
    colisao_lista = []
    for tile in tiles:
        if rect.colliderect(tile):
            colisao_lista.append(tile)
    return colisao_lista