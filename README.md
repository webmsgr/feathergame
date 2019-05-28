

# feathergame
A rpg written in python

# Builds
[![Build Status](https://semaphoreci.com/api/v1/webmsgr/feathergame/branches/master/badge.svg)](https://semaphoreci.com/webmsgr/feathergame) [![CircleCI](https://circleci.com/gh/webmsgr/feathergame.svg?style=svg)](https://circleci.com/gh/webmsgr/feathergame)
# Deploys
The latest deployed files can be found here:
+ [game.c](http://feathergame.herokuapp.com/game.c)
+ [game.pyx](http://feathergame.herokuapp.com/game.pyx)
+ [game.html](http://feathergame.herokuapp.com/game.html)

# Requirements
This project requires

+ python3
+ Cython
+ pygame
+ numpy
+ cyrandom

## Cloning
```
git clone https://github.com/webmsgr/feathergame.git
```
# Running/Building
First you install requirements.txt using
```
pip install -r requirements.txt
```
## Anything but windows
Simply run run.sh or build.sh if you dont want the game to autostart
## Windows
Build the game using
```
py -3 build.py build_ext --inplace
```
then run Feathergame.py

# Command Line Args
Use `FeatherGame.py -h` to see usage
# Gitpod
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/webmsgr/feathergame)
# Making tiles
**Currently Not Implemented**
## Image to tile
To make a tile, get a 16x16 image for the tile, and use
`tileediter.py --import image.png --to image`
This will import image.png to a tile called image
## Tile to image
To export a tile use
`tileeditor.py --export tile --to tile.png` to export the tile 'tile' to tile.png

## Other Commands:
see `tileediter.py -h`


# To contribute
To contribute, fork the repo and add your changes. Then submit a pull request.
# License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
