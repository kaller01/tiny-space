from particle import Particle
import pygame
from pygame import surface
from pygame.locals import *
vector = pygame.math.Vector2

class Effect(Particle):
    def __init__(self, positon, velocity) -> None:
        super().__init__()
        self.mass = 1
        self.width = 4
        self.height = 4
        self.radius = self.width/2
        self.surface = pygame.Surface([self.width,self.height], pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.positon = positon
        self.velocity = velocity
        self.rect.x, self.rect.y= int(self.positon.x-self.radius), int(self.positon.y+self.radius)
        self.draw()
       
    def draw(self):
        pygame.draw.circle(self.surface, (255, 100, 100), (self.width/2,self.width/2),self.width/2, width = 4)

    def __repr__(self):
        return "Effect"

    def get_rect(self):
        return self.rect

    def get_surface(self):
        return self.surface

    def update(self,dt):
        super().update(dt)
        # We do not want to update the position of the planet