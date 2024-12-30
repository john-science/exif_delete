import os
import shutil
import unittest
from contextlib import redirect_stdout
from io import StringIO
from random import randint

from PIL import Image

from exif_delete import batch_exif_delete, exif_delete, usage
from exif_delete import main as exif_main


class ExifDeleteTester(unittest.TestCase):

    def test_usage(self):
        """The script declares a usage() function that prints the help menu and exits."""
        f = StringIO()
        with redirect_stdout(f):
            self.assertRaises(SystemExit, usage)
        s = f.getvalue()

        assert s.strip().startswith("This is a simple tool")
        assert "EXIF" in s
        assert s.strip().endswith(".png")

    def test_main_need_help(self):
        """There are various, totally valid inputs you can give this script that will still result
        in the usage text being printed to std out and the system exiting.

        (All of these involve the user not passing an image file path.)
        """
        incomplete_inputs = [
            ["-h"],
            ["--help"],
            ["-r"],
            ["--replace"],
            ["-help", "-r"],
            ["--replace", "-h"],
        ]

        for incomplete_input in incomplete_inputs:
            f = StringIO()
            with redirect_stdout(f):
                self.assertRaises(SystemExit, exif_main, incomplete_input)
            s = f.getvalue()

            assert s.strip().startswith("This is a simple tool")
            assert "EXIF" in s
            assert s.strip().endswith(".png")

    def test_exif_delete_missing_file(self):
        """Try to run the exif_delete a file that doesn't exist."""
        f = StringIO()
        with redirect_stdout(f):
            exif_delete("fake.jpg", "fake_safe.jpg")
        s = f.getvalue()

        assert s.strip().startswith("ERROR")
        assert "Problem reading image file" in s

    def test_batch_exif_delete_missing_files(self):
        """Try to run the batch_exif_delete a file that doesn't exist."""
        f = StringIO()
        with redirect_stdout(f):
            batch_exif_delete(["fake.jpg"], True)
        s = f.getvalue()

        assert s.strip().startswith("Remov")
        assert "File Not Found" in s

    def test_exif_delete(self):
        """Run a real test of the primary exif_delete function."""
        # find the path to this script
        this_scripts_path = os.path.dirname(os.path.abspath(__file__))

        # find the path to the test image file
        repo_image_path = os.path.join(this_scripts_path, "resources", "nemo.jpg")

        # create a temporary directory for this test
        new_dir = os.path.join(
            this_scripts_path, ".test_{0}".format(randint(999, 999999))
        )
        while os.path.exists(new_dir):
            new_dir = os.path.join(
                this_scripts_path, ".test_{0}".format(randint(999, 999999))
            )

        # make the new directory, and copy the test file into place
        os.makedirs(new_dir)
        new_image_path = os.path.join(new_dir, "nemo.jpg")
        shutil.copy(repo_image_path, new_image_path)

        # run the actual code to remove the EXIF data from the file
        safe_image_path = new_image_path[:-4] + "_safe.jpg"
        exif_delete(new_image_path, safe_image_path)

        # Do the output files exist where we think they should be?
        assert os.path.exists(new_image_path)
        assert os.path.exists(safe_image_path)

        # Validate EXIF data in both files.
        old_img = Image.open(new_image_path)
        old_exif = old_img._getexif()
        assert type(old_exif) is dict
        assert len(list(old_exif.keys())) > 0

        new_img = Image.open(safe_image_path)
        new_exif = new_img._getexif()
        assert new_exif is None

        # do some cleanup
        shutil.rmtree(new_dir)

    def test_batch_exif_delete(self):
        """Run a real test of the primary batch_exif_delete function."""
        # find the path to this script
        this_scripts_path = os.path.dirname(os.path.abspath(__file__))

        # find the path to the test image file
        repo_image_path = os.path.join(this_scripts_path, "resources", "nemo.jpg")

        # try the test for replace True and False
        for replace in [False, True]:
            # create a temporary directory for this test
            new_dir = os.path.join(
                this_scripts_path, ".test_{0}".format(randint(999, 999999))
            )
            while os.path.exists(new_dir):
                new_dir = os.path.join(
                    this_scripts_path, ".test_{0}".format(randint(999, 999999))
                )

            # make the new directory, and copy the test file into place
            os.makedirs(new_dir)
            new_image_path = os.path.join(new_dir, "nemo.jpg")
            shutil.copy(repo_image_path, new_image_path)

            # run the actual code to remove the EXIF data from the file
            batch_exif_delete([new_image_path], replace)

            # Did it work?
            assert os.path.exists(new_image_path)

            # Validate EXIF data in both files.
            if replace:
                old_img = Image.open(new_image_path)
                old_exif = old_img._getexif()
                assert old_exif is None

            # do some cleanup
            shutil.rmtree(new_dir)


if __name__ == "__main__":
    unittest.main()
