import pygame
import globals
class Forcefield_Counter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.scale = 1
        self.template_image = pygame.transform.scale(pygame.image.load(r"assets/images/forcefield.png"), (self.scale, self.scale))
        self.rects = []
        
    def draw(self, surface):
        for i in range(len(self.images)):
            surface.blit(self.images[i], self.rects[i])
    def remove_forcefield(self):
        self.images.pop()
        self.rects.pop()
    def add_forcefield(self):
        appended_image = pygame.transform.scale(pygame.image.load(r"assets/images/forcefield.png"), (self.scale * 32, self.scale * 32)) 
        appended_rect = self.template_image.get_rect()
        appended_rect.topleft = (len(self.rects) * (5 + self.scale * 32), 0)
        self.images.append(appended_image)
        self.rects.append(appended_rect)
