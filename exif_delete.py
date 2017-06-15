"""
Purpose:

    This is a simple tool to allow you to delete all the metadata (EXIF data) from your images.

Flags:

    -r  (Optional)  Use this flag if you want to over-write the original file with the new
                    metadata-free version.
                    By default, the files are not replaced.

Usage:

    python exif_delete.py /path/to/image1.jpg
    python exif_delete.py /path/to/image1.jpg /path/to/image2.png image3.gif
    python exif_delete.py /path/to/images_*.jpg
    python exif_delete.py -r /path/to/images_*.png
    python exif_delete.py --replace /path/to/images_*.png
"""

# standard libraries
import os
import sys
# third-party libraries
from PIL import Image


def main():
    ''' main function to allow the user to treat this as a stand-alone tool
    '''
    images = []
    replace = False

    # commandline parsing
    for i in range(1, len(sys.argv)):
        if sys.argv[i].lower() in ['-r', '--r', '-replace', '--replace']:
            replace = True
        elif sys.argv[i].lower() in ['-h', '--h', '-help', '--help']:
            usage()
        else:
            images.append(sys.argv[i])

    # error if no files are passed to the script
    if len(images) < 1:
        usage()

    # do the heavy lifting
    batch_exif_delete(images, replace)


def usage():
    ''' Print a help menu to the screen, if the user enters a bad command line flag.
    '''
    print(__doc__)
    exit()


def batch_exif_delete(images, replace):
    ''' Remove the EXIF data from a list of images.
        If the `replace` flag is set to True, then the new path is the same
        as the original path. If now, the file name will have "_safe"
        appended to it.
    '''
    for original_image_path in images:
        # validate that the file exists
        if not os.path.exists(original_image_path):
            print('ERROR: File Not Found. ' + str(original_file_path))
            continue

        # build output file name
        if replace:
            new_image_path = original_image_path
        else:
            base_path, ext = os.path.splitext(original_image_path)
            new_image_path = base_path + "_safe" + ext

        # create new image file, with stripped EXIF data
        exif_delete(original_image_path, new_image_path)


def exif_delete(original_file_path, new_file_path):
    ''' Read an image file and write a new one,
        that lacks the original metadata.
    '''
    # open input image file
    try:
        original = Image.open(open(original_file_path))
    except IOError:
        print('ERROR: Problem reading image file. ' + str(original_file_path))

    # create output image, forgetting the EXIF metadata
    stripped = Image.new(original.mode, original.size)
    stripped.putdata(list(original.getdata()))
    stripped.save(new_file_path)


if __name__ == '__main__':
    main()
