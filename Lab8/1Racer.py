"""
Racer
Extend example project from lecture and finish following tutorials:
https://coderslegacy.com/python/python-pygame-tutorial/
https://coderslegacy.com/python/pygame-tutorial-part-2/
https://coderslegacy.com/python/pygame-tutorial-part-3/
Extra tasks to the given tutorial:
1.Adding randomly appearing coins on the road
2.Showing the number of collected coins in the top right corner
3.Comment your code
"""
#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
 
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
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#music
pygame.mixer.music.load('Lab8/music/background.wav')
pygame.mixer.music.play(-1)

#Background 
background = pygame.image.load("Lab8/images/AnimatedStreet.png")
background_y = 0 

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


#Enemy class
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED + 2)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#Player class 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab8/images/Player.png")
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
        self.image = pygame.image.load("Lab8/images/coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -400) 

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -400)
 
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coin = pygame.sprite.Group()
coin.add(C)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)
 
#Adding a new User event(speed increases every second) 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        #Increase speed
        if event.type == INC_SPEED:
            if SPEED < 10: 
                SPEED += 0.1     
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

    #Get the highscore to display
    f = open('Lab8/highscore.txt', 'r')
    HS = f.readline()
    HS = int(HS)

    #write score, highscore and coins
    highscore = font_small.render(f'Highscore:{HS}', True, BLACK)
    DISPLAYSURF.blit(highscore, (10,10))
    scores = font_small.render(str(SCORE), True, BLACK)
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
        pygame.mixer.Sound('Lab8/music/catch.mp3').play()
        COINS += 1
        collided_coin = pygame.sprite.spritecollideany(P1, coin)
        collided_coin = pygame.sprite.spritecollideany(P1, coin)
        collided_coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), -400)
         
    #Game over part
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('Lab8/music/crash.wav').play()
        time.sleep(1)
        #Save the highscore
        f = open('Lab8/highscore.txt', 'w')
        f.write(str(max(SCORE, HS)))   

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