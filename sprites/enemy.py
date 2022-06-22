import pygame
import random
import utils
utils = utils.Utils()
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, speed):
        super().__init__()

        surface = pygame.display.get_surface()
        self.image = pygame.image.load(r"assets/images/enemy.png")
        self.scale = 100
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = self.image.get_rect()
        width, height = surface.get_size()
        min_distance_from_player_on_spawn = 150
        self.rect.x = random.randint(0, width)
        self.rect.y = random.randint(0, height)
        while self.rect.x <= player.rect.x + min_distance_from_player_on_spawn and self.rect.x >= player.rect.x - min_distance_from_player_on_spawn: 
            self.rect.x = random.randint(0, width)
        while self.rect.y <= player.rect.y + min_distance_from_player_on_spawn and self.rect.y >= player.rect.y - min_distance_from_player_on_spawn:
            self.rect.y = random.randint(0, height)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        
        player = player
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self, player):
        playercoords = player.rect.center
        movevec = [playercoords[0] - self.rect.center[0], playercoords[1] - self.rect.center[1]]
        movevec = (utils.normalize_vector(tuple(movevec))[0] * self.speed, utils.normalize_vector(tuple(movevec))[1] * self.speed)
        self.rect = self.rect.move(movevec)
    def dead(self):
        self.kill()
    def increase_speed(self):
        self.speed += 1
