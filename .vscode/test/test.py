"""Simple test for the get_rars script"""

import unittest


class Test1(unittest.TestCase):
    """Initial tests"""

    # -- Se ejecuta antes de cualquier test
    def setUp(self):
        """Configurar el test"""
        print("-> Setup!!")

    # -- Se ejecuta al finalizar cada test
    def tearDown(self):
        """Limpiar el test"""
        print("->Fin!")

    # --- All the test methods defined should start with
    # --- the name "test"

    def test_msg1(self):
        """Testing1"""

        a = True
        self.assertTrue(a)

    def test_msg2(self):
        """Testing2"""

        a = 5
        b = 5
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
