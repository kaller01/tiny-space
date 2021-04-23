import pygame

vector = pygame.math.Vector2

class Particle:
    def __init__(self) -> None:
        # Physics
        self.positon = vector(0,0)
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)
        self.force = vector(0,0)
        self.mass = 1
        #Display

    def update(self,dt):
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        self.positon += self.velocity * dt
        self.force = vector(0,0)
        self.rect.x, self.rect.y= int(self.positon.x), int(self.positon.y)

    def addForce(self,force):
        self.force += force
        

    def get_surface():
        pass
    
    def get_rect():
        pass

    def draw():
        pass