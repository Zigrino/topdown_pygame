import pygame

class Forcefield(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player_sprite = player
        self.image = pygame.image.load(r"assets/images/forcefield.png")
        self.scale = 50
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = self.image.get_rect()
    def draw(self, surface):
            surface.blit(self.image, self.rect)
    def update(self, player_rect):
        self.rect.center = player_rect.center
