import pyglet 
from math import atan, sin, cos
      
class GNodo():
    def __init__(self, dato, n_batch, x, y, radio):
        self.radio = radio
        self.dato = dato
        self.batch = n_batch
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)
        self.mouse_over = False
        self.forma = pyglet.shapes.Circle(x, y, self.radio, 
                                        batch=self.batch, group=self.background)
        self.etiq = pyglet.text.Label(text=dato, color=(0,0,0,255), 
                                    font_size=14,x=self.forma.x, y=self.forma.y,
                                    anchor_x="center", anchor_y="center",
                                    batch=self.batch, group=self.foreground)
                
    def change_pos(self, x, y):
        self.forma.x = x
        self.forma.y = y
        self.etiq.x = self.forma.x
        self.etiq.y = self.forma.y

    def x(self):
        return self.forma.x
    
    def y(self):
        return self.forma.y

    def r(self):
        return self.radio
        
    def check_mouse_over(self,x,y):
        m_range_x = x in range(self.forma.x-self.radio,self.forma.x+self.radio)
        m_range_y = y in range(self.forma.y-self.radio,self.forma.y+self.radio)
        return m_range_x and m_range_y

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_over = self.check_mouse_over(x,y)
        if self.mouse_over:
            self.forma.color = (255, 242, 189)
        else:
            self.forma.color = (255, 255, 255)


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.mouse_over:
            self.change_pos(x,y)

class GLinea():
    def __init__(self, l_batch, nodo1, nodo2, double=False):
        self.n1 = nodo1
        self.n2 = nodo2
        self.batch = l_batch
        self.linea = pyglet.shapes.Line(x=nodo1.x(), y=nodo1.y(), 
                                        x2=nodo2.x(), y2=nodo2.y(), 
                                        color=(255,255,255), batch=self.batch)

        # PENDIENTE DE LA FLECHA (se puede evitar esta división asquerosa???)
        if (self.linea.y2-self.linea.y) != 0:
            self.pendiente = (self.linea.x2-self.linea.x)/(self.linea.y2-self.linea.y)
        else: 
            self.pendiente = 0.01

        # ANGULO DE LA FLECHA
        self.angulo_p1 = atan(self.pendiente)

        # ANGULO DE LAS PUNTAS EXTERNAS
        self.angulo_p2 = atan(self.pendiente+0.03)
        self.angulo_p3 = atan(self.pendiente-0.03)
        
        # COORDENADAS DE LA PUNTA 1 (LA QUE ESTÁ PEGADA AL NODO)
        self.x_punta = sin(self.angulo_p1)*self.n2.r()+self.n2.x()
        self.y_punta = cos(self.angulo_p1)*self.n2.r()+self.n2.y()

        # COORDENADAS DE LAS OTRAS DOS PUNTAS
        self.x2_punta = sin(self.angulo_p2)*self.n2.r()+self.n2.x()+10
        self.y2_punta = cos(self.angulo_p2)*self.n2.r()+self.n2.y()+10
        self.x3_punta = sin(self.angulo_p3)*self.n2.r()+self.n2.x()-10
        self.y3_punta = cos(self.angulo_p3)*self.n2.r()+self.n2.y()+10

        # FORMA                 
        self.punta1 = pyglet.shapes.Triangle(x=self.x_punta, y=self.y_punta,
                                            x2=self.x2_punta, y2=self.y2_punta,
                                            x3=self.x3_punta, y3=self.y3_punta,
                                            color=(255,0,0), batch=self.batch)
    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.linea.position = (self.n1.x(),self.n1.y(),self.n2.x(),self.n2.y())
       # PENDIENTE DE LA FLECHA (se puede evitar esta división asquerosa???)
        if (self.linea.y2-self.linea.y) != 0:
            self.pendiente = (self.linea.y2-self.linea.y)/(self.linea.x2-self.linea.x)
        else: 
            self.pendiente = 0.01

        # ANGULO DE LA FLECHA
        self.angulo_p1 = atan(self.pendiente)

        # ANGULO DE LAS PUNTAS EXTERNAS
        self.angulo_p2 = atan(self.pendiente+0.33)
        self.angulo_p3 = atan(self.pendiente-0.33)
        
        # COORDENADAS DE LA PUNTA 1 (LA QUE ESTÁ PEGADA AL NODO)
        self.x_punta = sin(self.angulo_p1)*self.n2.r()+self.n2.x()
        self.y_punta = cos(self.angulo_p1)*self.n2.r()+self.n2.y()

        # COORDENADAS DE LAS OTRAS DOS PUNTAS
        self.x2_punta = sin(self.angulo_p2)*(self.n2.r()+10)+self.n2.x()+10
        self.y2_punta = cos(self.angulo_p2)*(self.n2.r()+10)+self.n2.y()+10
        self.x3_punta = sin(self.angulo_p3)*(self.n2.r()+10)+self.n2.x()-10
        self.y3_punta = cos(self.angulo_p3)*(self.n2.r()+10)+self.n2.y()+10

        self.punta1.position = (self.x_punta,self.y_punta,
                                self.x2_punta, self.y2_punta,
                                self.x3_punta, self.y3_punta)
  
class GrafoPlot(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Grafo")
        self.batch = pyglet.graphics.Batch()    
        self.nodos = []
        #self.nodos.append(GNodo("EQS", self.batch, x=500, y=400, radio=30))
        self.nodos.append(GNodo("TRV", self.batch, x=200, y=500, radio=30))
        self.nodos.append(GNodo("BSA", self.batch, x=100, y=300, radio=30))
        self.lineas = []
        self.lineas.append(GLinea(self.batch, self.nodos[0], self.nodos[1], double=True))
        #self.lineas.append(GLinea(self.batch, self.nodos[1], self.nodos[2], double=True))
        for n in self.nodos:
            super().push_handlers(n.on_mouse_drag)
            super().push_handlers(n.on_mouse_motion)
        for l in self.lineas:
            super().push_handlers(l.on_mouse_drag)
    def on_draw(self):
        self.clear()
        self.batch.draw()

if __name__ == '__main__':
    gplot = GrafoPlot(800,600)
    pyglet.app.run()
