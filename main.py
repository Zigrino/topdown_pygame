import pygame
import sys
import sprites.player
import sprites.enemy
import sprites.gun 
import sprites.bullet
import sprites.gameover
import sprites.bullet_counter
import sprites.bullet_drop
import utils
import time
pygame.init()
utils = utils.Utils()
#Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

fullscreen = input("Fullscreen or na (fullscreen is easier)? y/n: ") 
bullet_num = int(input("How many bullets would you like to start with? (more = easier): "))

#Window creating
#screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
if fullscreen == "y" or fullscreen == "yes":
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else: 
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("")
clock = pygame.time.Clock()
 
def main():
    global bullet_num

    #Sprites
    player = sprites.player.Player()
    gun = sprites.gun.Gun()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    bullet_counter = sprites.bullet_counter.Bullet_Counter(bullet_num)
    drops = pygame.sprite.Group()
    #variables
    running = True
    mouse_exit = False
    max_enemies = 5
    last_spawn_time = time.time()
    spawn_delay = 2
    min_spawn_delay = 0.5
    start_time = time.time()
    difficulty_time = time.time()
    difficulty_increment_time = 5
    enemy_speed = 2
    enemy_max_speed = 6
    player_dead = False
    god_mode = False
    god_firing = False
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
                if god_mode:
                    god_firing = True
                if not player_dead and not god_mode and bullet_num > 0:
                    bullet_num -= 1
                    bullet_counter.remove_bullet()
                    bullets.add(sprites.bullet.Bullet(player.rect.center))
                    print(f"You have {bullet_num} bullets left")
            if event.type == pygame.MOUSEBUTTONUP:
                if god_mode:
                    god_firing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    if god_mode:
                        god_mode = False
                        print("Disabled god mode")
                    else:
                        god_mode = True
                        print("GOD MODE ENABLED. PREPARE TO DIE, RED SCUM")

        #Godmode firing
        if god_firing:
            bullets.add(sprites.bullet.Bullet(player.rect.center))


        #stop mouse from exiting screen
        
        #collisions
        #enemy player collisions
        for enemy in enemies:
            if pygame.sprite.collide_mask(player, enemy):
                gameover = sprites.gameover.Gameover()
                player_dead = True
                player.dead()
                gun.player_killed()
        #bullet enemy collisions
        for bullet in bullets:
            for enemy in enemies:
                if pygame.sprite.collide_mask(bullet, enemy):
                    drops.add(sprites.bullet_drop.Drop(enemy.rect.center))
                    print("killed enemy")
                    enemy.dead()
        #player bullet drop collisions
        for drop in drops:
            if pygame.sprite.collide_mask(player, drop):
                bullet_num += 1
                bullet_counter.add_bullet()
                drop.kill()


                
        
        #Spawning enemies
        if time.time() - last_spawn_time >= spawn_delay:
            if len(enemies.sprites()) < max_enemies:
                print(len(enemies.sprites()))
                last_spawn_time = time.time()
                enemies.add(sprites.enemy.Enemy(player, speed = enemy_speed))
        if (time.time() - difficulty_time) >= difficulty_increment_time:
            print("increasing difficulty")
            max_enemies += 1
            if enemy_speed < enemy_max_speed:
                enemy_speed += 1
            if spawn_delay > min_spawn_delay:
                spawn_delay -= 0.3
            difficulty_time = time.time()

        #Rendering
        screen.fill((255, 255, 255))
        drops.draw(screen)
        player.draw(screen)
        enemies.draw(screen)
        bullet_counter.draw(screen)

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

