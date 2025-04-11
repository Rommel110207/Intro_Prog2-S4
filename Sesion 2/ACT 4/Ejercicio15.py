# Algoritmo para calcular el porcentaje de mujeres y varones en un aula.

mujeres = int(input("Introduce el número de mujeres: "))
varones = int(input("Introduce el número de varones: "))
total = mujeres + varones
porcentaje_mujeres = (mujeres / total) * 100
porcentaje_varones = (varones / total) * 100
print("El porcentaje de mujeres es:", porcentaje_mujeres, "%")
print("El porcentaje de varones es:", porcentaje_varones, "%")
