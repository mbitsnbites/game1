#!/usr/bin/env python3

import pygame

def main():
    # Initialize the pygame module.
    pygame.init()

    # Set the application icon and title.
    icon = pygame.image.load("icon_128x128.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("My game")
     
    # Create a surface on screen that has the size of 1024 x 768.
    screen = pygame.display.set_mode((1024, 768))
     
    # Main loop.
    running = True
    while running:
        # Event handling: get all events from the eventqueue.
        for event in pygame.event.get():
            # Only do something if the event is of type QUIT.
            if event.type == pygame.QUIT:
                # Stop the main loop.
                running = False
     
     
# Run the main function only if this module is executed as the main script.
if __name__=="__main__":
    main()

