import pygame

class Sprite:
    def __init__(self, sheet: str, frames: tuple, position: pygame.Vector2, velocity: pygame.Vector2, speed: int):
        self.sheet = pygame.image.load(sheet)
        self.frames = frames
        self.currentFrame = [0, 0]
        self.frameSize = (self.sheet.get_size()[0] / self.frames[0], self.sheet.get_size()[1] / self.frames[1])
        self.image = pygame.surface.Surface(self.frameSize)
        self.position = position
        self.velocity = velocity
        self.speed = speed
        self.rect = self.image.get_rect(center=self.position)
    
    def Update(self):
        self.image.blit(self.sheet, (0, 0), (self.frameSize[0] * self.currentFrame[0], self.frameSize[1] * self.currentFrame[1], self.frameSize[0], self.frameSize[1]))
        self.position += self.velocity * self.speed
        self.rect = self.image.get_rect(center=self.position)
