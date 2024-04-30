import unittest
import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.historial_compras import HistorialCompras
from modelo.cliente import Cliente
from modelo.factura import Factura

class TestHistorialCompras(unittest.TestCase):
    def setUp(self):
        self.historial = HistorialCompras()
        self.cliente = Cliente("Juan Perez", "1234567890")
        self.factura = Factura("2024-04-15", 100.0)

    def test_agregar_factura(self):
        self.historial.agregar_factura(self.cliente, self.factura)
        self.assertIn(self.cliente, self.historial.historial)
        self.assertIn(self.factura, self.historial.historial[self.cliente])

if __name__ == '__main__':
    unittest.main()
