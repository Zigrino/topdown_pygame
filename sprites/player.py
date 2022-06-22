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
        
        self.mask = pygame.mask.from_surface(self.image)
        self.surface = pygame.display.get_surface()
        self.isdead = False
    def draw(self, surface):
        if not self.isdead:
            surface.blit(self.image, self.rect)
        #pygame.gfxdraw.aacircle(self.image, self.rect.x, self.rect.y, self.width, self.color)
        #print(self.image.get_alpha())
        
    def update(self):
        if not self.isdead:
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

            self.screen_width, self.screen_height = self.surface.get_size()

            if self.rect.right > self.screen_width:
                if velocity[0] > 0:
                    velocity[0] = 0
            elif self.rect.left < 0:
                if velocity[0] < 0:
                    velocity[0] = 0
            if self.rect.bottom > self.screen_height:
                if velocity[1] > 0:
                    velocity[1] = 0
            elif self.rect.top < 0:
                if velocity[1] < 0:
                    velocity[1] = 0

            self.rect = self.rect.move(tuple(velocity))
    def dead(self):
        self.isdead = True
