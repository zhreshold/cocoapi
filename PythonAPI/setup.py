from __future__ import print_function
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext

# This hack delays importing cythonize until after setup_requires ensures that it exists.
class cythonize(list):
    def __init__(self, ext):
        self.ext = ext

    def __iter__(self):
        if self.ext is not None:
            from Cython.Build import cythonize
            list.__init__(self, cythonize(self.ext))
            self.ext = None
        return list.__iter__(self)

# hack to make sure numpy can be imported if numpy is not pre-installed
class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['src/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs = ['src'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

long_description = open('README.txt').read()

setup(name='pycocotools',
      license='FreeBSD',
      author='http://cocodataset.org/',
      description='Python APIs for MS COCO dataset.',
      long_description=long_description,
      packages=['pycocotools'],
      package_dir = {'pycocotools': 'pycocotools'},
      version='2.0.0.post2',
      url='https://github.com/zhreshold/cocoapi',
      setup_requires=['cython', 'setuptools>=18.0'],
      install_requires=['numpy', 'matplotlib'],
      cmdclass={'build_ext': build_ext},
      ext_modules=cythonize(ext_modules)
      )
