"""FeatherGame"""


import pygame
from pygame.locals import QUIT

def main():
    """Main Game"""
    background_colour = (255,255,255)
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Window')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.display.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
