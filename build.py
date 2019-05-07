from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import sys, glob, os

if sys.platform.startswith("win"):
    ext = "pyd"
else:
    ext = "so"

ext_modules = [Extension("game",["game.py"])]
setup(
    name = 'FeatherGame',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

built = glob.glob("game.cpython*."+ext)[0]
print("Built .{} file at {}".format(ext,built))


def mkdir(fld):
    if os.path.exists(fld):
        return
    else:
        os.mkdir(fld)
