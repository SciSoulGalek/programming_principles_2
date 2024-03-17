"""
Create a simple clock application (only with minutes and seconds) which is synchronized with system clock.
Use Mickey's right hand as minutes arrow and left - as seconds.
"""
import pygame
import datetime
pygame.init()

#display
width, height = 720, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

#mickey image
mickey_body = pygame.image.load("Lab7/images/main-clock.png")
mickey_hand_sec = pygame.image.load("Lab7/images/left-hand.png")
mickey_hand_min = pygame.image.load("Lab7/images/right-hand.png")

#image scale 
mickey_body = pygame.transform.scale(mickey_body, (665, 665))
mickey_hand_sec = pygame.transform.scale(mickey_hand_sec, (120, 436))
mickey_hand_min = pygame.transform.scale(mickey_hand_min, (120, 436))

#frame rate
clock = pygame.time.Clock()
FPS = 60

#main draw
def draw_clock(seconds, minutes):
    #main screen fill
    screen.fill((255, 255, 255))
    
    #body
    body_rect = mickey_body.get_rect(center=(width // 2, height // 2))
    screen.blit(mickey_body, body_rect)
    
    #seconds hand
    angle_sec = seconds * 6
    hand_sec_rotated = pygame.transform.rotate(mickey_hand_sec, -angle_sec)
    hand_sec_rect = hand_sec_rotated.get_rect(center=(width // 2, height // 2))
    screen.blit(hand_sec_rotated, hand_sec_rect)
    
    #minutes hand
    angle_min = minutes * 6
    hand_min_rotated = pygame.transform.rotate(mickey_hand_min, -angle_min)
    hand_min_rect = hand_min_rotated.get_rect(center=(width // 2, height // 2))
    screen.blit(hand_min_rotated, hand_min_rect)

    pygame.display.flip()

#main loop
while True:
    #exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    #time at this moment
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute
    
    #main draw
    draw_clock(seconds, minutes)
    
    #frame rate
    clock.tick(FPS)