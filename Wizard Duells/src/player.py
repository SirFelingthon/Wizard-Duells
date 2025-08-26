import pygame

from sprite import Sprite

class Player(Sprite):
    def __init__(self, position: pygame.Vector2, speed: int):
        super().__init__("assets/player.png", [1, 1], position, pygame.Vector2(0, 0), speed)

        self.health = 100
        self.mana = 100
    
    def Update(self):
        super().Update()

        self.velocity = pygame.Vector2(0, 0)
