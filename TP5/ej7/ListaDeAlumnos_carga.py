import datetime
from ListaDeAlumnos import *

#Carga de materias
APU = {}
APU["IF003"] = "Algorítmica y Programación I"
APU["IF006"] = "Algorítmica y Programación II"
APU["IF010"] = "Analisis y Diseño de Sistemas"
APU["IF002"] = "Expresión de Problemas y Algoritmos"
APU["IF001"] = "Elementos de Informática"

#Carga de alumnos
test1 = ListaDeAlumnos()

test1.append("24-18-975", 41475695, "Aguado", "Marcos Antonio", 123)
test1.append("24-18-910", 36860458, "Hernández", "Jesica Daiana", 123)
test1.append("24-18-943", 41040980, "Loncon", "Nahuel Hernan", 123)
test1.append("24-18-988", 38096837, "Lopez", "Guillermo David", 123)
test1.append("24-18-944", 39225191, "Mera Hossellain", "Jairo Roman", 123)
test1.append("24-18-869", 38626806, "Nievas Arroyo", "Joel Leonardo", 123)
test1.append("24-18-951", 39443047, "Vidal", "Emanuel Guillermo", 123)

test1.imprimir()

# Carga de Finales de alumnos
a1 = test1.primero()
ex = a1.finales()
ex.append(["IF001", datetime.date(2018,3,22), 2])
ex.append(["IF002", datetime.date(2018,4,15), 8])

# Prueba de agregarFinal()
a1.agregarFinal("IF010",datetime.date(2019,5,10),9)


# Imprimir Alumno
a1.imprimir()
print()

# Borrar un alumno
a1 = test1.remove("24-18-869")
print("Se quitó a {} de la lista".format(a1.numero_alumno()))
a1 = test1.remove("24-18-951")
print("Se quitó a {} de la lista".format(a1.numero_alumno()))
a1 = test1.remove("24-18-988")
print("Se quitó a {} de la lista".format(a1.numero_alumno()))

# Imprimir Alumno
test1.imprimir()
