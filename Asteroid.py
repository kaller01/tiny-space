from particle import Particle
import pygame
from pygame import surface
from pygame.locals import *
vector = pygame.math.Vector2

class Asteroid(Particle):
    def __init__(self,position,radius) -> None:
        super().__init__()
        self.positon = position
        self.radius = radius
        self.surface = pygame.Surface([radius*2,radius*2], pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y= int(self.positon.x-self.radius), int(self.positon.y+self.radius)
        self.draw()
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.surface

    def __repr__(self):
        return "Asteroid"

    def get_rect(self):
        return self.rect

    def get_sprite(self):
        pass

    def get_surface(self):
        return self.surface

    def update(self,dt):
       super().update(dt)
       #pass
    
    #def addForce(self, force):
        #pass

    def draw(self):
        pygame.draw.rect(self.surface, (255, 255, 255), (self.radius,self.radius,self.radius,self.radius))