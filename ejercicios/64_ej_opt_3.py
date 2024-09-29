# 3) Realiza un programa que sume todos los números enteros pares desde 
# el 0 hasta el 100

print(sum(range(0,101,2)))

# Segunda forma con bucles

num = 0
suma = 0

while num <=100:
    if num % 2 == 0:
        suma += num
    num += 1

print(suma)