import sys
if "-source" in sys.argv:
    import pyximport
    pyximport.install()

import game
game.main()