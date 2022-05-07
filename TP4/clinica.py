# a) Escribir un TAD ColaDePacientes, con los métodos nuevo_paciente, que recibe el nombre del paciente y lo
# encola, y un método proximo_paciente que devuelva el primer paciente en la cola y lo desencole.
# b) Escribir un TAD Recepción, que contenga un diccionario con las colas correspondientes a cada doctor o
# doctora, y los métodos nuevo_paciente que reciba el nombre del paciente y del especialista, y proximo_paciente
# que reciba el nombre de la persona liberada (el médico que terminó de atender) y devuelva el próximo paciente en
# espera (para ese médico). 

class ColaDePacientes:
    """ Una cola tradicional, pero tiene métodos con otros nombres"""
    def __init__(self):
        self.items = []
    
    def estaVacia(self):
        if len(self.items) == 0:
            return True
        return False
    
    def nuevo_paciente(self, paciente):
        return self.items.append(paciente)
    
    def proximo_paciente(self):
        if self.estaVacia():
            raise IndexError("La cola esta vacía")
        return self.items.pop(0)

    def __str__(self):
        return str(self.items)

class Recepcion:
    """ Almacena pares medico:cola en un diccionario. """
    def __init__(self):
        self.colas = {}
    def __str__(self):
        return str(self.colas)
    def nuevo_paciente(self, nombrePaciente, nombreMedico):
        if nombreMedico not in self.colas: # Si todavía no ingrese ningun paciente con ese médico...
            self.colas[nombreMedico] = ColaDePacientes() # Crear una cola de pacientes para ése médico...
        return self.colas[nombreMedico].nuevo_paciente(nombrePaciente) # Ahora que sé que está el médico, agrego el paciente a su cola.
    def proximo_paciente(self, medicoLibre):
        if medicoLibre not in self.colas: # Si no existe un médico con ese nombre, comunico el error...
            raise KeyError("Entrada no encontrada")
        else:
            return self.colas[medicoLibre].proximo_paciente()




        