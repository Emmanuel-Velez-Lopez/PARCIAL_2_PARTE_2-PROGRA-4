import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.cliente import Cliente 
from modelo.factura import Factura
from modelo.producto import ProductoDeControl

class OperacionesCRUD:
    def __init__(self):
        self.clientes = []

    def crear_cliente_con_compra(self, nombre, cedula, factura):
        cliente_existente = self.buscar_cliente_por_cedula(cedula)
        if cliente_existente:
            cliente_existente.agregar_factura(factura)
        else:
            nuevo_cliente = Cliente(nombre, cedula)
            nuevo_cliente.agregar_factura(factura)
            self.clientes.append(nuevo_cliente)

    def buscar_cliente_por_cedula(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def vender_producto_de_control(self, cliente, producto):
        # Verificar si el cliente existe en la lista de clientes
        if cliente not in self.clientes:
            return "El cliente no existe en la base de datos."

        # Verificar si el producto es de control
        if not isinstance(producto, ProductoDeControl):
            return "El producto no es un producto de control."

        # Realizar la venta del producto al cliente
        cliente.agregar_producto(producto)
        return "Venta realizada exitosamente."
    
    def buscar_por_cedula(self, cedula):
        facturas_encontradas = []
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                facturas_encontradas.extend(cliente.facturas)
        return facturas_encontradas
