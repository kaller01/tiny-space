from ParticleManager import ParticleManager
import pygame
from player import Player
from camera import Camera, Follow, Static
from engine import Engine
from Planet import Planet
from effect import Effect
from config import *
from pygame.locals import *
clock = pygame.time.Clock()
vector = pygame.math.Vector2

PLAYER = True

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
if PLAYER:
    particles.addPlayer(rocket)

p1 = Planet(vector(-200,300),100,10**7)
p2 = Planet(vector(300,100),100,10**7)
e = Effect(vector(100,100),vector(10,0))

particles.addParticle(p1)
particles.addParticle(p2)
particles.addParticle(e)

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

    camera.scroll()

    pygame.display.flip()

    clock.tick(FPS)