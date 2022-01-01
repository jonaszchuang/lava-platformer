import sys
import os
import pygame
import random
from platform import Platform
from player import Player
from lava import Lava
from wall import Wall
from fireball import Fireball
from heart import Heart
from background import Background
from points import Points
from start import Start

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
changing = [255, 100, 50]
way = 1
way2 = 1
way3 = 1

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Platforms sprite group
platforms = pygame.sprite.Group()
walls = pygame.sprite.Group()
lavas = pygame.sprite.Group()
fireballs = pygame.sprite.Group()
lives = pygame.sprite.Group()
hearts = 3
backgrounds = pygame.sprite.Group()
fire_points = pygame.sprite.Group()
starts = pygame.sprite.Group()
back_text = pygame.sprite.Group()

platforms.add(Platform(300, 500, 350, 50))
platforms.add(Platform(125, 375, 225, 50))
platforms.add(Platform(650, 350, 200, 50))
platforms.add(Platform(700, 600, 200, 25))
platforms.add(Platform(0, SCREEN_HEIGHT, SCREEN_WIDTH, 10))
platforms.add(Platform(SCREEN_WIDTH / 8, SCREEN_HEIGHT, SCREEN_WIDTH, 10))
platforms.add(Platform(SCREEN_WIDTH / 6, SCREEN_HEIGHT, SCREEN_WIDTH, 10))
platforms.add(Platform(SCREEN_WIDTH / 4, SCREEN_HEIGHT, SCREEN_WIDTH, 10))
platforms.add(Platform(SCREEN_WIDTH / 2, SCREEN_HEIGHT, SCREEN_WIDTH, 10))
platforms.add(Platform(SCREEN_WIDTH - (SCREEN_WIDTH / 8), SCREEN_HEIGHT, SCREEN_WIDTH, 10))
platforms.add(Platform(SCREEN_WIDTH - (SCREEN_WIDTH / 6), SCREEN_HEIGHT, SCREEN_WIDTH, 10))
platforms.add(Platform(SCREEN_WIDTH - (SCREEN_WIDTH / 4), SCREEN_HEIGHT, SCREEN_WIDTH, 10))
walls.add(Wall(0, 0, 10, SCREEN_HEIGHT))
walls.add(Wall(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT))
fireballs.add(Fireball(SCREEN_WIDTH, random.randint(300, 500)))
fireballs.add(Fireball(SCREEN_WIDTH + 700, random.randint(300, 500)))
fireballs.add(Fireball(SCREEN_WIDTH + 1400, random.randint(300, 500)))
lavas.add(Lava(650, SCREEN_HEIGHT - 40, 450, 40))
lavas.add(Lava(5, SCREEN_HEIGHT - 40, 450, 40))
back_text.add(Lava(200, 200, 512, 121))
lavaSpeed = -0.001
backgrounds.add(Background())
fire_points.add(Points(random.randint(0, SCREEN_WIDTH - 100), random.randint(300, 500)))
starts.add(Start(200, 200))
counter = 0

start_game = False

#Making font
FONT = pygame.font.SysFont("monospace", 100)
FONT2 = pygame.font.SysFont('arial', 100)
label_gameOver = FONT.render("Game Over", 1, (changing))
label_counter = FONT.render(str(counter), 1, (changing))
label_title1 = FONT2.render("Lava Platformer", 1, (changing))


def reset_lives():
    lives.remove(all)
    for i in range(0, hearts):
        lives.add(Heart(SCREEN_WIDTH - 350 - (i * 200), 0))

# Create the player sprite and add it to the players sprite group
player = Player(400, 500)
players = pygame.sprite.Group()
players.add(player)
reset_lives()

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()
        
    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if start_game == True:
        if keys_pressed[pygame.K_UP]:
            counter += 1
            pygame.time.wait(10)
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            player.move(-player.move_speed, 0)
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            player.move(player.move_speed, 0)
        if keys_pressed[pygame.K_q]:
            if counter - 15 >= 0:
                hearts += 1
                reset_lives()
                counter -= 15
            pygame.time.wait(10)
        if keys_pressed[pygame.K_LSHIFT]:
            pygame.time.wait(75)
        if keys_pressed[pygame.K_SPACE]:
            player.jump()
    if keys_pressed[pygame.K_RETURN] or keys_pressed[pygame.K_KP_ENTER]:
        start_game = True

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        pass
    if mouse_buttons[2]:  # If right mouse pressed
        pass

    """
    UPDATE section - manipulate everything on the screen
    """
    
    players.update()

    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
    
    for platform in hit_platforms:
            player.on_platform_collide(platform)

    if hearts == 0:
        pygame.time.wait(10000)
        pygame.quit()
        sys.exit()

    if start_game == True:
        

        if pygame.sprite.spritecollide(player, lavas, False):
            player.kill()
            hearts -= 1
            lives = pygame.sprite.Group()
            reset_lives()
            player = Player(0, 0)
            players.add(player)

        if pygame.sprite.spritecollide(player, fireballs, False):
            player.kill()
            hearts -= 1
            lives = pygame.sprite.Group()
            reset_lives()
            player = Player(0, 0)
            players.add(player)

        if len(hit_platforms) == 0:
            player.can_jump = False

        if pygame.sprite.spritecollide(player, fire_points, True):
            fire_points.clear
            fire_points.add(Points(random.randint(0, SCREEN_WIDTH - 100), random.randint(300, 500)))
            counter += 2

        for platform in platforms:
            if platform.rect.x <= 0:
                platform.rect.x = SCREEN_WIDTH
            else:
                platform.rect.x -= 2

                random_amount = random.randint(1, 2)
                random_amount2 = random.randint(1, 2)
                random_amount3 = random.randint(1, 2)
                if changing[2] >= 250:
                    way3 = -1
                if changing[1] >= 250:
                    way2 = -1
                if changing[0] >= 250:
                    way = -1
                if changing[0] <= 5:
                    way = 1
                if changing[1] <= 5:
                    way2 = 1
                if changing[2] <= 5:
                    way3 = 1              
                changing[0] += random_amount3 * way
                changing[1] += random_amount2 * way2
                changing[2] += random_amount * way3
                label_counter = FONT.render(str(counter), 1, changing)
                label_gameOver = FONT.render("Game Over", 1, changing)

        for lava in lavas:
            if lava.rect.x == 0 - lava.width:
                lava.rect.x = SCREEN_WIDTH
            else:
                lava.rect.x -= 1

        for fireball in fireballs:
            if fireball.rect.x <= -1000 - fireball.rect.width:
                fireball.rect.x = SCREEN_WIDTH
                fireball.rect.y = random.randint(300, 500)
            else:
                fireball.rect.x -= fireball.move_speed

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    
    backgrounds.draw(screen)
    screen.blit(label_title1, (150, 75))
    if start_game == False:
        back_text.draw(screen)
        starts.draw(screen)
    # if start_game == True:
    platforms.draw(screen)
    players.draw(screen)
    walls.draw(screen)
    lavas.draw(screen)
    fireballs.draw(screen)
    lives.draw(screen)
    if hearts <= 0:
        screen.blit(label_gameOver, (SCREEN_WIDTH / 4, -10))
    fire_points.draw(screen)
    screen.blit(label_counter, (SCREEN_WIDTH - 150, 40))

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    