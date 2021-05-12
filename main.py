from ParticleManager import ParticleManager
import pygame
from player import Player
from camera import Camera, Follow, Static
from engine import Engine
from Planet import Planet
from config import *
import math
from pygame.locals import *
from score import renderScore
clock = pygame.time.Clock()
vector = pygame.math.Vector2

rocket = Player()
camera = Camera(rocket)
follow = Follow(camera,rocket)
static = Static(camera,rocket)

camera.setmethod(follow)

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT+100])
game = pygame.Surface([WIDTH,HEIGHT])
ux = pygame.Surface([WIDTH,100])
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
    ux.fill((255))
    screen.blit(game,(0,0))
    game.fill((0, 0, 0))

    renderScore(ux,score)
    
    rocket.set_keys(pressed_keys)
    
    particles.update(dt)

    # Calculate score
    if rocket.velocity.length() >= 10:
        score += 0.0001*rocket.velocity.length()

    if particles.collisionWithPlayer:
        font = pygame.font.Font(None,144)
        s = math.ceil(score)
        text = "GAME OVER"
        text2 = "YOUR SCORE: " + str(s)
        text_surface = font.render(text, True, (255,255,55))
        screen.blit(text_surface,((WIDTH/2),HEIGHT/2))

        text_surface = font.render(text2, True, (255,255,55))
        screen.blit(text_surface,((WIDTH/2),HEIGHT*0.7))
        # spelet ska resetta efter detta

    camera.scroll()
    screen.blit(ux,(0,HEIGHT))

    pygame.display.flip()

    clock.tick(FPS)