import pygame
import random
import utils
utils = utils.Utils()
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/enemy.png")
        self.scale = 100
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 700)
        self.rect.y = random.randint(0, 500)
        self.speed = 4
        
        surface = pygame.display.get_surface()
        player = player
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self, player):
        playercoords = player.rect.center
        print(player.rect.x, " ", player.rect.y)
        movevec = [playercoords[0] - self.rect.center[0], playercoords[1] - self.rect.center[1]]
        movevec = (utils.normalize_vector(tuple(movevec))[0] * self.speed, utils.normalize_vector(tuple(movevec))[1] * self.speed)
        self.rect = self.rect.move(movevec)

