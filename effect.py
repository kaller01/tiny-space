from particle import Particle
import pygame
from pygame import surface
from pygame.locals import *
vector = pygame.math.Vector2

class Effect(Particle):
    def __init__(self, positon, velocity,mass) -> None:
        super().__init__()
        self.mass = mass
        self.width = 2
        self.height = 2
        self.radius = self.width/2
        self.surface = pygame.Surface([self.width,self.height], pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.positon = positon
        self.velocity = velocity
        self.rect.x, self.rect.y= int(self.positon.x-self.radius), int(self.positon.y+self.radius)
        self.draw()
        self.timelimit = 1 # How long until the particle disappears
       
    def draw(self):
        pygame.draw.circle(self.surface, (200, 200, 255), (self.width/2,self.width/2),self.width/2)

    def __repr__(self):
        return "Effect"

    def get_rect(self):
        return self.rect

    def get_surface(self):
        return self.surface

    def update(self,dt):
        super().update(dt)
        self.timelimit -= dt

    def timeout(self):
        return self.timelimit < 0
        
