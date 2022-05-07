from ClaseListaEC import *

"inicializar"

milis = ListaEC()
milis.append(23, "so", 500)
milis.append(27, "word", 1500)
milis.append(101, "uno", 750)

descuento = 100

"Ver lo cargado"

milis.imprimir()

"Recorrer"

actN = milis.primero()
antN = None

while(not actN == None):
    restante = actN.tiempoR()
    print("{} {}/{}".format(actN, restante, actN.tiempoT()))
    if(descuento >= restante):
        "Borrar Nodo"
        milis.removeB(antN, actN)
        print("    sale {}".format(actN))
    else:
        actN.actualizar(-descuento)
    antN = actN
    actN = actN.proximo()
    if(actN.isHeader()):
        actN = actN.primero()
        antN = None
