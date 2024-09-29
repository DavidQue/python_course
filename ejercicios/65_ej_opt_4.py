# 4)Realiza un programa que pida al usuario cuántos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética

# numero = int(input("¿Cuántos números quieres introducir?"))
total_numeros = None
while total_numeros is None:
    try:
        total_numeros = int(input("¿Cuántos números quieres introducir? "))
        break
    except ValueError:
        print("Por favor, introduce un número entero válido.")

suma = 0

for i in range(total_numeros):
    num = int(input(f"Introduce el número en posición {i+1}: "))
    suma += num

media = suma / total_numeros
print(f"La media es: {media}")
print("Fin del programa")
