# Diseñe un algoritmo que lea los datos necesarios y calcule la masa, según la formula

presion = float(input("Introduce la presión: "))
volumen = float(input("Introduce el volumen: "))
temperatura = float(input("Introduce la temperatura: "))

masa = (presion * volumen)/(0.37 * (temperatura + 460))

print(f"La masa es: {masa:.2f}")