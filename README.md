# exif_delete

All the photos you share online contain metadata. This metadata can include:

* the location the photo was taken
* the time the photo was taken
* detailed information about your camera / phone

Facebook (and the other online advertisers) make money by tracking and selling your personal information. But *you* should be in control of what information you share with the world.

Enter the `exif_delete` tool.

This is a simple Python script that I use to strip all of the metadata from my photos before I share them online.  It is lightweight, easy-to-use, and fast.  If you are like me, you take a lot of photos, and this tool will help protect your privacy.


## Installation

This script will work with Python v3.3 to v3.7 and only requires one third-party library: `PIL`.

To install from local source:

    python setup.py install


## Usage

This is a simple commandline tool.  Just pass the name of the image file(s) you want to strip to the script, and it will do the rest:

    python exif_delete.py /path/to/my/image.jpg

    python exif_delete.py image1.jpg image2.png image3.gif

    python exif_delete.py /path/to/*/my/images/*.jpg

By default, the script will create a new image file with `"_safe"` appended to the file name.  For instance, this:

    /full/path/to/image1234.jpg

Will become:

    /full/path/to/image1234_safe.jpg

However, if you want to just over-write the original image file by stripping all the EXIF data from it, you can add the `--replace` flag:

    python exif_delete.py --replace /path/to/my/image.jpg
