from Producto import Producto
import SG as sg
def leer_inventario(nombre_archivo):
    

    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                instruccion, detalles = linea.strip().split(' ', 1)
                
                if instruccion == 'crear_producto':
                    nombre, cantidad, precio_unitario, ubicacion = detalles.split(';')
                    producto = Producto(nombre, int(cantidad), float(precio_unitario), ubicacion)
                    sg.listaProductos.insertar(producto)

        sg.listaProductos.recorrer()

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")


    def agregar_stock(self, nombre, cantidad, ubicacion):
        producto_existente = self.encontrar_producto(nombre, ubicacion)
        
        if producto_existente:
            producto_existente.cantidad += cantidad
            print(f"Se agregaron {cantidad} unidades de {nombre} a {ubicacion}")
        else:
            print(f"No se encontró el producto {nombre} en {ubicacion}")


def leer_movimientos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                instruccion, detalles = linea.strip().split(' ', 1)

                if instruccion == 'agregar_stock':
                    nombre, cantidad, ubicacion = detalles.split(';')
                    producto_existente = sg.listaProductos.buscar_producto(nombre, ubicacion)

                    if producto_existente:
                        sg.listaProductos.agregar_stock(nombre, ubicacion, int(cantidad))
                    else:
                        print(f"No se encontró el producto {nombre} en {ubicacion} para agregar stock")
                
                elif instruccion == 'vender_producto':
                    nombre, cantidad, ubicacion = detalles.split(';')
                    producto_existente = sg.listaProductos.buscar_producto(nombre, ubicacion)
                    
                    if producto_existente:
                        sg.listaProductos.vender_producto(nombre, ubicacion, int(cantidad))
                    else:
                        print(f"No se encontró el producto {nombre} en {ubicacion} para agregar stock")
        sg.listaProductos.recorrer()
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")


