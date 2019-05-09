"""FeatherGame"""


IF UNAME_SYSNAME == "Windows":
    DEF platform = "win"
ELIF UNAME_SYSNAME == "Darwin":
    DEF platform = "darwin"
ELIF UNAME_SYSNAME == "Linux":
    DEF platform = "linux"
ELSE:
    DEF platform = "unknown"


import pygame
from pygame.locals import QUIT

cpdef main():
    """Main Game"""
    DEF red = (255,0,0)
    DEF green = (0,255,0)
    DEF blue = (0,0,255)
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
