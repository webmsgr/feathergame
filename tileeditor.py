"""Tileeditor.py, Import/ Export tiles"""
# @todo make tile editor
import numpy
from PIL import Image
import struct
import argparse
import sys
import os
def convert(tiledata):
    new = []
    for x in range(tiledata.shape[0]):
        newrow = []
        for y in range(tiledata.shape[1]):
            data = int(tiledata[y,x]).to_bytes(3,'big')
            r,g,b = data[0],data[1],data[2]
            newrow.append((r,g,b))
        new.append(newrow)
    i = Image.new("RGB",(16,16))
    idata = i.load()
    ix = 0
    for x in new:
        iy = 0
        for y in x:
            idata[ix,iy] = y
            iy += 1
        ix += 1
    return i
def loadtiles(tilefile):
    out = {}
    try:
        with numpy.load(tilefile) as i:
            for file in i.files:
                out[file] = convert(i[file])
        return out
    except FileNotFoundError:
        return {}

def savetiles(tilefile,tiles):
    newtiles = {}
    for tile in tiles:
        tilename = tile
        tile = tiles[tile]
        ntile = numpy.array(tile)
        ntilearray = ntile.tolist()
        nntile = []
        x = 0
        for col in ntilearray:
            y = 0
            nrow = []
            for row in col:
                nrow.append(int.from_bytes(struct.pack(">BBB",row[0],row[1],row[2]),"big"))
                y += 1
            x += 1
            nntile.append(nrow)
        ntile = numpy.array(nntile,numpy.int32)
        newtiles[tilename] = ntile
    print(newtiles)
    numpy.savez(tilefile,**newtiles)


parser = argparse.ArgumentParser(description="Tile editor")
parser.add_argument("--tilefile",default="tiles.npz",help="The tile file to use")
actionGroup = parser.add_mutually_exclusive_group()
actionGroup.add_argument("-i","--importimage",metavar="inputfile",help="Image to tile")
actionGroup.add_argument("-x","--exporttile",metavar="tile",help="Tile to image")
actionGroup.add_argument("-l","--list",action="store_true",help="List all tiles")
parser.add_argument("-to",help="destination",required="-i" in sys.argv or "-x" in sys.argv, metavar="file/tile")
out = parser.parse_args()
if not out.importimage and not out.exporttile and not out.list:
    parser.error("-i or -x or -l is required")
#if out.importimage and not out.totile:
#    parser.error("-i requires --totile")
#if out.exporttile and not out.tofile:
#    parser.error("-x requires --tofile")

print("Loading tile file...",end=" ")
tiles = loadtiles(out.tilefile)
print("Done")
if out.list:
    print("Tiles:")
    i = 0
    for tile in tiles:
        print(tile)
        i += 1
    print("Found {} tiles".format(i))
if out.exporttile:
    tile = out.exporttile
    if not tile in tiles:
        print("Tile not found!")
        sys.exit(1)
    else:
        tile = tiles[tile]
        print("Exporting...",end=" ")
        tile.save(out.to)
        print("Done!")
if out.importimage:
    if os.path.exists(out.importimage):
        image = Image.open(out.importimage)
        if out.to in tiles:
            print("Tile exists! Overwrite?")
            override = input("y/n?")
            if override in ["y","Y","yes"]:
                print("Overwriting...")
            elif override in ["n","N","no"]:
                print("Cancled")
                sys.exit(1)
            else:
                print("unknown option...")
                sys.exit(1)
        print("Adding tile...",end=" ")
        tiles[out.to] = image
        savetiles(out.tilefile,tiles)
        print("Done!")
    else:
        print("File not found!")
#print(savetiles("",loadtiles("tiles.npz")))