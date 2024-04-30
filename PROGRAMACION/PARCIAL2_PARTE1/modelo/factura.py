class Factura:
    def __init__(self, fecha, valor_total=0.0):
        self.fecha = fecha
        self.valor_total = valor_total
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
