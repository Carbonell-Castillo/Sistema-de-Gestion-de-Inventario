import tkinter as tk
from tkinter import filedialog

# Crear una ventana de tkinter sin mostrarla
ventana = tk.Tk()
ventana.withdraw()

# Abrir la ventana de selección de archivo
ruta_archivo = filedialog.askopenfilename()

# Mostrar la ruta del archivo seleccionado (esto es opcional)
if ruta_archivo:
    print("Archivo seleccionado:", ruta_archivo)
else:
    print("Ningún archivo seleccionado")
