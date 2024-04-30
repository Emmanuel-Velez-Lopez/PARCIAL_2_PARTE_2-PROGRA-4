class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    def calcular_total(self):
        total = sum(producto.valor for producto in self.productos)
        return total