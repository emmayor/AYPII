# Crear un programa que, usando el TAD definido en el Ejercicio 1, permita a un usuario administrar una lista de tareas pendientes. Dá la opción de elegir entre las operaciones: agregar tareas, borrar tareas o listar las tareas de la lista.
# Considerá lo siguiente:
# • Las tareas se agregan al final de la lista, y llevan un número de ítem de lista y una descripción. El número se genera automáticamente a partir del número del último elemento de la lista + 1.
# • Se puede borrar una tarea de cualquier lugar de la lista, utilizando el número de ítem.
# • La opción de listar muestra todas las tareas pendientes que están en la lista, en el orden en que se agregaron.

from ListaEn_Ej1 import ListaEnlazada

listaTareas = ListaEnlazada()
desc = -1

while desc != '0':
    desc = input("Ingrese el nombre de la tarea a agregar. Ingrese 0 para terminar\n")
    if desc != '0':
        nuevaTarea = (desc,len(listaTareas)+1)
        listaTareas.append(nuevaTarea)
        print(f"Se ha creado la tarea \"{desc}\"")
while desc != '0':
    desc = input("Ingrese el nombre de la tarea a borrar. Ingrese 0 para terminar\n")
    if desc != '0':
        pos = listaTareas.indice()
print(listaTareas)
