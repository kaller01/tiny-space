from ParticleManager import ParticleManager
import pygame
from player import Player
from camera import Camera, Follow, Static
from engine import Engine
from Planet import Planet
from config import *
from pygame.locals import *
from score import renderScore
joystick = True
clock = pygame.time.Clock()
vector = pygame.math.Vector2

rocket = Player()
camera = Camera(rocket)
follow = Follow(camera,rocket)
static = Static(camera,rocket)

camera.setmethod(follow)

pygame.init()

if(joystick):
    pygame.joystick.init()
    _joystick = pygame.joystick.Joystick(0)
    _joystick.init()
    print (_joystick.get_init())
    print (_joystick.get_id())
    print (_joystick.get_name())
    print (_joystick.get_numaxes())
    print (_joystick.get_numballs())
    print (_joystick.get_numbuttons())
    print (_joystick.get_numhats())
    print (_joystick.get_axis(0))

screen = pygame.display.set_mode([WIDTH, HEIGHT+50])
game = pygame.Surface([WIDTH,HEIGHT])
ux = pygame.Surface([WIDTH,100])
SpaceEngine = Engine(game,camera)
particles = ParticleManager(SpaceEngine)
particles.addPlayer(rocket)
particles.generatePlanets()


score = 0

running = True
update = True

if(joystick):
    axes = [ 0.0 ] * _joystick.get_numaxes()
    buttons = [ False ] * _joystick.get_numbuttons()

while running:

    pressed_keys = pygame.key.get_pressed()
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif joystick and event.type == pygame.JOYAXISMOTION:
            e = event.dict
            axes[e['axis']] = e['value']
            
    if joystick:
        x,y,z,v = axes
        v = (-v+1)/2
        x 
        if(v > 0.1):
            rocket.accelerate(v)
        rocket.rotate(x*5)


    if(pressed_keys[K_F1]):
        camera.setmethod(static)
    if(pressed_keys[K_F2]):
        camera.setmethod(follow)


    # Fill the background with white
    ux.fill((255))
    screen.blit(game,(0,0))
    game.fill((0, 0, 30))

    renderScore(ux,score)
    
    rocket.set_keys(pressed_keys)
    if(update):
        particles.update(dt)

    # Calculate score
    if rocket.velocity.length() >= 10:
        score += 0.0001*rocket.velocity.length()

    if particles.collisionWithPlayer:
        font = pygame.font.Font(None,144)
        text = "GAME OVER"
        text_surface = font.render(text, True, (255,255,55))
        screen.blit(text_surface,((WIDTH/2),HEIGHT/2))
        #update = False
        rocket.reset()
        camera.setmethod(follow)
        print("SCORE: "+str(score))
        score = 0

        # spelet ska resetta efter detta

    camera.scroll()
    screen.blit(ux,(0,HEIGHT))

    pygame.display.flip()

    clock.tick(FPS)