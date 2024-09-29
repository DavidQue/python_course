# 2) Realiza un programa que lea un número impar por teclado. Si el usuario
# no introduce un número impar, debe repetirse el proceso hasta que lo
# introduzca correctamente


n1 = 0
while n1 % 2 == 0:
    n1 = int(input("Introduce un número impar"))
print("Su número impar es",n1)