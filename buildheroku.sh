cython -3 --I "`python3 -c 'import numpy; print(numpy.get_include())'`" game.pyx
[ -f *.c ]
