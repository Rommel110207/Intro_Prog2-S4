# En un hospital existen 3 áreas: Urgencias, Pediatría y Traumatología. El presupuesto 
# anual del hospital se reparte de la siguiente manera: 
# Obtener la cantidad de dinero que recibirá cada área para cualquier monto presupuestal.

monto_presupuestal = float(input("Ingrese el monto presupuestal: "))

urgencias = monto_presupuestal * 0.37
pediatría = monto_presupuestal * 0.42
traumatología = monto_presupuestal * 0.21

print(f"El monto para urgencias es: {urgencias:.2f}")
print(f"El monto para pediatría es: {pediatría:.2f}")
print(f"El monto para traumatología es: {traumatología:.2f}")

 