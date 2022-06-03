import pyglet
from Grafo import Grafo

class GrafoPlot:
    def __init__(self, grafo, titulo="Grafo", ancho=800, alto=600):
        self.windowH = ancho
        self.windowW = alto
        self.window = pyglet.window.Window(self.windowH, self.windowW, caption=titulo,)
        self.grafo = grafo
        self.listaCirculos = {}
        self.GBatch = pyglet.graphics.Batch()

    def dibujarNodos(self):
        i = 0
        for nodo in self.grafo.lista_vertices:
            nodoPosX = 400+i
            nodoPosY = 500
            self.listaCirculos[nodo] = (pyglet.shapes.Circle(nodoPosX, nodoPosY, 20, batch=self.GBatch),
                                        pyglet.text.Label(text=nodo, color=(255,0,0,0), font_size=14, x=nodoPosX+10 // 2,
                                        y=nodoPosY+10,batch=self.GBatch))
            i += 40

    

grafo1 = Grafo() 

a,b,c,d,e = "F","Z","E","T","B"

grafo1.insertar(a, b, True)
grafo1.insertar(b,c)
grafo1.insertar(b,d)
grafo1.insertar(d,e)
grafo1.insertar(d,a)

grafico = GrafoPlot(grafo1, "Grafo Test 1")
grafico.dibujarNodos()
pyglet.gl.glClearColor(0.8, 0.8, 0.8, 1.0)


@grafico.window.event
def on_draw():
    grafico.window.clear()
    grafico.GBatch.draw()

# on mouse drag event
@grafico.window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    # printing some message
    print("Mouse is dragged")
     


# Main entry point
if __name__ == '__main__':
    pyglet.app.run()
