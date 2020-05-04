from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("C:\\Users\\Lenovo\\Desktop\\PROJECTS\\django_top2\\sth-knowledge\\source\\les_Python\\less_cython\\src\\uncompiled_lib.py")
)