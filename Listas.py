from Producto import Producto

class nodo:
  def __init__(self, Producto=None, siguiente=None):
    self.Producto = Producto
    self.siguiente = siguiente

class lista_enlazada:
  def __init__(self):
    self.primero = None

  def insertar(self, Producto):
    if self.primero is None:
      self.primero = nodo(Producto=Producto)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(Producto=Producto)

  def recorrer(self):
    actual = self.primero
    print("Datos: ")
    print("Producto     Cantidad        Precio Unitario     Valor Total     Ubicacion ")
    while actual != None:
      print(actual.Producto._nombre, "         ", actual.Producto._cantidad, "          ", actual.Producto._precioUnitario, "       ", (actual.Producto._cantidad * actual.Producto._precioUnitario), "              ", actual.Producto._ubicacion)
      actual = actual.siguiente

  def buscar_producto(self, nombre, ubicacion):
    actual = self.primero

    while actual:
        if actual.Producto._nombre == nombre and actual.Producto._ubicacion == ubicacion:
            print("Producto Econtrado: ", actual.Producto._nombre)
            return True            
        actual = actual.siguiente

    return False
  
  def agregar_stock(self, nombre, ubicacion, nueva_cantidad):
    actual = self.primero

    while actual:
        if actual.Producto._nombre == nombre and actual.Producto._ubicacion == ubicacion:
            actual.Producto._cantidad += nueva_cantidad
            print(f"Se agregaron {nueva_cantidad} unidades a {nombre}. Nueva cantidad: {actual.Producto._cantidad} en la ubicacion: {ubicacion}")
            return True
        actual = actual.siguiente

    print(f"No se encontró el producto {nombre} en el inventario.")
    return False



#   def eliminar(self, usuario):
#     actual = self.primero
#     anterior= None

#     while actual and actual.nota.usuario != usuario:
#       anterior = actual
#       actual = actual.siguiente

#     if anterior is None:
#       self.primero = actual.siguiente
#       actual.siguiente = None
#     elif actual:
#       anterior.siguiente = actual.siguiente
#       actual.siguiente = None

#   def buscar(self, usuario):
#     actual = self.primero
#     anterior= None

#     while actual and actual.nota.usuario != usuario:
#       anterior = actual
#       actual = actual.siguiente

#     if anterior is None:
#       self.primero = actual.siguiente
#       print("Usuario: ", actual.nota.usuario, "| Titulo: ", actual.nota.titulo, "| Libreta: ", actual.nota.libreta, "| Contenido: ", actual.nota.contenido, "| Fecha creacion:", actual.nota.fecha_creacion, "| Fecha modificacion: ", actual.nota.fecha_modificacion, "| Tipo acceso: ", actual.nota.tipo_acceso)
#     elif actual:
#       anterior.siguiente = actual.siguiente
#       print("Usuario: ", actual.nota.usuario, "| Titulo: ", actual.nota.titulo, "| Libreta: ", actual.nota.libreta, "| Contenido: ", actual.nota.contenido, "| Fecha creacion:", actual.nota.fecha_creacion, "| Fecha modificacion: ", actual.nota.fecha_modificacion, "| Tipo acceso: ", actual.nota.tipo_acceso)