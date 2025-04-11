# Solicita el nombre, precio de un producto y un porcentaje de descuento. Muestra el 
# nombre del producto y precio final luego de aplicar el descuento.

nombre_producto = input("Introduce el nombre del producto: ")
precio_producto = float(input("Introduce el precio del producto: "))
porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))

precio_final = precio_producto * (1 - (porcentaje_descuento / 100))

print(f"Producto: {nombre_producto}")
print(f"Precio final: {precio_final:.2f}")