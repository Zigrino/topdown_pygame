import pygame
import time

class Missile_Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.sprite_sheet_image = pygame.image.load("assets/images/round_explosion/spritesheet/spritesheet.png").convert_alpha()
        self.spawn_time = time.time()
        self.image_width = 0
        self.image_height = 0
        self.scale = 1
        self.color = (255, 255, 255)
        self.position = position
        self.frame = 0
        self.image = None
        self.rect = None
        self.image_count = 0
        self.height_count = 0
        self.update()
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet_image, (0, 0), (x, y, width, height))
        return sprite
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.image = self.get_sprite((self.image_count % 10) * 100, (self.height_count) * 100, 100, 100)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.frame = pygame.time.get_ticks()
        self.image_count += 1
        if self.image_count % 10 == 0:
            self.height_count += 1
        if self.image_count >= 60:
            self.kill()



