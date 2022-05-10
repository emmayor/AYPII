# Crear un programa que, usando el TAD definido en el Ejercicio 1, permita a un usuario
# administrar una lista de tareas pendientes. 
# Dá la opción de elegir entre las operaciones: agregar tareas, borrar tareas o listar las tareas de la lista.
# Considerá lo siguiente:
# • Las tareas se agregan al final de la lista, y llevan un número de ítem de lista y una descripción. 
#   El número se genera automáticamente a partir del número del último elemento de la lista + 1.
# • Se puede borrar una tarea de cualquier lugar de la lista, utilizando el número de ítem.
# • La opción de listar muestra todas las tareas pendientes que están en la lista, en el orden en que se agregaron.

from ListaEn_def import ListaEnlazada

listaTareas = ListaEnlazada()

def agregarTarea():
    desc = -1
    while desc != '0':
        desc = input("Ingrese el nombre de la tarea a agregar. Ingrese 0 para terminar\n")
        if desc != '0':
            # Como usamos el último elemento de la lista para generar el número, debemos asegurarnos de que 
            # éste exista. 
            if listaTareas.ult_nodo != None:
                listaTareas.append((listaTareas.ult_nodo.valor()[0]+1,desc))
            else:
                listaTareas.append((1,desc))
            print(f"Se ha creado la tarea \"{desc}\". Indice: {listaTareas.ult_nodo.valor()[0]}")

def eliminarTarea():
    # Indice es un número mayor a 0
    indice = None
    while indice != 0:
        indice = int(input("Ingrese el número de la tarea a borrar. Ingrese 0 para terminar\n"))
        if indice != 0:
            for tarea in listaTareas:
                if tarea.valor()[0] == indice:
                    listaTareas.borrar(tarea.valor())
            print(f"Se ha eliminado la tarea número \"{indice}\"")

def imprimirLista():
    print(listaTareas)

entrada = ''
while entrada != '0':
    print("LISTADOR DE TAREAS - SELECCIONE UNA OPCION")
    print("1: Añadir tareas")
    print("2: Eliminar tareas")
    print("3: Imprimir lista de tareas")
    print("0: Salir")
    entrada = input('> ')
    # Se requiere Python 3.10 para que funcione "switch" 
    match entrada:
        case '1':
            agregarTarea()
        case '2':
            eliminarTarea()
        case '3':
            imprimirLista()
