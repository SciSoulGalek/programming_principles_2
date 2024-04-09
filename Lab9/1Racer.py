"""
Racer
Extend example project from Lab 8 and add following tasks: 
Extra tasks to the given tutorial:
1.Randomly generating coins with different weights on the road
2.Increase the speed of Enemy when the player earns N coins
3.Comment your code
"""
#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
pygame.mixer.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0
FUEL = 100

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#Background 
background = pygame.image.load("Lab9/images/AnimatedStreet.png")
background_y = 0 

#Instructions
instructions = [
'Instructions',
'Controls: UP, DOWN, LEFT, RIGHT',
'Normal coin gives 1',
'Smaller coin gives 3',
'Challenge yourself by collecting coins', 
'Don\'t forget to collect fuel',
'Press SPACE to start'
]
text_height = sum(font.size(line)[1] for line in instructions)
start_y = (SCREEN_HEIGHT - text_height) // 2


#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")

def display_start_screen():
    DISPLAYSURF.fill((0, 0, 0))  # Fill the screen with black
    for i, line in enumerate(instructions):
        start_text_surface = font_small.render(line, True, (255, 255, 255))
        start_text_rect = start_text_surface.get_rect(center=(SCREEN_WIDTH // 2, start_y + i * font.get_linesize()))
        DISPLAYSURF.blit(start_text_surface, start_text_rect)
    pygame.display.flip()

#Enemy class
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab9/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED + 2 + COINS / 100)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#Player class 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab9/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT: 
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab9/images/coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -(SPEED * 100)) 

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -(SPEED * 100))

#Better coin class
class Better_Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab9/images/coin.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -(SPEED * 500)) 

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -(SPEED * 500))

#Fuel class
class Fuel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab9/images/fuel.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -(SPEED * 100)) 

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -(SPEED * 100))
 
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C = Coin()
B = Better_Coin()
F = Fuel()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coin = pygame.sprite.Group()
coin.add(C)
better_coin = pygame.sprite.Group()
better_coin.add(B)
fuel = pygame.sprite.Group()
fuel.add(F)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)
all_sprites.add(B)
all_sprites.add(F)

# Fuel bar variables
FUEL = 100
fuel_bar_width = 100
fuel_bar_height = 10
fuel_bar_pos = (10, SCREEN_HEIGHT - 30)
fuel_decrease_rate = 0.1  # Rate at which fuel decreases per frame

#Get the highscore to display
f = open('Lab9/highscore.txt', 'r')
HS = f.readline()
HS = int(HS)

#Adding a new User event(speed increases every second) 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

start_screen = True
#Game Loop
while True:
    if start_screen:
        display_start_screen()
    #Cycles through all events occurring  
        for event in pygame.event.get():
            #Getting out of the start screen
            if event.type == pygame.KEYDOWN:
                if start_screen and event.key == pygame.K_SPACE:
                    start_screen = False
            #Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    else:
    #Cycles through all events occurring  
        for event in pygame.event.get():
            #Increase speed
            if event.type == INC_SPEED:
                if SPEED < 10: 
                    SPEED += 0.05     
            #Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #Move the background to create animation effect
        background_y += SPEED - 0.4
        if background_y >= SCREEN_HEIGHT:
            background_y = 0

        #Display the background
        DISPLAYSURF.blit(background, (0, background_y))
        DISPLAYSURF.blit(background, (0, background_y - SCREEN_HEIGHT))

        #Draw fuel bar
        pygame.draw.rect(DISPLAYSURF, GREEN, (fuel_bar_pos[0], fuel_bar_pos[1], FUEL, fuel_bar_height))
        pygame.draw.rect(DISPLAYSURF, BLACK, (fuel_bar_pos[0], fuel_bar_pos[1], fuel_bar_width, fuel_bar_height), 2)

        #Decrease fuel over time
        FUEL -= fuel_decrease_rate

        #Display score, highscore and coins
        highscore = font_small.render(f'Highscore:{HS}', True, BLACK)
        scores = font_small.render(str(SCORE), True, BLACK)
        if HS <= SCORE:
            HS = SCORE
        DISPLAYSURF.blit(highscore, (10,10))
        DISPLAYSURF.blit(scores, (10,30))
        coins = font_small.render(str(COINS), True, BLACK)
        DISPLAYSURF.blit(coins, (360,10))

        if SPEED < 10:
            speed = font_small.render(f'Speed:{str(round(SPEED, 2))}', True, BLACK)
            DISPLAYSURF.blit(speed, (SCREEN_WIDTH // 2 - 48, SCREEN_HEIGHT - 50))
        else:
            speed = font_small.render(f'Speed:10(MAX)', True, BLACK)
            DISPLAYSURF.blit(speed, (SCREEN_WIDTH // 2 - 48, SCREEN_HEIGHT - 50))

        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        #Collecting coin
        if pygame.sprite.spritecollideany(P1, coin):
            pygame.mixer.Sound('Lab9/music/catch.mp3').play()
            COINS += 1
            collided_coin = pygame.sprite.spritecollideany(P1, coin)
            collided_coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), -(SPEED * 100))

        #Collecting better coin
        if pygame.sprite.spritecollideany(P1, better_coin):
            pygame.mixer.Sound('Lab9/music/catch.mp3').play()
            COINS += 3
            collided_better_coin = pygame.sprite.spritecollideany(P1, better_coin)
            collided_better_coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), -(SPEED * 500))

        #Collecting fuel
        if pygame.sprite.spritecollideany(P1, fuel):
            pygame.mixer.Sound('Lab9/music/catch.mp3').play()
            FUEL = min(100, FUEL + 20)
            collided_fuel = pygame.sprite.spritecollideany(P1, fuel)
            collided_fuel.rect.center = (random.randint(40, SCREEN_WIDTH-40), -(SPEED * 100))

        #Game over part
        if pygame.sprite.spritecollideany(P1, enemies) or FUEL < 0:
            pygame.mixer.Sound('Lab9/music/crash.wav').play()
            time.sleep(1)
            #Save the highscore
            f = open('Lab9/highscore.txt', 'w')
            f.write(str(HS))   

            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,250))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()        
        pygame.display.update()
    
    FramePerSec.tick(FPS)