import pygame

class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font('freesansbold.ttf', 64)
        self.text1 = self.font.render("GAME OVER", True, (0, 0, 0), (255, 255, 255))
        self.text2 = self.font.render("to restart, press r", True, (0, 0, 0), (255, 255, 255))
        self.playerDead = False
        self.rect1 = self.text1.get_rect()
        self.rect2 = self.text2.get_rect()
    def draw(self, screen):
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        self.rect1.center = (width//2, height//2 - 50)
        self.rect2.center = (width//2, height//2 + 50)
        if self.playerDead:
            screen.blit(self.text1, self.rect1)
            screen.blit(self.text2, self.rect2)

