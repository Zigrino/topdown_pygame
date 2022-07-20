import pygame

class Defence_Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        surface = pygame.display.get_surface()
        xbound, ybound = surface.get_size()
        self.image = pygame.image.load(r"assets/images/defence_powerup.png")
        self.rect = self.image.get_rect()
        #Bounds on spawning coords
        if self.x > (xbound - self.image.get_size()[0] // 2):
            self.x = xbound - self.image.get_size()[0]
        elif self.x < (self.image.get_size()[0] // 2):
            self.x = self.image.get_size()[0]
        if self.y > (ybound - self.image.get_size()[1] // 2):
            self.y = ybound - self.image.get_size()[1]
        elif self.y < self.image.get_size()[1] // 2:
            self.y = self.image.get_size()[1]
        self.rect.center = (self.x, self.y)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

