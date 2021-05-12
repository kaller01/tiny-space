import pygame
import math

def renderScore(surface,score):
    # DRAW SCORE
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)
    # create a text suface object,
    # on which text is drawn on it.
    scoreString = str(math.floor(score))
    text = font.render('SCORE: ' + scoreString, True, green, blue)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    # X, Y relative to surface
    textRect.bottomleft = (100, 50)
    surface.blit(text, textRect)

    