import pygame
import config
vector = pygame.math.Vector2
from abc import ABC, abstractmethod

class Camera:
    def __init__(self, player):
        self.player = player
        self.offset = vector(0,0)
        self.offset_float = vector(0,0)
        self.DISPLAY_W, self.DISPLAY_H = config.WIDTH,config.HEIGHT
        self.CONST = vector(-self.DISPLAY_W / 2 + player.rect.w / 2, -self.DISPLAY_H / 2 + player.rect.w / 2)

    def setmethod(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()

class CameraScroll(ABC):
    def __init__(self, camera, player):
        self.camera = camera
        self.player = player

    @abstractmethod
    def scroll(self):
        pass

class Follow(CameraScroll):
    def __init__(self,camera,player):
        CameraScroll.__init__(self,camera,player)
        # super().__init__(camera,player)

    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)

class Static(CameraScroll):
    def __init__(self, camera, player):
        CameraScroll.__init__(self, camera, player)

    def scroll(self):
        pass

class Border(CameraScroll):
    def __init__(self, camera, player):
        CameraScroll.__init__(self, camera, player)

    def scroll(self):
        pass