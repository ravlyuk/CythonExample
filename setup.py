from os.path import join
from glob import glob
from setuptools import Extension, setup

from Cython.Build import cythonize

source_files = []
for ext in ('*.c', '*.pyx'):
    source_files.extend(glob(join("cython_scripts", ext)))

extensions = [Extension("fibonacci_cython", source_files)]

setup(
    name='test',
    version='1.0',
    ext_modules=cythonize(extensions)
)
