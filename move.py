import pygame, sys
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from pygame import mixer
import random
import colisao_teste

pygame.init()
def move(rect, movement, tiles):
    tipos_de_colisao = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    colisao_lista = colisao_teste.colisao_teste(rect, tiles)
    for tile in colisao_lista:
        if movement[0] > 0:
            rect.right = tile.left
            tipos_de_colisao['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            tipos_de_colisao['left'] = True
    rect.y += movement[1]
    colisao_lista = colisao_teste.colisao_teste(rect, tiles)
    for tile in colisao_lista:
        if movement[1] > 0:
            rect.bottom = tile.top
            tipos_de_colisao['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            tipos_de_colisao['top'] = True

    return rect,tipos_de_colisao