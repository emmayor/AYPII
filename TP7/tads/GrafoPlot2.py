import pyglet 
      
class GNodo():
    def __init__(self, dato, n_batch, x, y, radio):
        self.radio = radio
        self.dato = dato
        self.batch = n_batch
        # 
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
    def __init__(self, l_batch, nodo1, nodo2):
        self.n1 = nodo1
        self.n2 = nodo2
        self.batch = l_batch
        self.linea = pyglet.shapes.Line(x=nodo1.x(), y=nodo1.y(), 
                                        x2=nodo2.x(), y2=nodo2.y(), 
                                        color=(255,255,255), batch=self.batch)
    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.linea.position = (self.n1.x(),self.n1.y(),self.n2.x(),self.n2.y())
  
class GrafoPlot(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Grafo")
        self.batch = pyglet.graphics.Batch()    
        self.nodos = []
        self.nodos.append(GNodo("EQS", self.batch, x=500, y=500, radio=30))
        self.nodos.append(GNodo("TRV", self.batch, x=200, y=500, radio=30))
        self.lineas = []
        self.lineas.append(GLinea(self.batch, self.nodos[0], self.nodos[1]))
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
