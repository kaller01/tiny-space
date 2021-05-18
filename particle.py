import pygame

vector = pygame.math.Vector2

class Particle:
    def __init__(self) -> None:
        # Physics
        self.positon = vector(0,0)
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)
        self.force = vector(0,0)
        self.mass = 10000
        self.width = 1
        self.height = 1
        #Display

    def update(self,dt):
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        self.positon += self.velocity * dt
        self.force = vector(0,0)
        self.rect.x, self.rect.y= int(self.positon.x-self.width), int(self.positon.y+self.height)

    def addForce(self,force):
        self.force += force

    def get_surface():
        pass
    
    def get_rect():
        pass
    

    def draw():
        pass

    def timeout():
        return False
      
    def draw(self):
        pygame.draw.circle(self.surface, (255, 255, 255), (self.radius,self.radius),self.radius, width = 4)
