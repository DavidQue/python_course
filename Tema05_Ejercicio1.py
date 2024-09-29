# 1) Formatea los siguientes valores para mostrar el resutlado indicado:
# "Hola Mundo" -> Alineado a la derecha en 20 caracteres
# "Hola Mundo" -> Truncamiento en el cuarto carácter (índice 3)
# "Hola Mundo" -> Alineamiento al centro en 20 caracteres con truncamiento
#                 en el segundo carácter (índice 1)
# 150 -> Formateo a 5 números enteros rellenados con ceros
# 7887 -> Formateo a 7 números enteros rellenados con espacios
# 20.02 -> Formateo a 3 números enteros y 3 números decimales

hola = "Hola mundo"
n1 = 150
n2 = 7887
n3 = 20.02
print("{:>20}".format(hola))
print("{:.4}".format(hola))
print("{:^20.2}".format(hola))
print("{:05d}".format(n1))
print("{:7d}".format(n2))
print("{:07.3f}".format(n3))