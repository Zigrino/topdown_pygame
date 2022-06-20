import pygame
import pygame.gfxdraw
import constants
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Constants
        self.width = 30
        self.height = 30
        self.walkspeed = 5
        self.size = 3
        #rgb value
        self.color = (21, 145, 240)
        #other stuff
        self.image = pygame.image.load(r"assets/images/player.png")
        #scale image
        self.scale = 100
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        #get rectangle for image, set position
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        surface = pygame.display.get_surface()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        #pygame.gfxdraw.aacircle(self.image, self.rect.x, self.rect.y, self.width, self.color)
        #print(self.image.get_alpha())
        
    def update(self):
        #inputs
        keys = pygame.key.get_pressed()
        velocity = [0, 0] #velocity vector
        if keys[pygame.K_a]:
            velocity[0] -= self.walkspeed
        if keys[pygame.K_d]:
            velocity[0] += self.walkspeed
        if keys[pygame.K_w]:
            velocity[1] -= self.walkspeed
        if keys[pygame.K_s]:
            velocity[1] += self.walkspeed
        #border collisions
        if self.rect.right > 800:
            if velocity[0] > 0:
                velocity[0] = 0
        elif self.rect.left < 0:
            if velocity[0] < 0:
                velocity[0] = 0
        if self.rect.bottom > 600:
            if velocity[1] > 0:
                velocity[1] = 0
        elif self.rect.top < 0:
            if velocity[1] < 0:
                velocity[1] = 0

        self.rect = self.rect.move(tuple(velocity))
