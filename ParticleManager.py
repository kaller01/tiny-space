class ParticleManager():
    def __init__(self,engine) -> None:
        self.engine = engine
        self.particles = []

    def addParticle(self,particle):
        self.particles.append(particle)

    def update(self,dt):
        for particle in self.particles:
            particle.update(dt)

    def draw(self):
        for particle in self.particles:
            self.engine.draw(particle.get_surface(),particle.get_rect())