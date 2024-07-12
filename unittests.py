import unittest
from tests import operaciones

class TestOperaciones(unittest.TestCase):

    """
    Test para la funcion operaciones, usando la libreria unittest, se evalua si la suma de 10 y 6 es igual a 16, la resta es igual a 4,
    la multiplicacion es igual a 60 y la division es igual a 1.6666666666666667.
    """
    def test_suma(self):
        self.assertEqual(operaciones(10, 6), (16, 4, 60, 1.6666666666666667))

if __name__ == '__main__':
    unittest.main()