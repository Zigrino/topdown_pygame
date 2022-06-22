import pygame
import utils
import math
utils = utils.Utils()
class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/gun.png") 
        self.scale = 0.1
        #dimensions of image is 889 * 193
        self.image = pygame.transform.scale(self.image, (889*self.scale, 193*self.scale))
        self.rect = self.image.get_rect()
        self.original_image = self.image
        self.playerisdead = False
    def draw(self, surface):
        if not self.playerisdead:
            surface.blit(self.image, self.rect)


    def update(self, player):
        if not self.playerisdead:
            self.rect.center = player.rect.center
            mousepos = pygame.mouse.get_pos()
            vec_to_mouse = utils.subtract_vectors(self.rect.center, mousepos)
            #rotating image
            angle = -math.atan2(vec_to_mouse[1], vec_to_mouse[0]) * (180/math.pi)
            position = self.rect.center 
            self.image = pygame.transform.rotate(self.original_image, angle + 180)
            self.rect = self.image.get_rect(center = position)
    def player_killed(self):
        self.playerisdead = True
