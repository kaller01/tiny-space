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
        self.surface = pygame.Surface([20,70], pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.angle = 0
        self.thrusterForce = 60
        self.thruster = False

    def draw(self):
        surface = self.surface
        width = 20
        height = 60
        pygame.draw.ellipse(surface, (255, 255, 255), (surface.get_width()/2-width/2, surface.get_height()/2-height/2, width, height))
        pygame.draw.ellipse(surface, (255, 0, 0), (surface.get_width()/2-width/2, surface.get_height()/2+height-width/4-height/2, width, width/2))
        pygame.draw.rect(surface, (255, 255, 255), (surface.get_width()/2-width/2, surface.get_height()/2+height-width-height/2, width, width))
        pygame.draw.ellipse(surface, (0, 0, 255), (surface.get_width()/2-width/6, surface.get_height()/2-width/6, width/3, width/3))

    def get_surface(self):
        return pygame.transform.rotozoom(self.surface, self.angle-90,1)

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
            force.y = -force.y
            self.addForce(force)

        super().update(dt)
        self.draw()
        print(self.rect)
        