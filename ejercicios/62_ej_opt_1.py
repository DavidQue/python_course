# 1) Realiza un programa que lea dos números por teclado y permita elegir
# entre 3 opciones en un menú:
# - Mostrar una suma de los dos números
# - Mostrar una resta del primero menos el segundo
# - Mostrar una multiplicación de los dos números
# - En caso de no introducir una opción válidad, el programa informará de
#   que no es correcta

n1 = float(input("Introduce el primer número"))
n2 = float(input("Introduce el segundo número"))

print("¿Qué quieres hacer?")
print("1. Sumar los 2 números")
print("2. Restar los 2 números")
print("3. Multiplicar los 2 números")
opcion = input("Introduce una opción: ")

if opcion == "1":
    print("La suma de",n1,"+",n2,"es",n1+n2)
elif opcion == "2":
    print("La resta de",n1,"+",n2,"es",n1-n2)
elif opcion == "e":
    print("La multiplicación de",n1,"+",n2,"es",n1*n2)
else:
    print("Opción incorrecta")