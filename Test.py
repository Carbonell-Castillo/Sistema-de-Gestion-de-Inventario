import Listas as listas
from Producto import Producto
import SG as sg

producto1 = Producto("Producto A", 10, 15.99, "Estante 1")
producto2 = Producto("Producto B", 10, 15.99, "Estante 1")
sg.listaProductos.insertar(producto1)
sg.listaProductos.insertar(producto2)
sg.listaProductos.recorrer()
