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
        self.thruster = False
        self.vMax = 1000 ** 2
        self.effects = list()
        self.angularAcc = 0
        self.angularVelocity = 0
        self.mainThrusterForce = 1000
        self.sideThrusterForce = 100
        

    def __repr__(self):
        return "Player"

    def draw(self):
        surface = self.surface
        width = 20
        height = 60
        # pygame.draw.circle(self.surface, (255, 0, 0), (self.width/2,self.height/2),self.width/2)
        # pygame.draw.circle(self.surface, (0,255,0),(self.width,self.height/2),10)
        alpha = 255
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

        

    def update(self, dt):
        if self.thruster:
            self.accelerate(1)
        
        if self.keys[K_LEFT]:
            self.rotate(-3)
        elif self.keys[K_RIGHT]:
            self.rotate(3)

        # print("Rocket",self.force)
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        self.angularVelocity += self.angularAcc * dt
        self.angle += self.angularVelocity * dt
        if(self.velocity.length_squared() > self.vMax):
            self.velocity.scale_to_length(self.vMax ** 0.5)
        self.positon += self.velocity * dt
        self.force = vector(0,0)
        self.angularAcc = 0
        self.rect = (self.get_surface()).get_rect(center=(30/2,60/2))
        self.rect.y = -self.rect.y
        self.rect.x += int(self.positon.x-self.height/2)
        self.rect.y += int(self.positon.y+self.width/2)
        self.draw()
        # print("Rocket angle",self.angle)
        # print(self.positon)
       

    def timeout(self):
        return False

    def getEffects(self):
        effects = self.effects
        self.effects = list()
        return effects

    def useThruster(self,value):
        dt = 1/60
        effectMass = 0.05
        force = self.mainThrusterForce*value
        acceleration = force / effectMass
        v = acceleration*dt
        offset = ((random.random()*2)-1)*20 # Random offset just to make it look more fun, no physics implementation of it
        self.createEffect(v,self.angle+180+offset,effectMass)
        offset = ((random.random()*2)-1)*20 # Random offset just to make it look more fun, no physics implementation of it
        self.createEffect(v,self.angle+180+offset,effectMass)
        offset = ((random.random()*2)-1)*20 # Random offset just to make it look more fun, no physics implementation of it
        self.createEffect(v,self.angle+180+offset,effectMass)
        offset = ((random.random()*2)-1)*20 # Random offset just to make it look more fun, no physics implementation of it
        self.createEffect(v,self.angle+180+offset,effectMass)
        offset = ((random.random()*2)-1)*20 # Random offset just to make it look more fun, no physics implementation of it
        self.createEffect(v,self.angle+180+offset,effectMass)
        offset = ((random.random()*2)-1)*20 # Random offset just to make it look more fun, no physics implementation of it
        self.createEffect(v,self.angle+180+offset,effectMass)
        offset = ((random.random()*2)-1)*20 # Random offset just to make it look more fun, no physics implementation of it
        self.createEffect(v,self.angle+180+offset,effectMass)
   
        return acceleration * effectMass

    def useThrusterSide(self,value):
        dt = 1/60
        effectMass = 0.01
        force = self.sideThrusterForce*value
        acceleration = force / effectMass
        v = acceleration * dt
        offset = ((random.random()*2)-1)*10 # Random offset just to make it look more fun, no physics implementation of it
        self.createEffect(v,self.angle+180+90+offset,effectMass)
        return acceleration * effectMass

    def createEffect(self,v,angle,effectMass):
        pos = vector(self.positon.x,self.positon.y)
        v = vector(v,0)
        v.rotate_ip(angle)
        v += self.velocity # Add rockets velocity
        length = vector(30,0)
        length.rotate_ip(self.angle+180)
        pos += length
        effect = Effect(pos, v, effectMass)
        self.effects.append(effect)

    def reset(self):
        self.positon = vector(0,0)
        self.velocity = vector(0,0)
        self.angularVelocity = 0
        self.angle = 0

    def accelerate(self,value):
        force = self.useThruster(value)
        force = vector(force,0)
        force.rotate_ip(self.angle)
        self.addForce(force)

    def rotate(self,value):
        self.angularAcc = -self.useThrusterSide(value)