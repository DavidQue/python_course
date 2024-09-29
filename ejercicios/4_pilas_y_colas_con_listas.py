#PILAS último en entrar es el primero en salir
pila = [3, 4, 5]
pila.append(6)
pila.append(7)

# extraer elementos
n = pila.pop() #devuelve el último elemento de la "pila"

#print(pila,n) # la lista tiene un elemento menos, pero lo hemos guardado
              # en una variable

#COLAS primero en entrar es el primero en salir

#se suele importar de una librería de python
from collections import deque

cola = deque() #cola vacía

cola = deque(["David", "María", "Marta", "Manuel"])

# Para añadir
cola.append("Lupo")

print(cola)

# Para quitar el primer elemento que se metió y guardarlo en una variable

d = cola.popleft()

print(cola)