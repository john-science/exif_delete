from contextlib import redirect_stdout
from exif_delete import batch_exif_delete, exif_delete, main, usage
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
        assert s.strip().endswith(".png")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
