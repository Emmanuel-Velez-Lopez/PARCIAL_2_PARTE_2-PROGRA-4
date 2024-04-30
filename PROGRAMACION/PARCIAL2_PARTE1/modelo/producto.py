
class Producto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

class ProductoDeControl(Producto):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, valor):
        super().__init__(nombre, valor)
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion
