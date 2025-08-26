import pygame, sys

from player import Player

pygame.init()
pygame.joystick.init()

class Game:
    def __init__(self, windowSize: tuple):
        self.window = pygame.display.set_mode(windowSize)
        self.surface = pygame.surface.Surface((windowSize[0] / 2, windowSize[1] / 2))
        self.clock = pygame.time.Clock()
        self.deltaTime = 0
    
    def Run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Close()
                
                if event.type == pygame.JOYBUTTONDOWN:
                    print(event.button, event.joy)
            
            self.deltaTime = self.clock.tick(60) / 1000

            self.window.fill((0, 0, 0))
            self.surface.fill((0, 0, 0))

            for joystick in joysticks:
                directionX = pygame.joystick.Joystick(joystick.get_id()).get_axis(0)
                if abs(directionX) > 0.2:
                    players[joystick.get_id()].velocity.x = directionX

            for sprite in renderOrder:
                sprite.Update()
                self.surface.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
            
            self.window.blit(pygame.transform.scale(self.surface, self.window.get_size()), (0, 0))
            pygame.display.update()

    @staticmethod
    def Close():
        pygame.quit()
        sys.exit()

joysticks = []
for index in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(index)
    joystick.init()
    joysticks.append(joystick)

players = []
for index in range(len(joysticks)):
    player = Player(pygame.Vector2(0, 0), 2)
    players.append(player)

renderOrder = []
for player in players:
    renderOrder.append(player)

game = Game((600, 400))
game.Run()
