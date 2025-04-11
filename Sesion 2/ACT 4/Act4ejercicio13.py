# Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra 
# los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer 
# la ruta en una semana cualquiera.

tiempo_lunes = float(input("Ingrese el tiempo del lunes (en minutos): "))
tiempo_miercoles = float(input("Ingrese el tiempo del miércoles (en minutos): "))
tiempo_viernes = float(input("Ingrese el tiempo del viernes (en minutos): "))

tiempo_promedio = (tiempo_lunes + tiempo_miercoles + tiempo_viernes) / 3

print(f"El tiempo promedio que tarda en recorrer la ruta es: {tiempo_promedio:.2f} minutos")