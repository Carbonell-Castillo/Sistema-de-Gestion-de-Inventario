import tkinter as tk
from tkinter import filedialog
import SG as sg ##Super global
import Producto as producto
import Logic as logic


if __name__ == "__main__":
    
    while True:
        option = sg.showMenu()

        if option == 1:
            inventario_inicial = sg.open_file()        
            if inventario_inicial:
                print("Cargando Inventario inicial desde:", inventario_inicial)
                logic.leer_inventario(inventario_inicial)

        elif option == 2:
            instrucciones_movimientos = sg.open_file()
            if instrucciones_movimientos:
                print("Cargando Instrucciones de movimientos desde:", instrucciones_movimientos)
                logic.leer_movimientos(instrucciones_movimientos)
        
        elif option == 3:
            informe_inventario = sg.open_file()
            if informe_inventario:
                print("Creando Informe de inventario con el archivo:", informe_inventario)
        elif option == 4:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



