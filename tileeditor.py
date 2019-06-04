"""Tileeditor.py, Import/ Export tiles"""
# @todo make tile editor
import numpy
from PIL import Image
import struct
import argparse
import sys
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
    with numpy.load(tilefile) as i:
        for file in i.files:
            out[file] = convert(i[file])
    return out

def savetiles(tilefile,tiles):
    newtiles = {}
    for tile in tiles:
        tilename = tile
        tile = tiles[tile]
        tiledata = tile.convert()
        size = tile.size
        ntile = []
        for x in range(size[0]):
            nrow = []
            for y in range(size[1]):
                r,g,b = tiledata.getpixel((x,y))
                # @todo fix tile saving.
                # @body the first row is fine,but the others are strange
                newrgb = struct.pack(">BBB",r,g,b)
                nrow.append(int.from_bytes(newrgb,"big"))
            ntile.append(nrow)
        ntile = numpy.array(ntile)
        print(ntile)
        newtiles[tilename] = ntile
parser = argparse.ArgumentParser(description="Tile editor")
parser.add_argument("--tilefile",default="tiles.npz")
actionGroup = parser.add_mutually_exclusive_group()
actionGroup.add_argument("-i","--importimage",metavar="inputfile")
actionGroup.add_argument("-x","--exporttile",metavar="tile")
actionGroup.add_argument("-l","--list",action="store_true")
parser.add_argument("-to", required="-i" in sys.argv or "-x" in sys.argv, metavar="file/tile")
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
    else:
        tile = tiles[tile]
        print("Exporting...",end=" ")
        tile.save(out.to)
        print("Done!")

#print(savetiles("",loadtiles("tiles.npz")))