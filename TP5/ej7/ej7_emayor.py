# En el Aula Virtual está definido un Tipo Abstracto de Datos llamado ListaDeAlumnos, que implementa una Lista
# Doblemente Enlazada de Alumnos, con los siguientes datos:
# Nº de Alumno, DNI, Apellido, Nombre, Código de carrera que cursa, 
# y los finales que tiene rendidos (código de materia, fecha, nota).
# Se definen e implementan las siguientes operaciones para las listas de alumnos:

# • Crear una lista de alumnos, inicialmente vacía. La lista mantiene la cantidad de alumnos en un invariante.
# • Insertar un alumno en la lista, manteniendo el orden por número de alumno (legajo).
# • Borrar de la lista y devolver un alumno (el objeto), utilizando para ello el número de alumno.
# • Imprimir la lista, con los datos básicos de cada alumno

# Por otro lado, para los alumnos se definen las operaciones de creación y manejo de punteros (próximo, siguiente)
# y la impresión del alumno, incluyendo los finales que ha rendido.
# También se incluye el programa ListaDeAlumnos_carga que muestra algunas formas posibles de utilizar los
# nuevos tipos definidos.

# a) Amplíar la implementación de tal manera que se pueda agregar una nueva nota de examen final (código de
# materia, fecha, nota), utilizando un método y no accediendo a la estructura, como se hace en el programa carga
# de ejemplo. Se debe validar la nota (0 - 10) y que la materia exista en el diccionario de materias.
# b) Escribí un programa que, dado el TAD definido previamente, solicite un numero de alumno e imprima sus datos,
# incluyendo los exámenes rendidos y las notas obtenidas. Se debe informar si el alumno no existe en la lista.
# Para resolver los ejercicios, se puede extender el TAD con los métodos que consideres necesarios.

from ListaDeAlumnos import *

test1 = ListaDeAlumnos()

test1.append("24-18-975", 41475695, "Aguado", "Marcos Antonio", 123)
test1.append("24-18-910", 36860458, "Hernández", "Jesica Daiana", 123)
test1.append("24-18-943", 41040980, "Loncon", "Nahuel Hernan", 123)
test1.append("24-18-988", 38096837, "Lopez", "Guillermo David", 123)
test1.append("24-18-944", 39225191, "Mera Hossellain", "Jairo Roman", 123)
test1.append("24-18-869", 38626806, "Nievas Arroyo", "Joel Leonardo", 123)
test1.append("24-18-951", 39443047, "Vidal", "Emanuel Guillermo", 123)

entrada = ""

while entrada != '0':
    entrada = str(input("Ingrese un número de alumno. 0 para salir.\n> "))
    if entrada != '0':
        alumno = test1.busqPorID(entrada)
    if alumno == None:
        print("El número de legajo ingresado no está en la lista")
    else:
        alumno.imprimir()
        