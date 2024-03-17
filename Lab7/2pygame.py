"""
Create music player with keyboard controller.
You have to be able to press keyboard: play, stop, next and previous as some keys.
Player has to react to the given command appropriately.
"""
import pygame 
import os
pygame.init()
pygame.mixer.init()

#colors
WHITE = (255, 255, 255)

#display
width, height = 480, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")
paint_rect = pygame.Rect(0, 480, 480, 300)  

#buttons image
pause = pygame.image.load("Lab7/images/pause-icon.png")
play = pygame.image.load("Lab7/images/play-icon.png")
next = pygame.image.load("Lab7/images/next.png")
next_clicked = pygame.image.load("Lab7/images/next_clicked.png")
image = pygame.image.load("Lab7/images/mus_image.png")

#image scale 
pause = pygame.transform.scale(pause, (150, 150))
play = pygame.transform.scale(play, (150, 150))
next = pygame.transform.scale(next, (150, 150))
next_clicked = pygame.transform.scale(next_clicked, (150, 150))
previous = pygame.transform.rotate(next, 180)
previous_clicked = pygame.transform.rotate(next_clicked, 180)

#path to the music folder
music_folder = 'Lab7/music'

#load all music files
music_files = []
for file_name in os.listdir(music_folder):
    if file_name.endswith('.ogg' or '.mp3'):
        music_files.append(os.path.join(music_folder, file_name))

#player state
current_track = 0
is_playing = False
volume = 1
next_clicked_frames_to_show_image = 0
previous_clicked_frames_to_show_image = 0
current_time = 0.0

#frame rate
clock = pygame.time.Clock()
FPS = 60

# Function to play the current track
def play_track():
    global is_playing, length, current_time
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    length = pygame.mixer.Sound(music_files[current_track]).get_length()
    is_playing = True
    current_time = 0.0

#font
font = pygame.font.Font(None, 36) 
text_color = (0, 0, 0)

#first play to prevent errors
play_track()
pygame.mixer.music.pause()
is_playing = False

print("""Instructions:
      SPACE - play/pause
      RIGHT - next track
      LEFT - previous track
      UP - volume up
      DOWN - volume down""")
#main loop
while True:
    #exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            #pause
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
            #next
            elif event.key == pygame.K_RIGHT:
                next_clicked_frames_to_show_image = 20
                current_track = (current_track + 1) % len(music_files)
                play_track()
            #previous
            elif event.key == pygame.K_LEFT:
                previous_clicked_frames_to_show_image = 20
                current_track = (current_track - 1) % len(music_files)
                play_track()
            #volume
            elif event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)

    #main screen fill
    screen.fill(WHITE)
    pygame.draw.rect(screen, 'cyan', paint_rect)
    image_rect = image.get_rect(center=(width // 2, height // 2 - 150))
    screen.blit(image, image_rect)
    
    #draw buttons
    if is_playing:
        #pause
        pause_rect = pause.get_rect(center=(width // 2, height // 2 + 250))
        screen.blit(pause, pause_rect)
    else:
        #play
        play_rect = play.get_rect(center=(width // 2, height // 2 + 250))
        screen.blit(play, play_rect)
    #next
    next_rect = next.get_rect(center=(width // 2 + 150, height // 2 + 250))
    screen.blit(next, next_rect)
    #previous
    previous_rect = previous.get_rect(center=(width // 2 - 150, height // 2 + 250))
    screen.blit(previous, previous_rect)

    #next button clicked
    if next_clicked_frames_to_show_image > 0:
        screen.blit(next_clicked, next_rect)
        next_clicked_frames_to_show_image -= 1
        pygame.display.update()
    #previous button clicked
    if previous_clicked_frames_to_show_image > 0:
        screen.blit(previous_clicked, previous_rect)
        previous_clicked_frames_to_show_image -= 1
        pygame.display.update()

    #music timer
    if is_playing:
        current_time += 1 / FPS
        if current_time > length + 1:
            pygame.mixer.music.stop()
            pygame.mixer.music.play()
            current_time = 0.0
    
    #track info
    track_name = os.path.basename(music_files[current_track])
    music_name = font.render(track_name, True, text_color)
    screen.blit(music_name, (width // 2 - music_name.get_width() // 2, height // 2 - music_name.get_height() // 2 + 50))
    timer_now = font.render(str(int(current_time)), True, text_color)
    screen.blit(timer_now, (width // 2 - timer_now.get_width() // 2 - 200, height // 2 - timer_now.get_height() // 2 + 150))
    timer_end = font.render(str(int(length)), True, text_color)
    screen.blit(timer_end, (width // 2 - timer_end.get_width() // 2 + 200, height // 2 - timer_end.get_height() // 2 + 150))

    #volume info
    volume_to_show = font.render(f'Volume: {int(volume * 100)}', True, text_color)
    screen.blit(volume_to_show, (width // 2 - volume_to_show.get_width() // 2, height // 2 - volume_to_show.get_height() // 2 + 150))

    pygame.display.update()
    
    #frame rate
    clock.tick(FPS)