import argparse
parser = argparse.ArgumentParser(description='FeatherGame')
parser.add_argument("--fps",
                    help="Set max fps, default: 60",
                    type=int,
                    default=60)
parser.add_argument("--mapsize",
                    help="Set the size of map, (WILL BREAK THINGS MAYBE), default: 32",
                    type=int,
                    default=32)
parser.add_argument("--tilesize",
                    help="Set size of tiles, (WILL BREAK THINGS), default: 16",
                    type=int,
                    default=16)
args = parser.parse_args()
maxfps = args.fps
mapsize = args.mapsize
tilesize = args.tilesize
import game
game.main(maxfps,mapsize,tilesize)