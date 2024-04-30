# modelo/historial_compras.py

class HistorialCompras:
    def __init__(self):
        self.historial = {}

    def agregar_factura(self, cliente, factura):
        if cliente not in self.historial:
            self.historial[cliente] = []
        self.historial[cliente].append(factura)
