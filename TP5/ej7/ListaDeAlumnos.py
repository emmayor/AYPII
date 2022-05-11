from datetime import date

APU = {}
APU["IF003"] = "Algorítmica y Programación I"
APU["IF006"] = "Algorítmica y Programación II"
APU["IF010"] = "Analisis y Diseño de Sistemas"
APU["IF002"] = "Expresión de Problemas y Algoritmos"
APU["IF001"] = "Elementos de Informática"

class Alumno:
    """ Define un dato de tipo Alumno, con las siguientes características """
    def __init__(self, a_id, a_di, a_ap, a_nm, a_cc, prox=None, ante=None):
        self.alu_id = a_id
        self.alu_di = a_di
        self.alu_ap = a_ap
        self.alu_nm = a_nm
        self.alu_cc = a_cc
        self.alu_ex = []
        self.prox = prox    ## Enlace al próximo alumno
        self.ante = ante    ## Enlace al anterior alumno
	
    def __str__(self):
        return "{} {}, {}".format(self.alu_id, self.alu_ap, self.alu_nm)

    def numero_alumno(self):
        return self.alu_id
        
    def proximo(self):
        return self.prox

    def anterior(self):
        return self.ante

    def enlazarProximo(self, otroAlu):
        """ Engancha el Alumno actual, self, con otroAlu """
        self.prox = otroAlu

    def enlazarAnterior(self, otroAlu):
        """ Engancha el Alumno actual, self, con otroAlu """
        self.ante = otroAlu

    def finales(self):
        return self.alu_ex
    
    def agregarFinal(self, materia, fecha: date, nota: int):
        if not materia in APU:
            raise ValueError(f"La materia {materia} no existe")
        elif nota < 0 or nota > 10:
            raise ValueError("Nota inválida")
        else:
            self.alu_ex.append([materia,fecha,nota])
    def imprimir(self):
        print("{} {} {} {} {}".format(self.alu_id, self.alu_di, self.alu_ap.upper(), self.alu_nm, self.alu_cc))
        for exfi in self.alu_ex:
            print("          {} {} {}".format(exfi[0], exfi[1].strftime("%d/%m/%Y"), exfi[2]))
    

class ListaDeAlumnos:
    """Modela una lista enlazada."""

    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        self.ulti = None
        # cantidad de elementos de la lista
        self.len = 0

    def es_vacia(self):
        return self.len == 0

    def primero(self):
        return self.prim

    def ultimo(self):
        return self.ulti
        
    def append(self, a_id, a_di, a_ap, a_nm, a_cc):
        # agrega un alumno a la lista, según nº de alumno
        nuevoAlu = Alumno(a_id, a_di, a_ap, a_nm, a_cc)
        if self.es_vacia():
            self.prim = nuevoAlu
            self.ulti = nuevoAlu
        else:
            # encontrar el lugar en que va
            actAlu = self.prim
            
            if nuevoAlu.numero_alumno() < actAlu.numero_alumno():
                # insertar al principio de la lista
                nuevoAlu.enlazarProximo(actAlu)
                self.prim = nuevoAlu
            else:
                antAlu = None
                while (actAlu.numero_alumno() <=
                       nuevoAlu.numero_alumno() and actAlu.proximo() != None):
                    antAlu = actAlu
                    actAlu = actAlu.proximo()
                if actAlu.numero_alumno() <= nuevoAlu.numero_alumno():
                    # insertar al final de la lista
                    nuevoAlu.enlazarAnterior(actAlu)
                    actAlu.enlazarProximo(nuevoAlu)
                    self.ulti = nuevoAlu
                else:
                    # insertar en el medio de la lista
                    nuevoAlu.enlazarProximo(actAlu)
                    nuevoAlu.enlazarAnterior(antAlu)
                    antAlu.enlazarProximo(nuevoAlu)
                    actAlu.enlazarAnterior(nuevoAlu)
        self.len += 1

    def busqPorID(self, a_id):
        actual = self.prim
        while actual != None and a_id != actual.alu_id:
            actual = actual.proximo()
        if actual != None:
            return actual
        return None


    def remove(self, a_id):
        # quita de la lista y devuelve el alumno con un cierto id
        if self.es_vacia():
            raise IndexError("No hay alumnos en la lista")
        actAlu = self.prim
        antAlu = None
        while (actAlu.numero_alumno() != a_id and actAlu.proximo()!= None):
            antAlu = actAlu
            actAlu = actAlu.proximo()

        if actAlu.numero_alumno() != a_id:
            raise IndexError("El Alumno {} no existe".format(a_id))

        if antAlu == None:
            ## Borrar el primer alumno de la lista
            self.prim = actAlu.proximo()
            if self.prim != None:
                self.prim.enlazarAnterior(actAlu.anterior())
            else:
                ## Era el primer y único alumno de la lista!!
                self.ulti = None
        elif actAlu.proximo() == None:
            ## Es el último alumno de la lista
            antAlu.enlazarProximo(actAlu.proximo())
            self.ulti = antAlu
        else:
            ## Es un alumno del medio
            antAlu.enlazarProximo(actAlu.proximo())
            actAlu.proximo().enlazarAnterior(actAlu)
                
        self.len -= 1
        return actAlu

    def imprimir(self):
        actAlu = self.prim
        while actAlu != None:
            print(actAlu)
            actAlu = actAlu.proximo()
    
                
                                
                    
        
                
            
        
        
