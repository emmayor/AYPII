# !!! --- Puntos a) y b) en "clinica.py" --- !!!
# c) Escribir un programa que permita al usuario ingresar nuevos pacientes o indicar que un consultorio se ha
# liberado y en ese caso imprima el próximo paciente en espera.

from clinica import Recepcion

recepcion = Recepcion()

def agregarPacientes():
    paciente = input("Ingrese el nombre completo del paciente\n> ")
    medico = input("Ingrese el apellido del médico\n> ")
    recepcion.nuevo_paciente(paciente,medico)
    print(f"Se agregó el paciente {paciente} a la cola del Dr./Dra. {medico}.")

def liberarMedico():
    medico = input("Ingrese el apellido del médico\n> ")
    try:
        proximo = recepcion.proximo_paciente(medico)
        print(f"El próximo paciente del Dr./Dra {medico} es {proximo}")
    except IndexError: 
        print("Este médico no tiene ningun paciente por atender")   
    except KeyError:
        print("El médico ingresado no existe! Agregue un paciente con su médico correspondiente, o implemente un método que permita agregar médicos sin pacientes!")     

entrada = ''
while entrada != '0':
    print("GESTION DE CLINICA - SELECCIONE UNA OPCION")
    print("1: Añadir pacientes")
    print("2: Liberar médico")
    print("0: Salir")
    entrada = input()
    if entrada == '1':
        agregarPacientes()
        print(recepcion)
    if entrada == '2':
        liberarMedico()


