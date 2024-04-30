import unittest
import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.producto import Producto  

class TestProducto(unittest.TestCase):
    def test_creacion_producto(self):
        producto = Producto("12345", "Fertilizante A", "cada 15 días", 50.0)
        self.assertEqual(producto.registro_ica, "12345")
        self.assertEqual(producto.nombre, "Fertilizante A")
        self.assertEqual(producto.frecuencia_aplicacion, "cada 15 días")
        self.assertEqual(producto.valor, 50.0)

if __name__ == '__main__':
    unittest.main()