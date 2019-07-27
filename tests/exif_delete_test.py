from contextlib import redirect_stdout
from exif_delete import batch_exif_delete, exif_delete, usage, main as exif_main
from io import StringIO
import unittest


class ExifDeleteTester(unittest.TestCase):

    def test_usage(self):
        """ The script declares a usage() function that prints the help menu and exits. """
        f = StringIO()
        with redirect_stdout(f):
            self.assertRaises(SystemExit, usage)
        s = f.getvalue()

        assert s.strip().startswith("Purpose:")
        assert 'EXIF' in s
        assert s.strip().endswith(".png")

    def test_main_need_help(self):
        """ There are various, totally valid inputs you can give this script that will still result
        in the usage text being printed to std out and the system exiting.
        (All of these involve the user not passing an image file path.)
        """
        incomplete_inputs = [['-h'], ['--help'], ['-r'], ['--replace'], ['-help', '-r'],
                             ['--replace', '-h']]

        for incomplete_input in incomplete_inputs:
            f = StringIO()
            with redirect_stdout(f):
                self.assertRaises(SystemExit, exif_main, incomplete_input)
            s = f.getvalue()

            assert s.strip().startswith("Purpose:")
            assert 'EXIF' in s
            assert s.strip().endswith(".png")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
