import pygame
import sys
import sprites.player
import sprites.enemy
import sprites.gun 
import sprites.bullet
import sprites.gameover
import utils
pygame.init()
utils = utils.Utils()
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
    enemies = pygame.sprite.Group(sprites.enemy.Enemy(player))
    bullets = pygame.sprite.Group()
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
                bullets.add(sprites.bullet.Bullet(player.rect.center))
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
        
        #collisions
        for enemy in enemies:
            if pygame.sprite.collide_mask(player, enemy):
                gameover = sprites.gameover.Gameover()
                player.dead()
                gun.player_killed()
                print("player killed")
        for bullet in bullets:
            for enemy in enemies:
                if pygame.sprite.collide_mask(bullet, enemy):
                    enemy.dead()
                    print("killed enemy")
                
    
        #Rendering
        screen.fill((255, 255, 255))
        player.draw(screen)
        enemies.draw(screen)

        gun.draw(screen)
        bullets.draw(screen)
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

