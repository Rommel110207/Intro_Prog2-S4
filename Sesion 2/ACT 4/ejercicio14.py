# Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su 
# salario actual y un descuento de 2,5% por servicios.

salario_actual = float(input("Ingrese el salario actual del empleado: "))

incremento = salario_actual * 0.08
salario_con_incremento = salario_actual + incremento

descuento = salario_con_incremento * 0.025
nuevo_salario = salario_con_incremento - descuento

print(f"El nuevo salario del empleado es: {nuevo_salario:.2f}")

