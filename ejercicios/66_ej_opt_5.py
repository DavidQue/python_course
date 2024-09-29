# 5)Realiza un programa que pida al usuario un número del 0 al 9, y que 
# mientras el número no sea correcto se repita el proceso. Luego debe
# comprobar si el número se encuentra en la lista de números y notificarlo

lista = [1, 3, 5, 7]

while True:
    numero = int(input("Introduzca un número del 0 al 9"))
    if(numero>= 0 and numero <=9):
        break

if numero in lista:
    print("Sí")
else:
    print("No")