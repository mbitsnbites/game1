#!/usr/bin/env python3

import math
import os
import pygame
import sys


# Game and data directories.
GAME_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(GAME_DIR, 'data')

# Screen settings.
WINDOW_RESOLUTION = (1024, 768)
USE_FULLSCREEN = False    # Set this to True for fullscreen mode.


def main():
    # Initialize the pygame module.
    pygame.init()

    # Set the application icon and title.
    icon = pygame.image.load(os.path.join(DATA_DIR, 'icon.png'))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('My game')

    # Create the screen surface (the game window).
    res = WINDOW_RESOLUTION
    flags = pygame.DOUBLEBUF | pygame.HWSURFACE;
    if USE_FULLSCREEN:
        res = (0, 0)
        flags = flags | pygame.FULLSCREEN
    screen = pygame.display.set_mode(res, flags)

    # Get the real size of the window (important in fullscreen mode).
    res = screen.get_size()

    # Load game data.
    spaceship = pygame.image.load(os.path.join(DATA_DIR, 'spaceship.png'))
     
    # Main loop.
    running = True
    while running:
        # Get the current time (convert milliseconds to seconds).
        t = pygame.time.get_ticks() * 0.001

        # Event handling: Get all events from the eventqueue.
        for event in pygame.event.get():
            # Should we quit?
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # Stop the main loop.
                running = False

        # Clear the screen with a background color.
        screen.fill((50, 80, 100))

        # Draw a spaceship :-)
        screen.blit(spaceship, (500+200*math.sin(t), 400))

        # When we're done painting to the screen, flip front/back buffers.
        pygame.display.flip()


    # Stop the program.
    pygame.quit()
    sys.exit()


# Run the main function only if this module is executed as the main script.
if __name__=="__main__":
    main()

