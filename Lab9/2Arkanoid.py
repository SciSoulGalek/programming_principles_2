"""
Arkanoid
Extend example project from Lab 8 and add following tasks:
1.You still need to work on arkanoid;
2.You need to add customization of a game, so a player can change some parameters of a game while he's playing (press "pause", choose "settings", switch some parameters and continue the game);
3.The game needs to have a main menu (or a pause menu)
"""
import pygame, math, random, time
# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 810, 540
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 120, 20
PADDLE_SPEED = 15
BALL_RADIUS = 13
BALL_SPEED = 5
BRICK_ROWS, BRICK_COLS = 6, 10
MAX_BOUNCE_ANGLE = math.radians(60)
BONUS_PERKS = ['Speed up', 'Speed down', 'Paddle expand', 'Paddle shrink']

# Some initializations
collision_cycle = 0
bonus_text = ""
bonus_text_timer = 0
normal_mode_text_timer = 0
challenge_mode_text_timer = 0

# Frames
clock = pygame.time.Clock()
FPS = 60
# Set up the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid Game")

# Function for increasing ball's speed over time and shrinking paddle's width per 5 collisions
def overtime():
    global collision_cycle, BALL_SPEED, PADDLE_WIDTH, paddle
    collision_cycle += 1
    if BALL_SPEED < 13:
        BALL_SPEED += 0.2
    if collision_cycle % 5 == 0 and PADDLE_WIDTH > 70: 
        PADDLE_WIDTH -= 1
    paddle.width = PADDLE_WIDTH
# Function to rotate the ball when it collides with wall, paddle or bricks
def detect_collision(dx, dy, ball, rect):
    overtime()
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy
# Function for applying bonus perks 
def apply_bonus_perk(perk):
    global PADDLE_SPEED, PADDLE_WIDTH
    if perk == 'Speed up':
        PADDLE_SPEED += 5
    elif perk == 'Speed down':
        if PADDLE_SPEED <= 5:
            PADDLE_SPEED = 5
        else:
            PADDLE_SPEED -= 5
    elif perk == 'Paddle expand':
        PADDLE_WIDTH += 20
    elif perk == 'Paddle shrink':
        if PADDLE_WIDTH < 70:
            PADDLE_WIDTH = 70
        else:
            PADDLE_WIDTH -= 20
# Information part {
# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (WIDTH // 2, HEIGHT // 2)
# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (WIDTH // 2, HEIGHT // 2)
# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)
# }

# Brick breaking sound
collision_sound = pygame.mixer.Sound('Lab8/music/catch.mp3')
collision_sound.set_volume(0.5)

