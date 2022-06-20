import pygame
import sys
import sprites.player
 
pygame.init()
 
#Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
 
#Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")
clock = pygame.time.Clock()
 
def main():
    #Sprites
    player = sprites.player.Player()
 
    running = True
    while running:
        #Screen refresh rate
        clock.tick(FPS)
    
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        #Rendering
        screen.fill((255, 255, 255))
        player.draw(screen)
    
        #Updating sprites
        player.update() 
    
        #Screen Refresh
        pygame.display.update()
 
if __name__ == "__main__":
    main()

