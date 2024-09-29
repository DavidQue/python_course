v = "otro texto"
n = 10
# print("Un texto",v,"y un número",n)

c = "Un texto '{1}' y un número '{0}'".format(v,n)
print(c)

#Otra forma
print("Un texto '{texto}' y un número '{numero}'".format(numero=n,texto=v))

#Modificar la forma de mostrar valores

print("{:>30}".format("palabra")) # Alinear a la derecha con 30 caracteres
print("{:<30}".format("palabra")) # Alinear a la izquierda con 30 caracteres
print("{:^30}".format("palabra")) # Alinear al centro con 30 caracteres
print("{:.5}".format("palabra")) # Truncamiento a 5 caracteres
print("{:>30.3}".format("palabra")) # Alinear a la derecha con 30 caracteres y truncamiento de 3

#Formateo de números enteros, rellenando con espacios
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

#Formateo de números enteros, rellenando con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#Formateo de números flotantes, rellenando con espacios
print("{:6.2f}".format(3.1415926))
print("{:6.2f}".format(523.934226)) #Alineando con 6 caracteres

#Formateo de números flotantes, rellenando con ceros
print("{:026.2f}".format(3.1415926))
print("{:026.2f}".format(523.934226)) #Alineando con 6 caracteres