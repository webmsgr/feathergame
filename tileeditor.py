"""Tileeditor.py, Import/ Export tiles"""
# @todo make tile editor
import numpy
from PIL import Image

def convert(tiledata):
    print(tiledata.shape)
    new = []
    for x in range(tiledata.shape[0]):
        newrow = []
        for y in range(tiledata.shape[1]):
            data = int(tiledata[y,x]).to_bytes(3,'big')
            r,g,b = data[:]
            newrow.append((r,g,b))
        new.append(newrow)
    return Image.fromarray(numpy.array(new), mode="RGB")
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
                r = r << 2*8
                g = g << 1*8
                newrgb = r + g + b
                nrow.append(newrgb)
            ntile.append(nrow)
        ntile = numpy.array(ntile)
        print(ntile)
        newtiles[tilename] = ntile

