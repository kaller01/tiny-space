from opensimplex import OpenSimplex
opensimplex = OpenSimplex()
import pygame
from Planet import Planet
vector = pygame.math.Vector2
import math


class ParticleManager():
    def __init__(self,engine) -> None:
        self.engine = engine
        self.particles = []
        self.player = None

    def addParticle(self,particle):
        self.particles.append(particle)


    def addPlayer(self,particle):
        self.player = particle
        self.addParticle(particle)
        #lägga in rocket i particles? tills senare

    def checkCollision(self):
        for planet in self.particles:
            # print(planet)
            if planet.__repr__() == "Player":
                continue
            if self.getDistance(self.player,planet) <= planet.radius:
                # while True:
                print("crash")

    def update(self,dt):
        for particle in self.particles:
            particle.update(dt)

    def draw(self):
        for particle in self.particles:
            self.engine.draw(particle.get_surface(),particle.get_rect())


    def gravity(self):
        for p1 in self.particles:
            for p2 in self.particles:
                distance = self.getDistance(p1,p2)
                #                   #   mass2 = p2.mass             #   mass1 = p1.mass
                force = self.getForce(distance,p1,p2)
                p1.addForce(force)                                 
                p2.addForce(force)

    def getDistance(self,p1,p2):
        x1 = p1.positon.x
        x2 = p2.positon.x

        y1 = p1.positon.y
        y2 = p2.positon.y

        distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        #pos3 = vector(x2-x1,y2-y1)
        return distance

    def getForce(self,distance,p1,p2):
        mass1 = p1.mass
        return 0
        pass


    def generatePlanets(self):
        xAmount = 40
        yAmount = 40
        maxRadius = 500
        factor = 1
        grid = 1000
        for x in range(-xAmount,xAmount):
            for y in range(-yAmount,yAmount):
                print(x,y)
                value = (opensimplex.noise2d(x,y)+1)/2
                value **= factor
                if value >= 0.5:
                    radius = value * maxRadius
                    positon = vector(x*grid+maxRadius,y*grid+maxRadius)
                    planet = Planet(positon,radius)
                    self.addParticle(planet)
