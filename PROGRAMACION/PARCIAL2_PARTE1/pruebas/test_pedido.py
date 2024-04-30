import unittest
import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.pedido import Pedido
from modelo.cliente import Cliente
from modelo.producto import Producto

class TestPedido(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Juan Perez", "1234567890")
        self.productos = [
            Producto("12345", "Fertilizante A", "cada 15 días", 50.0),
            Producto("67890", "Control de Plagas B", "cada 30 días", 70.0)
        ]
        self.pedido = Pedido(self.cliente, self.productos)

    def test_calculo_total(self):
        total_esperado = 120.0  # 50.0 + 70.0
        self.assertEqual(self.pedido.calcular_total(), total_esperado)

if __name__ == '__main__':
    unittest.main()
