# COCOAPI for PyPI

This fork is used for deploying pycocotools to PyPI.

It combines:

- original cocoapi https://github.com/cocodataset/cocoapi
- windows fix: https://github.com/philferriere/cocoapi

Therefore source dist build is enabled across platforms (make sure you have Visual C++ installed on Windows)

Note that build from ``sdist`` without ``cython`` and ``numpy`` is slow because they will be built temporarily upon setup.
