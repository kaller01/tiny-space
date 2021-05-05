from particle import Particle
import pygame
from pygame import surface
from pygame.locals import *
vector = pygame.math.Vector2


# Should maybe be called rocket
# Extends Particle
class Player(Particle):
    def __init__ (self):
        super().__init__()
        self.width = 60
        self.height = 30
        self.surface = pygame.Surface([30,60], pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.mass = 1
        self.angle = 0
        self.thrusterForce = 60
        self.thruster = False
        

    def __repr__(self):
        return "Player"

    def draw(self):
        surface = self.surface
        width = 20
        height = 60
        # pygame.draw.circle(self.surface, (255, 0, 0), (self.width/2,self.height/2),self.width/2)
        # pygame.draw.circle(self.surface, (0,255,0),(self.width,self.height/2),10)
        alpha = 100
        pygame.draw.ellipse(surface, (255, 255, 255,alpha), (surface.get_width()/2-width/2, surface.get_height()/2-height/2, width, height))
        pygame.draw.ellipse(surface, (255, 0, 0,alpha), (surface.get_width()/2-width/2, surface.get_height()/2+height-width/4-height/2, width, width/2))
        pygame.draw.rect(surface, (255, 255, 255,alpha), (surface.get_width()/2-width/2, surface.get_height()/2+height-width-height/2, width, width))
        pygame.draw.ellipse(surface, (0, 0, 255,alpha), (surface.get_width()/2-width/6, surface.get_height()/2-width/6, width/3, width/3))

    def get_surface(self):
        return pygame.transform.rotozoom(self.surface, self.angle,1)
        # return self.surface

    def get_rect(self):
        return self.rect

    def set_keys(self, keys):
        self.keys = keys

        if self.keys[K_UP]:
            self.thruster = True
        else:
            self.thruster = False

        if self.keys[K_LEFT]:
            self.angle+=2
        elif self.keys[K_RIGHT]:
            self.angle-=2

    def update(self, dt):
        if self.thruster:
            force = vector(self.thrusterForce,0)
            force.rotate_ip(self.angle)
            self.addForce(force)

        # print("Rocket",self.force)
        super().update(dt)
        self.draw()
        # print("Rocket angle",self.angle)
        # print(self.positon)
       

        