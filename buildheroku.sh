cythonize -3 --include-dir `python3 -c "import numpy; print(numpy.get_include())"` game.pyx
[ -f *.c ]
