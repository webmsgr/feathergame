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

cs = glob.glob("*.c")
built = [glob.glob("{}.cpython*.{}".format(i.split(".")[0],ext))[0] for i in cs]
builtmess = ["{}.py -> {} -> {}".format(cs[i].split(".")[0],cs[i],built[i]) for i in range(len(cs))]
print("Built {} .{} file(s) ({})".format(len(built),ext,','.join(builtmess)))


def mkdir(fld):
    if os.path.exists(fld):
        return
    else:
        os.mkdir(fld)
