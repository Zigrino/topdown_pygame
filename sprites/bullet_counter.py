import pygame

class Bullet_Counter(pygame.sprite.Sprite):
    def __init__(self, initial_bullet_num):
        super().__init__()
        self.images = []
        for i in range(initial_bullet_num):
            self.images.append(pygame.image.load(r"assets/images/bullet.png"))
        #rescaling images
        self.scale = .05
        for i in range(len(self.images)):
            # dimensions of image are 337 × 617
            self.images[i] = pygame.transform.scale(self.images[i], (self.scale * 337, self.scale * 617))

        #creating rects
        self.rects = []
        for i in self.images:
            self.rects.append(i.get_rect())
        #setting positions
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        for i in range(len(self.rects)):
            self.rects[i].bottomleft = (0 + i*(5 + self.scale * 337), height)
            
    def draw(self, surface):
        for i in range(len(self.images)):
            surface.blit(self.images[i], self.rects[i])
    def remove_bullet(self):
        self.images.pop()
        self.rects.pop()
    def add_bullet(self):
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        appended_image = pygame.transform.scale(pygame.image.load(r"assets/images/bullet.png"), (self.scale * 337, self.scale * 617))
        self.images.append(appended_image)
        appended_rect = self.images[-1].get_rect()
        appended_rect.bottomleft = (len(self.rects) * (5 + self.scale * 337), height)
        self.rects.append(appended_rect)
    


