from ParticleManager import ParticleManager
import pygame
from player import Player
from camera import Camera, Follow, Static
from engine import Engine
from Planet import Planet
from config import *
from pygame.locals import *
clock = pygame.time.Clock()
vector = pygame.math.Vector2

rocket = Player()
camera = Camera(rocket)
follow = Follow(camera,rocket)
static = Static(camera,rocket)

camera.setmethod(follow)

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT+200])
game = pygame.Surface([WIDTH,HEIGHT])
SpaceEngine = Engine(game,camera)
particles = ParticleManager(SpaceEngine)
particles.addPlayer(rocket)
particles.generatePlanets()

score = 0

running = True
while running:

    pressed_keys = pygame.key.get_pressed()
    

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if(pressed_keys[K_F1]):
        camera.setmethod(static)
    if(pressed_keys[K_F2]):
        camera.setmethod(follow)


    # Fill the background with white
    screen.fill((255))
    screen.blit(game,(0,0))
    game.fill((0, 0, 0))

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
    scoreString = str(score)
    text = font.render('SCORE: ' + scoreString, True, green, blue)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    textRect.bottomleft = (WIDTH//4 - 100, HEIGHT//4 + 650)
    screen.blit(text, textRect)
    #

    rocket.set_keys(pressed_keys)
    
    particles.update(dt)

    if rocket.velocity.length() >= 10:
        score += 0.001*rocket.velocity.length()
    print(rocket.velocity.length(), "length")
    print(score, "score")
    # particles.checkCollision() 

    camera.scroll()
    # particles.draw()

    pygame.display.flip()

    clock.tick(FPS)