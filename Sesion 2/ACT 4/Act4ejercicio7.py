# Calcula la calificación final de un estudiante con ponderaciones: 
# Tareas: 30% 
# Examen parcial: 30% 
# Examen final: 40%

print("Ingrese las siguientes calificaciones en base a 100")
tareas = float(input("Ingrese la calificación de tareas: "))
examen_parcial = float(input("Ingrese la calificación del examen parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))

calif_tareas = tareas * 0.3
calif_examen_parcial = examen_parcial * 0.3
calif_examen_final = examen_final * 0.4

calificacion_final = calif_tareas + calif_examen_parcial + calif_examen_final

print(f"La calificación final es {calificacion_final:.2f}")