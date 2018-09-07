# exif_delete

All the photos you share online contain metadata. This meta data can include: the location the photo was taken, the time, and detailed information about your camera / phone.  Facebook and many other companies use this information to track you and learn things about you. But *you* should be in control of what information you share with the world.

Enter the `exif_delete` tool.

This is a simple Python script that I use to strip all of the metadata from my photos before I share them online.  It is lightweight, easy-to-use, and fast.  If you are like me, you take a lot of photos, and this tool will help protect your privacy.


## Installation

If you are familiar with Python, this script will work in Python version 2.6 through 3.5 and only requires one third-party library (`PIL`).  The installation is standard.

If you are new to Python, not to worry; very little installation is required.  You *will* need to have some (relatively modern) version of Python installed on your computer, and you will need access to the command line. Then you just have to install `PIL`, the Python Imaging Library.  One way of doing that is to use `pip`:

    pip install -r requirements.txt

Another option is to install using `setuptools`:

    python setup.py install

Then just run the script as in the section below.  If you run the script and get the error:

    ImportError: No module named PIL

Then you did not correctly install the `PIL` module, and will have to get that installed. Perhaps you got an error in the "pip install" line above?


## Usage

This is a simple commandline tool.  Just pass the script the name of the image file(s) you want to strip, and it will do the rest:

    python exif_delete.py /path/to/my/image.jpg
    
    python exif_delete.py image1.jpg image2.png image3.gif
    
    python exif_delete.py /path/to/*/my/images/*.jpg

By default, the script will create a new image file with `"_safe"` appended to the file name.  For instance, this:

    /full/path/to/image1234.jpg

Will become:

    /full/path/to/image1234_safe.jpg

However, if you want to just over-write the original image file by stripping all the EXIF data from it, you can add the `--replace` flag:

    python exif_delete.py --replace /path/to/my/image.jpg
