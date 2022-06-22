import pygame
import sys
import sprites.player
import sprites.enemy
import sprites.gun 
import sprites.bullet
import utils
pygame.init()
 
#Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

 
#Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("")
clock = pygame.time.Clock()
 
def main():
    #Sprites
    player = sprites.player.Player()
    gun = sprites.gun.Gun()
    enemies = [sprites.enemy.Enemy(player)] 
    bullets = []
    running = True
    mouse_exit = False
    while running:
        #Screen refresh rate
        clock.tick(FPS)
    
        #Events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if mouse_exit:
                mouse_exit = False
            else:
                mouse_exit = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullets.append(sprites.bullet.Bullet(player.rect.center))
        #stop mouse from exiting screen
        mousepos = pygame.mouse.get_pos() 
        """
        if not mouse_exit:
            if mousepos[0] <= 0:
                pygame.mouse.set_pos([0, mousepos[1]])
            elif mousepos[0] >= WIDTH:
                pygame.mouse.set_pos([WIDTH, mousepos[1]])
            if mousepos[1] <= 0:
                pygame.mouse.set_pos([mousepos[0], 0])
            elif mousepos[1] >= HEIGHT:
                pygame.mouse.set_pos([mousepos[0], HEIGHT])
        """

                
    
        #Rendering
        screen.fill((255, 255, 255))
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        gun.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        #Updating sprites
        player.update() 
        for enemy in enemies:
            enemy.update(player)
        gun.update(player) 
        for bullet in bullets:
            bullet.update()
        #Screen Refresh
        pygame.display.update()
 
if __name__ == "__main__":
    main()

