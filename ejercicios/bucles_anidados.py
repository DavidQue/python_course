lista = ["OLA", 10, "aDIÓS", [50, 100, 150]]
#último elemento del último elemento
# print(lista[-1][-1])
# for numero in lista[-1]:
#     print(numero)

#RECORRE SUBLISTAS
lista = [
    "Esto es un texto",             # cadena
    (1, 5, 10, 15, 20, 25),         # tupla
    ["Azul", "Verde", "Amarillo"]   # lista
]

# for coleccion in lista:
#     for elemento in coleccion:
#         print(coleccion, "->" ,elemento)

# for indice_coleccion, coleccion in enumerate(lista):
#     for indice_elemento, elemento in enumerate(coleccion):
#         print(lista[indice_coleccion][indice_elemento])

#TABLA
tabla = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
]

# for fila in tabla:
#     for columna in fila:
#         print(columna, end=" ")
#     print()

# for indice_fila, fila in enumerate(tabla):
#     for indice_columna, columna in enumerate(fila):
#         print(tabla[indice_fila][indice_columna], end=" ")
#     print()

# CUBO

cubo = [
    tabla, tabla, tabla
    ]
# print(cubo[0][0][0])

    # Lo recorremos dinámicamente

# for tabla in cubo:
#     for fila in tabla:
#         for columna in fila:
#             print(columna)

for k, tabla in enumerate(cubo):
    for i, fila in enumerate(tabla):
        for j, columna in enumerate(fila):
            print(cubo[i][j][k], end=" ")
        print()
    print()