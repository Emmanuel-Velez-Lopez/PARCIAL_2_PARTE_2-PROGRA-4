import unittest
import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.cliente import Cliente
from modelo.factura import Factura
from crud.operaciones_crud import OperacionesCRUD

class TestOperacionesCRUD(unittest.TestCase):
    def test_crear_cliente_con_compra(self):
        # Crear instancias de factura y cliente
        factura = Factura(fecha="2024-04-30", valor_total=150.0)
        cliente = Cliente(nombre="Juan", cedula="123456789")

        # Crear operaciones CRUD y agregar cliente con compra
        operaciones_crud = OperacionesCRUD()
        operaciones_crud.crear_cliente_con_compra(cliente.nombre, cliente.cedula, factura)

        # Verificar que el cliente se agregó correctamente
        self.assertIn(cliente, operaciones_crud.clientes)

        # Verificar que la factura se agregó al cliente correctamente
        cliente_encontrado = operaciones_crud.buscar_cliente_por_cedula(cliente.cedula)
        self.assertIsNotNone(cliente_encontrado)
        self.assertIn(factura, cliente_encontrado.facturas)

if __name__ == "__main__":
    unittest.main()
