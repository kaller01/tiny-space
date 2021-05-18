from particle import Particle
import pygame
from pygame import surface
from pygame.locals import *
vector = pygame.math.Vector2



class Planet(Particle):
    def __init__(self,position,radius,mass) -> None:
        super().__init__()
        self.positon = position
        self.radius = radius
        self.surface = pygame.Surface([radius*2,radius*2], pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y= int(self.positon.x-self.radius), int(self.positon.y+self.radius)
        self.mass = mass
        self.draw()
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.surface
        

    def __repr__(self):
        return "Planet"

    def get_rect(self):
        return self.rect

    def get_sprite(self):
        pass

    def get_surface(self):
        return self.surface

    def update(self,dt):
        #super().update(dt)
        pass
        # We do not want to update the position of the planet

    def draw(self):
        pygame.draw.circle(self.surface, (190, 60, 70), (self.radius,self.radius),self.radius)
        pygame.draw.circle(self.surface, (0,0,0), (self.radius,self.radius),self.radius, width = 4)
        font = pygame.font.Font(None,40)
        text = str(int(self.mass)) + " kg"
        text_surface = font.render(text, True, (255,255,255))
        self.surface.blit(text_surface,(self.radius/2,self.radius/2))

    def timeout(self):
        return False