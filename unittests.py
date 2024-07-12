import unittest
from tests import operaciones

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(operaciones(10, 6), (16, 4, 60, 1.6666666666666667))

if __name__ == '__main__':
    unittest.main()