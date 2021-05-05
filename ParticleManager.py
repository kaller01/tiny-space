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
        self.G = 0.1
        self.collisionWithPlayer = False

    def addParticle(self,particle):
        self.particles.append(particle)

    def addPlayer(self,particle):
        self.player = particle
        self.addParticle(particle)
        #lägga in rocket i particles? tills senare

    def checkCollision(self, planet):
            # print(planet)
        if not planet.__repr__() == "Player": 
            if self.getDistance(self.player.positon,planet.positon) <= planet.radius**2:
                self.player.velocity = vector(0,0)
                return True
        return False
    def update(self,dt):
        self.collisionWithPlayer = False
        for particle in self.particles:
            # print("Inframe", self.engine.camera.inframe(particle.positon))
            if not self.engine.camera.inframe(particle.positon):
                continue
            self.gravity(particle)
            particle.update(dt)
            if self.checkCollision(particle):
                self.collisionWithPlayer = True
            self.engine.draw(particle.get_surface(),particle.get_rect())
            self.engine.debug(particle.positon)

    def gravity(self,p1):
        if p1.__repr__() != "Planet":
            for p2 in self.particles:
                distance_squared = self.getDistance(p1.positon,p2.positon)
                if(p1 == p2 or p2.__repr__() == "Effect"):
                    continue
                angle = self.getAngle(p1.positon,p2.positon)
                
                # angle += 180 # return
                # print("Vinkel",angle)
                # print("Dist",distance_squared)
                # angle += 90
                # print("Vinkel",angle)
                force = self.getForce(distance_squared,angle,p1,p2)
                # print("Force",force)
                p1.addForce(-force)                                 

    def getDistance(self,p1,p2):
        distance = p1.distance_squared_to(p2)
        # angle = p1.angle_to(p2)
        # print(angle)
        # The angle between 
        return distance

    def getAngle(self,p1,p2):
        x = p1.x - p2.x
        y = p1.y - p2.y
        angle = math.atan2(x,y)
        angle = math.degrees(angle)
        angle -= 90 # 0
        angle = -angle
        return angle




    def getForce(self,distance,angle,p1,p2):
        mass1 = p1.mass
        mass2 = p2.mass
        G = self.G

        rawForce = G*mass1*mass2 / (distance)
        force = vector(rawForce,0)
        force.rotate_ip((angle))
        # force.y = -force.y
        return force

    def generatePlanets(self):
        xAmount = 20
        yAmount = 20
        maxRadius = 400
        maxMass = 10**8
        factor = 1
        grid = 1200
        for x in range(-xAmount,xAmount):
            for y in range(-yAmount,yAmount):
                # print(x,y)
                value = (opensimplex.noise2d(x,y)+1)/2
                value **= factor
                if value >= 0.5:
                    radius = value * maxRadius
                    mass = value * maxMass
                    positon = vector(x*grid+maxRadius,y*grid+maxRadius)
                    planet = Planet(positon,radius,mass)
                    self.addParticle(planet)
