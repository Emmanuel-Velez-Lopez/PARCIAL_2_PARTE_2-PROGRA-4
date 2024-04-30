import unittest
import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.cliente import Cliente
from modelo.factura import Factura
from crud.operaciones_crud import OperacionesCRUD

class TestOperacionesCRUD(unittest.TestCase):
    def setUp(self):
        self.operaciones_crud = OperacionesCRUD()

    def test_crear_cliente_con_compra(self):
        cliente = Cliente("Juan Perez", "1234567890")
        factura = Factura("2024-04-30")
        
        self.operaciones_crud.crear_cliente_con_compra(cliente.nombre, cliente.cedula, factura)
        
        # Verificar que el cliente se haya creado correctamente
        self.assertIn(cliente, self.operaciones_crud.clientes)
        # Verificar que la factura se haya asociado al cliente
        cliente_con_factura = self.operaciones_crud.buscar_cliente_por_cedula(cliente.cedula)
        self.assertIn(factura, cliente_con_factura.facturas)

if __name__ == '__main__':
    unittest.main()
