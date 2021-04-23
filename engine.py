import pygame
from camera import Camera

# Engine is mostly for compensating for camera
class Engine():
    def __init__(self,surface, camera) -> None:
        self.surface = surface
        self.camera = camera

    def draw(self, object, rect):
        # Compensate for camera
        self.surface.blit(object,(rect.x - self.camera.offset.x, rect.y - self.camera.offset.y))

