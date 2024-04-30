import unittest
import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.factura import Factura

class TestFactura(unittest.TestCase):
    def test_creacion_factura(self):
        factura = Factura("2024-04-15", 100.0)
        self.assertEqual(factura.fecha_emision, "2024-04-15")
        self.assertEqual(factura.valor_total, 100.0)

if __name__ == '__main__':
    unittest.main()