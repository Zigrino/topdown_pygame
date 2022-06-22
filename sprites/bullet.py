import pygame, utils, math
utils = utils.Utils()
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/bullet.png")
        self.scale = 0.05
        #dimensions are 337*617
        self.image = pygame.transform.scale(self.image, (self.scale * 337, self.scale * 617))
        self.rect = self.image.get_rect()
        self.rect.center = position
        #mask for collisions
        self.mask = pygame.mask.from_surface(self.image)

        self.original_image = self.image
        mousepos = pygame.mouse.get_pos() 
        self.vec_to_mouse = utils.subtract_vectors(self.rect.center, mousepos)

        angle = -math.atan2(self.vec_to_mouse[1], self.vec_to_mouse[0]) * (180/math.pi)
        position = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, angle + 90)
        self.rect = self.image.get_rect(center = position)
        self.vec_to_mouse = utils.normalize_vector(self.vec_to_mouse) 
        self.speed = 10
        self.surface = pygame.display.get_surface()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        self.rect = self.rect.move((-self.vec_to_mouse[0] * self.speed, -self.vec_to_mouse[1] * self.speed)) 
        width, height = self.surface.get_size()
        if self.rect.x < 0 or self.rect.x > width:
            self.kill()
        if self.rect.y < 0 or self.rect.y > height:
            self.kill()
        
