import pygame

class Drop(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/bullet_drop.png")
        self.scale = 0.15
        #dimensions 224 × 120
        self.image = pygame.transform.scale(self.image, (self.scale * 224, self.scale * 120))
        self.rect = self.image.get_rect()
        self.rect.center = position
    def draw(self, surface):
        surface.blit(self.image, self.rect)

