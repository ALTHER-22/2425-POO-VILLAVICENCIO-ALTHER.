# Programa para gestionar un registro de productos en una tienda
# Este programa permite agregar productos, calcular su precio total y mostrar el inventario disponible.

# Constantes: Mayúsculas con guiones bajos
IMPUESTO_VENTA = 0.12  # Porcentaje de impuesto sobre el precio del producto

# Clase: CamelCase
class Producto:
    def __init__(self, nombre, precio, en_stock):
        """Inicializa un producto con su nombre, precio y cantidad en stock"""
        self.nombre = nombre  # string
        self.precio = precio  # float
        self.en_stock = en_stock  # integer

    def mostrar_informacion(self):
        """Devuelve una representación legible de la información del producto"""
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.en_stock} unidades"

# Funciones: snake_case
def calcular_precio_con_impuesto(precio):
    """Calcula el precio final de un producto con el impuesto de venta incluido"""
    return precio * (1 + IMPUESTO_VENTA)

def agregar_producto(lista_productos, producto):
    """Agrega un producto al inventario"""
    lista_productos.append(producto)

def calcular_total_inventario(lista_productos):
    """Calcula el valor total del inventario considerando el stock de cada producto"""
    total = 0
    for producto in lista_productos:
        total += producto.precio * producto.en_stock
    return total

# Variables: snake_case
productos = []  # Lista para almacenar los productos del inventario

# Creación de instancias de productos
producto1 = Producto("Manzanas", 0.50, 100)
producto2 = Producto("Pan", 1.20, 50)
producto3 = Producto("Leche", 0.90, 30)

# Agregar productos al inventario
agregar_producto(productos, producto1)
agregar_producto(productos, producto2)
agregar_producto(productos, producto3)

# Mostrar información de los productos
print("Inventario de productos:")
for producto in productos:
    print(producto.mostrar_informacion())

# Calcular y mostrar el precio total del inventario
precio_total = calcular_total_inventario(productos)
print(f"\nEl valor total del inventario es: ${precio_total:.2f}")

# Ejemplo de cálculo del precio con impuesto para un producto
precio_con_impuesto = calcular_precio_con_impuesto(producto1.precio)
print(f"\nEl precio de una {producto1.nombre} con impuesto incluido es: ${precio_con_impuesto:.2f}")
