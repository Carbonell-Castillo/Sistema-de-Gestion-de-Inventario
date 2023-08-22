class Producto:
    def __init__(self, nombre, cantidad, precioUnitario, ubicacion):
        self._nombre = nombre
        self._cantidad = cantidad
        self._precioUnitario = precioUnitario
        self._ubicacion = ubicacion

    # Métodos Getter
    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precioUnitario(self):
        return self._precioUnitario

    def get_ubicacion(self):
        return self._ubicacion

    # Métodos Setter
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precioUnitario(self, precioUnitario):
        self._precioUnitario = precioUnitario

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion