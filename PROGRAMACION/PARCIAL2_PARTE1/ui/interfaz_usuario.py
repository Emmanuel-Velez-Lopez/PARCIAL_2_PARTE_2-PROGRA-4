import sys

sys.path.append("PARCIAL2_PARTE1") 
from modelo.cliente import Cliente 
from modelo.factura import Factura
from modelo.producto import ProductoDeControl
from crud.operaciones_crud import OperacionesCRUD


class InterfazUsuario:
    def __init__(self):
        self.operaciones_crud = OperacionesCRUD()

    def vender_producto_de_control(self):
        # Obtener los datos del cliente y el producto de control
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cedula_cliente = input("Ingrese la cédula del cliente: ")
        registro_ica = input("Ingrese el registro ICA del producto: ")
        nombre_producto = input("Ingrese el nombre del producto: ")
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación del producto: ")
        valor_producto = float(input("Ingrese el valor del producto: "))

        # Crear el cliente y el producto de control
        cliente = Cliente(nombre_cliente, cedula_cliente)
        producto = ProductoDeControl(registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto)

        # Realizar la venta del producto de control
        resultado = self.operaciones_crud.vender_producto_de_control(cliente, producto)
        print(resultado)
