import tkinter as tk
from tkinter import filedialog
import Listas as listas

listaProductos = listas.lista_enlazada()
def showMenu():
    while True:
        print("-------------------------------------------------")
        print("Practica 1 - Lenguajes formales y de programacion")
        print("-------------------------------------------------")
        print("# Sistema de inventario\n")
        print("1. Cargar Inventario inicial")
        print("2. Cargar Instrucciones de movimientos")
        print("3. Crear Informe de inventario")
        print("4. Salir\n")

        try:
            option = int(input("Ingrese una opción: "))
            if 1 <= option <= 4:
                return option
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")


def open_file():
    ventana = tk.Tk()
    ventana.withdraw()

    # Definir los tipos de archivo permitidos (por ejemplo, solo archivos CSV y TXT)
    tipos_archivo_permitidos = [("Archivos de Inventario", "*.inv"), ("Archivos de Movimientos", "*.mov")]

    # Abrir la ventana de selección de archivo con los tipos de archivo permitidos
    ruta_archivo = filedialog.askopenfilename(filetypes=tipos_archivo_permitidos)

    # Mostrar la ruta del archivo seleccionado (esto es opcional)
    if ruta_archivo:
        print("Archivo seleccionado:", ruta_archivo)
        return ruta_archivo
    else:
        print("Ningún archivo seleccionado")
        return None