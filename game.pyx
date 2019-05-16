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
cimport cpython
import cyrandom
import numpy
import os
import time
cimport numpy
from PIL import Image
from copy import deepcopy,copy
from pygame.locals import QUIT,MOUSEMOTION,MOUSEBUTTONDOWN, KEYDOWN
from pygame import K_s,K_l

cdef loadraw(nump,tile):
    tiles = numpy.load(nump)
    if tile in tiles.files:
        return tiles[tile]

cdef tiletonparray(tile):
    x = pygame.surfarray.array2d(tile)
    return x

cdef savetiles(nump,tiles):
    nt = {x:tiletonparray(tiles[x]) for x in tiles}
    numpy.savez(nump,**nt)


cpdef numpysaveloadtest():
    test = {"hi":numpy.array(["hi","hello"]),"hello":numpy.array(["hello","world"])}
    savetiles("test",test)
    assert numpy.array_equal(loadraw("test.npz","hi"),test["hi"])
    assert numpy.array_equal(loadraw("test.npz","hello"),test["hello"])
    os.remove("test.npz")
    return True

# gets tile that the cords x y are in
cdef (int,int) ctile(int x, int y, int tilesize):
    if tilesize == 0 or x == 0 or y == 0:
        return (0,0)
    return (<int>floor(x/tilesize),<int>floor(y/tilesize))

cdef (int,int) tileloc(int tx, int ty, int tilesize):
    cdef (int,int) tilepos = (tx*tilesize,ty*tilesize)
    return tilepos

cdef draw(map,int tilesize):
    cdef int x,y,height = len(map),width = len(map[0])
    cdef int drawx,drawy
    newsurface = pygame.Surface((width*tilesize,height*tilesize))
    for y in range(height):
        for x in range(width):
            drawx,drawy = tileloc(x,y,tilesize)
            newsurface.blit(map[y][x],(drawx,drawy))
    return newsurface

DEF red = (255,0,0)
DEF blue = (0,0,255)
DEF green = (0,255,0)
DEF white = (255,255,255)
DEF black = (0,0,0)

cdef class Tile:
    cdef bint up,down,right,left
    cdef init(self,tilepic,up=False,down=False,right=False,left=False):
        self.tilepic = tilepic
        self.up,self.down,self.right,self.left = up,down,right,left

cdef blankmap(int size,tile=""):
    cdef int i,j
    out = []
    for i in range(size):
        blk = []
        for j in range(size):
            blk.append(tile)
        out.append(blk)
    return out
cdef text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
cdef nparraytotile(arra):
    return pygame.surfarray.make_surface(arra)


cdef loadmap(mapname,tilesloaded=[]):
    mapdata = numpy.load(mapname+".npz")
    tiles = mapdata["tiles"]
    tiles = tiles.tolist()
    nt = copy(tiles)
    cdef int index
    for b in tiles:
        index = nt.index(b)
        npr = numpy.array(tiles[index])
        nt[index] = nparraytotile(npr)
        tilesloaded.append(nt[index])
    map = mapdata["map"]
    newmap = map.tolist()
    cdef int x,y
    for y in range(len(map)):
        for x in range(len(map[0])):
            newmap[y][x] = nt[newmap[y][x]]
    return newmap,tilesloaded

cdef savemap(map,filename):
    tiles = []
    cdef int x,y
    new = numpy.array(map).tolist()
    for y in range(len(map)):
        for x in range(len(map[0])):
            tl = map[y][x]
            if tl in tiles:
                new[y][x] = tiles.index(tl)
            else:
                tiles.append(tl)
                new[y][x] = tiles.index(tl)
    newtiles = copy(tiles)
    for tile in tiles:
        newtiles[tiles.index(tile)] = tiletonparray(tile)
    numpy.savez(filename, tiles=newtiles, map=new)


cdef randmap(size,tiles):
    cdef int x,y
    out = []
    for y in range(size):
        tmp = []
        for x in range(size):
            tmp.append(cyrandom.choice(tiles))
        out.append(tmp)
    return out
cdef gettileatcords(x,y,size,map):
    cdef int tx,ty
    tx,ty = ctile(x,y,size)
    return map[y][x]
DEF mode = "mapmake" # What mode are we in? Are we making maps or playing the game?



cpdef main(int maxfps = 60,int sctile = 32,int tilesize = 16):
    """Main Game"""
    cdef (int,int) tilet = (tilesize,tilesize)
    cdef int mx = 0,my = 0,mtx = 0, mty = 0
    pygame.init()
    # screen is sctile/sctile tiles
    txtFont = pygame.font.Font('freesansbold.ttf',15)
    fps = 0
    tl = []
    background_colour = (255,255,255)
    (width, height) = (sctile*tilesize, sctile*tilesize)
    screen = pygame.display.set_mode((width, height))
    # setup colored tiles
    redtile = pygame.Surface(tilet)
    redtile.fill(red)
    bluetile = pygame.Surface(tilet)
    bluetile.fill(blue)
    greentile = pygame.Surface(tilet)
    greentile.fill(green)
    blacktile = pygame.Surface(tilet)
    blacktile.fill(black) # may be redundent
    whitetile = pygame.Surface(tilet)
    whitetile.fill(white)
    # end colored tiles
    pygame.display.set_caption('Window')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    clock = pygame.time.Clock()
    IF mode == "mapmake":
        mp = blankmap(sctile,whitetile) # make a blank map
    ELSE:
        mp = randmap(sctile,[blacktile,whitetile]) # load map code goes here
    while running:
        screen.fill(background_colour)
        screen.blit(draw(mp,tilesize),(0,0))
        TextSurf, TextRect = text_objects(str(fps), txtFont)
        TextRect.topleft = (0,0)
        screen.blit(TextSurf, TextRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEMOTION:
                mx,my = event.pos
                mtx,mty = ctile(mx,my,tilesize)
            if event.type == MOUSEBUTTONDOWN:
                try:
                    button = {3:"right",1:"left"}[event.button]
                except KeyError:
                    print("Ignoring Mouse Button {}".format(event.button))
                    continue
                if button == "left":
                    mp[mty][mtx] = blacktile
                elif button == "right":
                    mp[mty][mtx] = whitetile
            if event.type == KEYDOWN:
                if event.key == K_s:
                    s = time.time()
                    savemap(mp,"testmap")
                    e = time.time()
                    print("Saving took {} ms".format(e-s))
                if event.key == K_l:
                    s = time.time()
                    mp,tl = loadmap("testmap",tl)
                    e = time.time()
                    print("Loading took {} ms".format(e-s))
        clock.tick(maxfps)
        fps = round(clock.get_fps())

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
