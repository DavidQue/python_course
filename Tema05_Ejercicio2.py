# 2) Crea un script llamado tabla.py que realice las siguientes tareas:
# Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
# El primer argumento hará referencia a las filasd e una tabla, el segundo a las columnas.
# En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
# El script contendrá un bucle for que itere el número de veces del primer argumento.
# Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
# Dento del segundo for ejecuta una instrucción print("*",End=W), (end=" evita el salto de línea")
# Ejecuta el código y observa el resultado0

import sys
print(sys.argv[0])
print(sys.argv[1])