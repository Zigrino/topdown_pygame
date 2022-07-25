import pygame
class Missile_Counter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.scale = 32
        self.template_image = pygame.transform.scale(pygame.image.load(r"assets/images/missile.png"), (self.scale, self.scale))
        self.rects = []
    def draw(self, surface):
        for i in range(len(self.images)):
            surface.blit(self.images[i], self.rects[i])
    
    def remove_missile(self):
        self.images.pop()
        self.rects.pop()
    def add_missile(self):
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        appended_image = pygame.transform.scale(pygame.image.load(r"assets/images/missile.png"), (self.scale, self.scale)) 
        appended_rect = self.template_image.get_rect()
        appended_rect.topright = (width - len(self.rects) * (-10 + self.scale), 0)
        self.images.append(appended_image)
        self.rects.append(appended_rect)

