"""
Paint
Extend example project from https://nerdparadise.com/programming/pygame/part6 and add the following functionality:
1.Draw rectangle
2.Draw circle
3.Eraser
4.Color selection
"""
import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BRUSH_SIZES = [5, 10, 20, 30]

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Paint Program')

# Define button dimensions and positions
RECT_BUTTON_RECT = pygame.Rect(20, 20, 80, 40)
CIRCLE_BUTTON_RECT = pygame.Rect(120, 20, 80, 40)

# Variables
brush_color = BLACK
brush_size = BRUSH_SIZES[0]
drawing = False
last_pos = None
using_eraser = False
drawing_rect = False
rect_start = None
rect_end = None
creating_rect = False  # Track if currently creating a rectangle

screen.fill(WHITE)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if RECT_BUTTON_RECT.collidepoint(event.pos):
                    creating_rect = True  # Start creating a rectangle
                    rect_start = None
                    rect_end = None
                elif CIRCLE_BUTTON_RECT.collidepoint(event.pos):
                    pass
                else:
                    drawing = True
                    last_pos = event.pos
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if creating_rect:  # Finish creating the rectangle
                    if rect_start is None:
                        rect_start = event.pos
                    elif rect_end is None:
                        rect_end = event.pos
                        pygame.draw.rect(screen, brush_color, (rect_start[0], rect_start[1],
                                                                rect_end[0] - rect_start[0], rect_end[1] - rect_start[1]), 2)
                        creating_rect = False
                else:
                    drawing = False
                last_pos = None
        elif event.type == MOUSEMOTION:
            if drawing:
                mouse_pos = event.pos
                if last_pos:
                    if using_eraser:
                        pygame.draw.line(screen, WHITE, last_pos, mouse_pos, brush_size)
                    else:
                        pygame.draw.line(screen, brush_color, last_pos, mouse_pos, brush_size)
                last_pos = mouse_pos
        elif event.type == KEYDOWN:
            if event.key == K_c:  # Clear the screen
                screen.fill(WHITE)
            elif event.key == K_r:  # Change color to red
                brush_color = RED
                using_eraser = False
            elif event.key == K_g:  # Change color to green
                brush_color = GREEN
                using_eraser = False
            elif event.key == K_b:  # Change color to blue
                brush_color = BLUE
                using_eraser = False
            elif event.key == K_s:  # Cycle through brush sizes
                brush_size = BRUSH_SIZES[(BRUSH_SIZES.index(brush_size) + 1) % len(BRUSH_SIZES)]
            elif event.key == K_e:  # Toggle eraser
                using_eraser = not using_eraser
                if using_eraser:
                    brush_color = WHITE

    # Draw buttons
    pygame.draw.rect(screen, BLACK, RECT_BUTTON_RECT)
    pygame.draw.rect(screen, BLACK, CIRCLE_BUTTON_RECT)

    # Draw text on buttons
    font = pygame.font.Font(None, 36)
    rect_text = font.render("Rect", True, WHITE)
    circle_text = font.render("Circle", True, WHITE)
    screen.blit(rect_text, (RECT_BUTTON_RECT.x + 10, RECT_BUTTON_RECT.y + 10))
    screen.blit(circle_text, (CIRCLE_BUTTON_RECT.x + 5, CIRCLE_BUTTON_RECT.y + 10))

    # Update the screen
    pygame.display.flip()