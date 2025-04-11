# Pide nombre y apellido y muestra un posible correo: 
# nombre.apellido@miuniversidad.edu.ni

nombre = input("Ingresa el nombre: ")
apellido = input("Ingresa el apellido: ")

print(*[nombre, ".", apellido, "@uamv.edu.ni"], sep='')
