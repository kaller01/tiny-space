from effect import Effect
from particle import Particle
import pygame
from pygame import surface
from pygame.locals import *
vector = pygame.math.Vector2
import random


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
        self.thrusterForce = 400
        self.thruster = False
        self.vMax = 500 ** 2
        self.effects = list()
        

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
        return pygame.transform.rotozoom(self.surface, self.angle-90,1)
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
            self.angle+=3
        elif self.keys[K_RIGHT]:
            self.angle-=3

    def update(self, dt):
        if self.thruster:
            force = vector(self.thrusterForce,0)
            force.rotate_ip(self.angle)
            self.createEffect()
            self.addForce(force)

        # print("Rocket",self.force)
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        print(self.velocity.length())
        if(self.velocity.length_squared() > self.vMax):
            self.velocity.scale_to_length(self.vMax ** 0.5)
        self.positon += self.velocity * dt
        self.force = vector(0,0)
        self.rect.x, self.rect.y= int(self.positon.x-self.height/2), int(self.positon.y+self.width/2)
        self.draw()
        # print("Rocket angle",self.angle)
        # print(self.positon)
       

    def timeout(self):
        return False

    def getEffects(self):
        effects = self.effects
        self.effects = list()
        return effects

    def createEffect(self):
        v = vector(200,0)
        offset = ((random.random()*2)-1)*20
        v.rotate_ip(self.angle+180+offset)
        effect = Effect(vector(self.positon.x,self.positon.y), v)
        self.effects.append(effect)