# Game objects {
# paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 20, PADDLE_WIDTH, PADDLE_HEIGHT)
# ball
ballRadius = 20
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
ball_speed_x = BALL_SPEED // 2
ball_speed_y = -BALL_SPEED // 2
# bricks
bricks = []
bonus_bricks = []
UNBREAKABLE_POSITIONS = [(1, 2), (1, 3), (1, 6), (1, 7), (2, 2), (2, 7), (3, 2), (3, 7), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
brick_width, brick_height = 76, 20
brick_spacing_x, brick_spacing_y = 5, 5
for i in range(BRICK_ROWS):
    for j in range(BRICK_COLS):
        brick_x = j * (brick_width + brick_spacing_x) + brick_spacing_x
        brick_y = i * (brick_height + brick_spacing_y) + brick_spacing_y + 50
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        is_unbreakable = (i, j) in UNBREAKABLE_POSITIONS
        is_bonus_brick = not is_unbreakable and random.random() < 0.1  # 10% chance of bonus brick
        if is_bonus_brick:
            bonus_bricks.append(brick)
        else:
            bricks.append((brick, is_unbreakable))
# }

# Function to display pause menu
pause_font = pygame.font.SysFont('comicsansms', 40)
def display_pause_menu():
    screen.fill((0, 0, 0))  # Fill the screen with black
    resume_text = pause_font.render('Resume (ESC)', True, (255, 255, 255))
    settings_text = pause_font.render('Settings (S)', True, (255, 255, 255))
    quit_text = pause_font.render('Quit (Q)', True, (255, 255, 255))
    resume_rect = resume_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    settings_rect = settings_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(resume_text, resume_rect)
    screen.blit(settings_text, settings_rect)
    screen.blit(quit_text, quit_rect)
    pygame.display.flip()

settings_font = pygame.font.SysFont('comicsansms', 40)

def display_settings_menu():
    global normal_mode_text_timer, challenge_mode_text_timer
    screen.fill((0, 0, 0))  # Fill the screen with black
    fps_text = settings_font.render('Normal/Challenge (M)', True, (255, 255, 255))
    full_text = settings_font.render('Fullscreen mode (F)', True, (255, 255, 255))
    back_text = settings_font.render('Back (ESC)', True, (255, 255, 255))
    fps_rect = fps_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    full_rect = full_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(fps_text, fps_rect)
    screen.blit(full_text, full_rect)
    screen.blit(back_text, back_rect)
    # Mode Changed    
    if normal_mode_text_timer > 0:
        fps_changed_text = settings_font.render('Normal Mode', True, WHITE)
        fps_changed_rect = fps_changed_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(fps_changed_text, fps_changed_rect)
        normal_mode_text_timer -= 1
    
    # Mode Changed    
    if challenge_mode_text_timer > 0:
        fps_changed_text = settings_font.render('Challenge Mode', True, WHITE)
        fps_changed_rect = fps_changed_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(fps_changed_text, fps_changed_rect)
        challenge_mode_text_timer -= 1
    pygame.display.flip()

def toggle_fullscreen():
    global screen, WIDTH, HEIGHT
    if not screen.get_flags() & pygame.FULLSCREEN:
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

fps_change = False
def toggle_FPS():
    global FPS, fps_change, normal_mode_text_timer, challenge_mode_text_timer
    fps_change = not fps_change
    if not fps_change:
        FPS = 60
        normal_mode_text_timer = 360
    else:
        FPS = 120
        challenge_mode_text_timer = 720

# Define a variable to track if the game is paused
paused = False
in_settings_menu = False

# Function to toggle pause state
def toggle_pause():
    global paused
    paused = not paused

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if in_settings_menu:
                    in_settings_menu = False
                else:
                    toggle_pause()
            elif event.key == pygame.K_s and paused:
                in_settings_menu = True
            elif event.key == pygame.K_q and paused and not in_settings_menu:
                running = False
            elif event.key == pygame.K_f and in_settings_menu:
                toggle_fullscreen()
            elif event.key == pygame.K_m and in_settings_menu:
                toggle_FPS()

    if not paused:
        # Move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.right += PADDLE_SPEED

        # Move the ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Collision part {
        # Check for collisions with walls
        if ball.left < -3 or ball.right > WIDTH + 3:
            overtime()
            ball_speed_x = -ball_speed_x
        if ball.top < 0:
            overtime()
            ball_speed_y = -ball_speed_y

        # Check for collisions with paddle
        if ball.colliderect(paddle) and ball_speed_y > 0:
            # Calculate bounce angle based on where the ball hits the paddle
            rel_x = (paddle.x + paddle.width / 2) - ball.centerx
            norm_x = rel_x / (paddle.width / 2)
            bounce_angle = norm_x * -MAX_BOUNCE_ANGLE
            # Update ball speed based on bounce angle
            ball_speed_x = BALL_SPEED * math.sin(bounce_angle)
            ball_speed_y = -BALL_SPEED * math.cos(bounce_angle)
        # }

        # Brick collision part {
        # Check for collisions with unbreakable bricks
        for i, brick_data in enumerate(bricks):
            brick, unbreakable = brick_data
            if brick is not None and unbreakable and ball.colliderect(brick):
                ball_speed_x, ball_speed_y = detect_collision(ball_speed_x, ball_speed_y, ball, brick)
                collision_sound.play()
                break  # Exit loop after handling one collision

        # Check for collisions with breakable bricks
        for i, brick_data in enumerate(bricks):
            brick, unbreakable = brick_data
            if brick is not None and not unbreakable and ball.colliderect(brick):
                bricks[i] = None  # Mark breakable brick as destroyed
                ball_speed_x, ball_speed_y = detect_collision(ball_speed_x, ball_speed_y, ball, brick)
                game_score += 1
                collision_sound.play()
                break

        # Update removed bricks
        bricks = [brick_data for brick_data in bricks if brick_data is not None]

        # Check for collisions with bonus bricks
        hitIndex = ball.collidelist(bonus_bricks)
        if hitIndex != -1:
            hitRect = bonus_bricks.pop(hitIndex)
            perk = random.choice(BONUS_PERKS)
            apply_bonus_perk(perk)
            ball_speed_x, ball_speed_y = detect_collision(ball_speed_x, ball_speed_y, ball, hitRect)
            game_score += 1
            bonus_text = f"Bonus: {perk}"
            bonus_text_timer = 120
            collision_sound.play()
        # }

        # Draw the game objects {
        # paddle
        pygame.draw.rect(screen, BLUE, paddle)
        # ball
        pygame.draw.circle(screen, WHITE, ball.center, BALL_RADIUS)
        # bricks
        for brick_data in bricks:
            if brick_data is not None:
                brick, unbreakable = brick_data
                if unbreakable:
                    color = BLUE  # Color for unbreakable bricks
                else:
                    color = WHITE  # Color for regular bricks
                pygame.draw.rect(screen, color, brick)
        #bonus bricks    
        for brick in bonus_bricks:
            pygame.draw.rect(screen, GOLD, brick)
        # }

        # Game score
        game_score_text = game_score_fonts.render(f'Score: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
        
        # Bonus bricks info    
        if bonus_text_timer > 0:
            bonus_text_surface = pygame.font.SysFont('comicsansms', 40).render(bonus_text, True, WHITE)
            bonus_text_rect = bonus_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(bonus_text_surface, bonus_text_rect)
            bonus_text_timer -= 1

        # Check if the ball missed the paddle
        if ball.top > HEIGHT:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
            running = False
        elif all(brick_data is None or brick_data[1] for brick_data in bricks) and all(brick_data is None for brick_data in bonus_bricks):
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)
            running = False

        pygame.display.flip()
        clock.tick(FPS)
    elif in_settings_menu:
        display_settings_menu()
    else:
        display_pause_menu()

time.sleep(1)    
pygame.quit()