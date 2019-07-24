''' Install with:  python setup.py install_scripts
'''

from setuptools import setup

readme_file = open("README.md", "r").read()

setup(
    name = "exif_delete",
    version = "0.9.1",
    author = "John Stilley",
    description = ("A simple commandline tool to remove the EXIF data from image files."),
    license = "GPLv3",
    keywords = "exif tool python",
    url = "https://github.com/theJollySin/exif_delete",
    long_description=readme_file,
    install_requires=['pillow>=1.1.0'],
    entry_points={'console_scripts': ['exif_delete=exif_delete:main']},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Security"
    ],
)
