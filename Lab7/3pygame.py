"""
Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key.
The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
"""
import pygame
pygame.init()

#colors
WHITE = (255, 255, 255)
RED =(255, 0, 0)

#display
W, H = 720, 720
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Ball Game")

#frame rate
clock = pygame.time.Clock()
FPS = 60

#ball settings
x = W // 2
y = H // 2
velocity = 20
c_rad = 25
c_color = (RED)
c_pos = [x, y]

#font
font = pygame.font.Font(None, 36) 
text_color = (0, 0, 0)

#main loop
while True:
    #exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    #moving and border
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and c_pos[0] > c_rad:
        c_pos[0] -= velocity
    if keys[pygame.K_RIGHT] and c_pos[0] < W - c_rad:
        c_pos[0] += velocity
    if keys[pygame.K_UP] and c_pos[1] > c_rad:
        c_pos[1] -= velocity
    if keys[pygame.K_DOWN] and c_pos[1] < H - c_rad:
        c_pos[1] += velocity   
    
    #main screen fill
    screen.fill(WHITE)
    
    #border hit text
    if c_pos[0] <= c_rad or c_pos[0] >= W - c_rad or c_pos[1] <= c_rad or c_pos[1] >= H - c_rad:
        message = font.render("You are on the border", True, text_color)
    else:
        message = None

    if message:
        screen.blit(message, (W // 2 - message.get_width() // 2, H // 2 - message.get_height() // 2))

    #draw the ball
    pygame.draw.circle(screen, c_color, (c_pos[0], c_pos[1]), c_rad)
   
    pygame.display.update()

    #frame rate
    clock.tick(FPS)