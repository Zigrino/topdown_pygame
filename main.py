import globals
import pygame
import pygame.mixer as mixer
import sys
import sprites.player
import sprites.enemy
import sprites.gun 
import sprites.bullet
import sprites.gameover
import sprites.bullet_counter
import sprites.bullet_drop
import sprites.gameover
import sprites.score
import sprites.damage_powerup
import sprites.defence_powerup
import utils
import random
import time
pygame.init()
utils = utils.Utils()
#Constants
WIDTH = globals.window_size[0]
HEIGHT = globals.window_size[1]
FPS = 60

fullscreen = input("Fullscreen or na (fullscreen is easier)? y/n: ") 
orig_bullet_num = int(input("How many bullets would you like to start with? (more = easier): "))


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
    global orig_bullet_num
    bullet_num = orig_bullet_num
    
    #Sprites
    player = sprites.player.Player()
    gun = sprites.gun.Gun()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    #powerups
    damage_powerups = pygame.sprite.Group()
    defence_powerups = pygame.sprite.Group()
    #bullet stuff
    bullet_counter = sprites.bullet_counter.Bullet_Counter(bullet_num)
    drops = pygame.sprite.Group()
    #gameover & score stuff
    gameover = sprites.gameover.Gameover()
    score = sprites.score.Score()
    #shoot sound
    shoot_sound = mixer.Sound(r"assets/sounds/shoot_sound.wav")
    empty_sound = mixer.Sound(r"assets/sounds/empty_sound.wav")
    pump_sound = mixer.Sound(r"assets/sounds/pump.wav")
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
    enemy_max_speed = 5
    player_dead = False
    god_mode = False
    god_firing = False

    #powerup global vars
    time_since_dmgpwr = 0
    time_since_dfnpwr = 0
    last_dmg_pwr_time = time.time()
    last_dfn_pwr_time = time.time()
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
                    #BULLET TIME
                    bullet_num -= 1
                    bullet_counter.remove_bullet()
                    shoot_sound.play()
                    bullets.add(sprites.bullet.Bullet(player.rect.center))
                elif not player_dead and bullet_num <= 0:
                    empty_sound.play()
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
                        enemy_max_speed = 25
                        print("GOD MODE ENABLED. PREPARE TO DIE, RED SCUM")
                if event.key == pygame.K_r:
                    main()
                if gameover and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()  


        #Godmode firing
        if god_firing:
            bullets.add(sprites.bullet.Bullet(player.rect.center))




        
        #collisions
        #enemy player collisions
        for enemy in enemies:
            if pygame.sprite.collide_mask(player, enemy):
                gameover.playerDead = True
                player_dead = True
                player.dead()
                gun.player_killed()
        #bullet enemy collisions
        for bullet in bullets:
            for enemy in enemies:
                if pygame.sprite.collide_mask(bullet, enemy):
                    drops.add(sprites.bullet_drop.Drop(enemy.rect.center))
                    enemy.dead()
                    score.score += 1
        #player bullet drop collisions
        for drop in drops:
            if pygame.sprite.collide_mask(player, drop):
                bullet_num += 1
                bullet_counter.add_bullet()
                pump_sound.play()
                drop.kill()

        #player powerup collisions
        for powerup in damage_powerups:
            if pygame.sprite.collide_mask(player, powerup):
                #Powerup stuff

                #Play sound and kill powerup
                powerup.kill()

        for powerup in defence_powerups:
            if pygame.sprite.collide_mask(player, powerup):
                #Powerup stuff

                #Play sound and kill powerup
                powerup.kill()
                
        
        #Spawning enemies
        if time.time() - last_spawn_time >= spawn_delay:
            if len(enemies.sprites()) < max_enemies:
                last_spawn_time = time.time()
                enemies.add(sprites.enemy.Enemy(player, speed = enemy_speed))
        if (time.time() - difficulty_time) >= difficulty_increment_time:
            max_enemies += 1
            if enemy_speed < enemy_max_speed:
                enemy_speed += 1
            if spawn_delay > min_spawn_delay:
                spawn_delay -= 0.3
            difficulty_time = time.time()
        

        #spawning powerups
        time_since_dmgpwr = time.time() - last_dmg_pwr_time
        if time_since_dmgpwr >= 6:
            screenx, screeny = screen.get_size()
            damage_powerups.add(sprites.damage_powerup.Damage_Powerup(random.randint(0, screenx), random.randint(0, screeny)))
            last_dmg_pwr_time = time.time()

        time_since_dfnpwr = time.time() - last_dfn_pwr_time

        if time_since_dfnpwr >= 6:
            screenx, screeny = screen.get_size()
            defence_powerups.add(sprites.defence_powerup.Defence_Powerup(random.randint(0, screenx), random.randint(0, screeny)))
            last_dfn_pwr_time = time.time()
        

        #Rendering
        screen.fill((255, 255, 255))
        if not gameover.playerDead:
            damage_powerups.draw(screen)
            defence_powerups.draw(screen)
            drops.draw(screen)
            bullet_counter.draw(screen)
            bullets.draw(screen)
            score.draw(screen)
            player.draw(screen)
            enemies.draw(screen)
            gun.draw(screen)

            
        else:
            gameover.draw(screen)
            score.gameover = True
            score.draw(screen)

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

