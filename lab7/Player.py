import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Music Player')

# Set up fonts
font = pygame.font.SysFont(None, 24)

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize music mixer
pygame.mixer.init()

# Define some variables
playlist = ['a-promise(chosic.com).mp3', 'keys-of-moon-white-petals(chosic.com).mp3']  # List of music files
current_track = 0  # Index of currently playing track
playing = False  # Whether music is currently playing

def draw_text(text, font, surface, x, y, color):
    """Draw text on the given surface at the given position."""
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def play_music(track):
    """Play the specified music track."""
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()

def stop_music():
    """Stop the currently playing music."""
    pygame.mixer.music.stop()

def next_track():
    """Play the next track in the playlist."""
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music(playlist[current_track])

def previous_track():
    """Play the previous track in the playlist."""
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music(playlist[current_track])

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if playing:
                    stop_music()
                    playing = False
                else:
                    play_music(playlist[current_track])
                    playing = True
            elif event.key == K_n:
                next_track()
            elif event.key == K_p:
                previous_track()

    # Clear the window
    window_surface.fill(WHITE)

    # Display current status
    status_text = "Playing" if playing else "Paused"
    draw_text(status_text, font, window_surface, 10, 10, BLACK)
    draw_text("Press SPACE to play/pause", font, window_surface, 10, 40, BLACK)
    draw_text("Press N for next track", font, window_surface, 10, 70, BLACK)
    draw_text("Press P for previous track", font, window_surface, 10, 100, BLACK)

    # Update the display
    pygame.display.update()
