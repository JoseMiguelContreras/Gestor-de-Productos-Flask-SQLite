class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aSQL(self):
        return (self.nombre, self.precio, self.cantidad)
