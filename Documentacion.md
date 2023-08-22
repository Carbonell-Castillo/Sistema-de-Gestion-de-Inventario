## Manual Técnico del Sistema de Inventario

Este manual técnico proporciona una descripción detallada de la lógica y el funcionamiento interno del sistema de inventario implementado en los archivos `SG.py`, `Producto.py`, `Main.py`, `logic.py` y `listas.py`. El sistema está diseñado para gestionar un inventario de productos y llevar a cabo movimientos de stock utilizando archivos de texto como fuente de datos.

## Contenido

1. **Introducción**
2. **Estructura del Código Fuente**
   - `SG.py`: Interfaz de Usuario
   - `Producto.py`: Clase Producto
   - `Main.py`: Programa Principal
   - `logic.py`: Lógica de Movimientos
   - `listas.py`: Estructura de Datos
3. **Flujo del Programa**
   - Carga de Inventario Inicial
   - Carga de Instrucciones de Movimientos
   - Procesamiento de Instrucciones
   - Creación de Informes de Inventario
4. **Detalles de Implementación**
5. **Conclusiones**

## 1. Introducción

El sistema de inventario implementado en estos archivos de Python tiene como objetivo principal permitir la gestión y seguimiento de productos en un inventario, así como la realización de movimientos de stock. El sistema está basado en la utilización de una lista enlazada para almacenar y manejar los productos del inventario, y utiliza archivos de texto como fuente de datos para cargar el inventario inicial y las instrucciones de movimientos.

## 2. Estructura del Código Fuente

### `SG.py`: Interfaz de Usuario

Este archivo contiene las funciones de interfaz de usuario, incluyendo la visualización del menú principal y la interacción con el usuario para seleccionar opciones. La función `open_file()` permite al usuario seleccionar archivos de inventario e instrucciones, como tambien la opcion de generar la variables globlaes donde se podra acceder a la lista de productos como tal.

### `Producto.py`: Clase Producto

Define la clase `Producto` que representa un producto en el inventario. Contiene métodos getter y setter para acceder y modificar sus atributos.

### `Main.py`: Programa Principal

Este archivo contiene el punto de entrada del programa. Utiliza funciones definidas en otros archivos para implementar el flujo del programa y la interacción con el usuario.

### `logic.py`: Lógica de Movimientos

Contiene las funciones para leer y procesar archivos de inventario e instrucciones de movimientos. Interactúa con la lista enlazada de productos definida en `listas.py`.

### `listas.py`: Estructura de Datos

Define la clase `nodo` y `lista_enlazada` que representan una lista enlazada utilizada para almacenar los productos del inventario. Incluye métodos para insertar productos, recorrer la lista, buscar productos y realizar movimientos de stock.

## 3. Flujo del Programa

### Carga de Inventario Inicial

1. El usuario selecciona la opción 1 en el menú principal.
2. El programa utiliza la función `open_file()` en `SG.py` para permitir al usuario seleccionar un archivo de inventario.
3. La lógica de `logic.py` lee el archivo de inventario, crea objetos `Producto` y los agrega a la lista enlazada.

### Carga de Instrucciones de Movimientos

1. El usuario selecciona la opción 2 en el menú principal.
2. El programa utiliza la función `open_file()` en `SG.py` para permitir al usuario seleccionar un archivo de instrucciones de movimientos.
3. La lógica de `logic.py` lee el archivo de instrucciones, procesa las operaciones y actualiza el inventario según las instrucciones.

### Procesamiento de Instrucciones

1. Las instrucciones de movimientos se dividen en instrucciones individuales y se procesan una por una.
2. La lógica de `logic.py` identifica el tipo de instrucción (agregar stock o vender producto) y realiza las operaciones correspondientes en la lista enlazada de productos.

### Creación de Informes de Inventario

1. El usuario selecciona la opción 3 en el menú principal.
2. La lógica de `listas.py` genera un informe detallado del inventario y lo guarda en un archivo llamado `Reporte.txt`.

## 4. Detalles de Implementación

La lógica del programa se basa en el uso de una lista enlazada para almacenar los productos. Cada nodo en la lista contiene un objeto `Producto`. La lógica de movimientos (`logic.py`) procesa las instrucciones leyendo y modificando la lista enlazada, cabe mencionar que el unico tipo de archivos que puede aceptar es de tipo `*.inv` y `*.mov`