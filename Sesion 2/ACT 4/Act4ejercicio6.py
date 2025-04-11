# Solicita el precio de 3 productos y muestra: 
# Subtotal 
# IVA (15%) 
# Total a pagar 

producto1 = float(input("Introduce el precio del producto 1: "))
producto2 = float(input("Introduce el precio del producto 2: "))
producto3 = float(input("Introduce el precio del producto 3: "))

subtotal = producto1 + producto2 + producto3
iva = subtotal * 0.15
total = subtotal + iva

print("Subtotal: ", subtotal)
print("IVA (15%): ", iva)
print("Total a pagar: ", total)

