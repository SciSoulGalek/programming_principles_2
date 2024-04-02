"""
Paint
Extend example project from https://nerdparadise.com/programming/pygame/part6 and add the following functionality:
1.Draw rectangle
2.Draw circle
3.Eraser
4.Color selection
"""
import pygame, sys
from random import randint

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

RAD = 30

drawing = False
color = BLACK

screen.fill(pygame.Color('white'))
rainbow = pygame.image.load('Lab9/images/rainbow.png')
rainbow = pygame.transform.scale(rainbow, (100, 100))
start_pos = 0
end_pos = 0

mode = 0
# 0 - Rect
# 1 - Circle
# 2 - Eraser
# 3 - Pencil

img_cnt = 0

while not finished:
    clock.tick(FPS)

    pos = pygame.mouse.get_pos()
    screen.blit(rainbow, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos
            if pos[0] > 20 and pos[0] < 100 and pos[1] > 20 and pos[1] < 100:
                color = screen.get_at(pos)
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pos
            rect_x = abs(start_pos[0] - end_pos[0])
            rect_y = abs(start_pos[1] - end_pos[1])

            if mode == 0:
                drawRect(color, start_pos, rect_x, rect_y)
            elif mode == 1:
                drawCircle(color, start_pos, rect_x)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 2:
                eraser(pos, RAD)
            elif mode == 3:
                if start_pos:
                    pygame.draw.line(screen, color, start_pos, pos, 2)
                start_pos = pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mode += 1
                mode %= 4
                if mode == 2:
                    color = WHITE
            if event.key == pygame.K_BACKSPACE:
                screen.fill(pygame.Color('white'))

            if event.key == pygame.K_s:
                surf = screen.subsurface(pygame.Rect(0, 200, WIDTH, HEIGHT - 200))
                pygame.image.save(surf, f'./screenshots/photo{img_cnt}.jpg')
                img_cnt += 1

    pygame.display.flip()

pygame.quit()
sys.exit()
