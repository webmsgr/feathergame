"""Build code with cpython"""


import sys
import glob
import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

if sys.platform.startswith("win"):
    EXT = "pyd"
else:
    EXT = "so"

EXT_MOD = cythonize([Extension("game", ["game.pyx"])],compiler_directives={"language_level":"3"})
setup(
    name='FeatherGame',
    cmdclass={'build_ext': build_ext},
    ext_modules=EXT_MOD
)

CS = glob.glob("*.c")
BUILT = [glob.glob("{}.*.{}".format(i.split(".")[0], EXT))[0] for i in CS]
BUILT_MESSAGES = ["{}.pyx -> {} -> {}".format(CS[i].split(".")[0], CS[i], BUILT[i]) for i in range(len(CS))]
print("Built {} .{} file(s) ({})".format(len(BUILT), EXT, ','.join(BUILT_MESSAGES)))


def mkdir(fld):
    """Make a directory"""
    if os.path.exists(fld):
        return
    os.mkdir(fld)
