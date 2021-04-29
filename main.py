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

screen = pygame.display.set_mode([WIDTH, HEIGHT])
game = pygame.Surface([WIDTH,HEIGHT])
SpaceEngine = Engine(game,camera)
particles = ParticleManager(SpaceEngine)
particles.addPlayer(rocket)
particles.generatePlanets()

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

    rocket.set_keys(pressed_keys)
    
    particles.update(dt)

    particles.checkCollision() 

    camera.scroll()
    particles.draw()

    pygame.display.flip()

    clock.tick(FPS)