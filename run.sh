rm game.*.so
rm game.c
python3 build.py build_ext --inplace
python3 FeatherGame.py