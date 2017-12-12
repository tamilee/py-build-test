##  To compile modules as cython  
##
## Sumeet Sandhu
## Copyright (C) 2013- Elementary IP LLC
#############################################

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("clusterPortfolio",  ["clusterPortfolio.py"]),
##    Extension("mymodule2",  ["mymodule2.py"]),
##   ... all your modules that need be compiled ...
]
setup(
    name = 'portfolio_generate',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
