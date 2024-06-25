"""Testing the get_rars modules"""

import unittest
from unittest.mock import patch
from io import StringIO


# -- Module to test
import get_rars as gr


class TestInitial(unittest.TestCase):
    """Initial tests"""

    # -- Redirect the standard output
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_output(self, stdout):
        """Testing the output of the main function"""

        # -- Function to test
        gr.main()

        # -- Read its stdoutput
        output = stdout.getvalue()

        # -- Check the output
        self.assertEqual(output, "Hola...\n")


if __name__ == "__main__":
    unittest.main()
