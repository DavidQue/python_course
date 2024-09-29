# Durante la planificación de un proyecto se han acordado una lsita de tareas. Para cada una de estas tareas,
# se han asigando un orden de prioridad (cuanto menor es el número de orden, más prioridad)
# ¿Eres capaz de crear una estructurad el tipo cola con todas las tareas ordenadas pero sin los nºs de orden?

# Pista: Para ordenar automáticamente una lista, es posible utilizar el método sort()

tareas = [
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas'],
]

print("--Tareas desordenadas--")

for tarea in tareas:
    print(tarea[0],tarea[1])


from collections import deque

tareas.sort()

print(tareas)
cola = deque()

for tarea in tareas:
    cola.append(tarea[1])

print("--Tareas ordenadas--")
for tarea in cola:
    print(tarea)

print("--Primera tarea a realizar--")
print(cola.popleft())
print("--Segunda tarea a realizar--")
print(cola.popleft())

