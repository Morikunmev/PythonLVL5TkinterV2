import matplotlib.pyplot as plt

# Inicializamos la lista de productos y sus porcentajes
productos = ["Canape", "Mini-pizzas", "Mini-empanadas", "Sushi", "Mini-chacarero", "Jugo", "Bebida",
             "PiscoSour", "Champagne", "Vino"]

# Inicializamos los porcentajes correspondientes (pueden ser valores ficticios)
porcentajes = [10, 15, 8, 12, 5, 7, 9, 3, 6, 15]


# Función para actualizar y mostrar el gráfico de regla de tres
def actualizar_grafico(producto):
    if producto in productos:
        indice = productos.index(producto)
        porcentaje = porcentajes[indice]

        # Creamos el gráfico
        plt.figure(figsize=(8, 6))
        plt.bar(productos, porcentajes, color='skyblue')
        plt.title(f"Porcentajes de Productos (Actualizado con {producto})")
        plt.xlabel("Productos")
        plt.ylabel("Porcentaje")
        plt.ylim(0, 20)  # Puedes ajustar el límite vertical según tus necesidades
        plt.bar(producto, porcentaje, color='orange')
        plt.show()


# Ejemplo de uso
producto_agregado = "Canape"  # Puedes cambiar esto según el producto que se agregue
actualizar_grafico(producto_agregado)

# Simulamos agregar otro producto (por ejemplo, "Mini-pizzas")
producto_agregado = "Mini-pizzas"
# Actualizamos los porcentajes (puedes modificar esto según tus necesidades)
porcentajes = [12, 14, 10, 15, 6, 8, 7, 4, 5, 18]
actualizar_grafico(producto_agregado)
