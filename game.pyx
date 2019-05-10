"""FeatherGame"""


IF UNAME_SYSNAME == "Windows":
    DEF platform = "win"
ELIF UNAME_SYSNAME == "Darwin":
    DEF platform = "darwin"
ELIF UNAME_SYSNAME == "Linux":
    DEF platform = "linux"
ELSE:
    DEF platform = "unknown"

from libc.math cimport floor
import pygame
from pygame.locals import QUIT
# gets tile that the cords x y are in
cdef (int,int) ctile(int x, int y, int tilesize):
    cdef (int,int) out = (<int>floor(x/tilesize),<int>floor(y/tilesize))
    return out

cdef (int,int) tileloc(int tx, int ty, int tilesize):
    cdef (int,int) tilepos = (tx*tilesize,ty*tilesize)
    return tilepos

cdef draw(map,tiles,int tilesize):
    cdef int x,y,height = len(map),width = len(map[0])
    cdef int drawx,drawy
    newsurface = pygame.Surface((width*tilesize,height*tilesize))
    for y in range(height):
        for x in range(width):
            drawx,drawy = tileloc(x,y,tilesize)
            newsurface.blit(tiles[map[y][x]],(drawx,drawy))
    return newsurface
cdef blankmap(int size,tile=""):
    cdef int i,j
    out = []
    for i in range(size):
        blk = []
        for j in range(size):
            blk.append(tile)
        out.append(blk)
    return out
cpdef main():
    """Main Game"""
    DEF maxfps = 60
    DEF red = (255,0,0)
    DEF green = (0,255,0)
    DEF blue = (0,0,255)
    DEF white = (255,255,255)
    DEF black = (0,0,0)
    DEF sctile = 8
    DEF tilesize = 8
    # screen is sctile/sctile tiles
    background_colour = (255,255,255)
    (width, height) = (sctile*tilesize, sctile*tilesize)
    screen = pygame.display.set_mode((width, height))
    blanksurface = pygame.Surface((tilesize,tilesize))
    blanksurface.fill(red)
    blank = blankmap(sctile)
    pygame.display.set_caption('Window')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(background_colour)
        screen.blit(draw(blank,{"":blanksurface},tilesize),(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                print(fps)
        clock.tick(maxfps)
        fps = clock.get_fps()
    pygame.display.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
