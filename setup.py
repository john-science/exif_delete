''' exif_delete

Install by building locally with:

python setup.py install
'''
from setuptools import setup

readme = open('README.md', 'r').read()

setup(
    name = "exif_delete",
    version = "0.9.5",
    author = "John Stilley",
    description = "A simple commandline tool to remove the EXIF data from image files.",
    license = "GPLv3",
    keywords = "tool security privacy images exif",
    url = "https://github.com/theJollySin/exif_delete",
    long_description=readme,
    install_requires=['pillow>=1.1.0'],
    py_modules=["exif_delete"],
    entry_points={'console_scripts': ['exif_delete=exif_delete:main']},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Security"
    ],
)
