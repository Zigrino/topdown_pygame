import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text = self.font.render(f"Score: {self.score}", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        self.rect.bottomright = (width, height)
        self.gameover = False
        self.font1 = pygame.font.Font('freesansbold.ttf', 64)
        self.text1 = self.font1.render(f"Score: {self.score}", True, (0, 0, 0), (255, 255, 255))
        self.rect1 = self.text1.get_rect()
    def draw(self, surface):
        width, height = surface.get_size()
        if self.gameover:
            self.text1 = self.font1.render(f"Score: {self.score}", True, (0, 0, 0), (255, 255, 255))
            self.rect1.center = (width//2, height//2 + 150)
            surface.blit(self.text1, self.rect1)

        else:
            self.text = self.font.render(f"Score: {self.score}", True, (0, 0, 0), (255, 255, 255))
            self.rect.bottomright = (width - 5, height - 5)
            surface.blit(self.text, self.rect)
