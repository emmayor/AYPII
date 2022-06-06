import pyglet 
      
class GNodo():
    def __init__(self, dato, n_batch, x, y, radio):
        self.radio = radio
        self.dato = dato
        self.batch = n_batch
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)
        # CIRCULO + ETIQUETA
        self.forma = pyglet.shapes.Circle(x, y, self.radio, 
                                        batch=self.batch, group=self.background)

        self.etiq = pyglet.text.Label(text=dato, color=(0,0,0,255), 
                                    font_size=14,x=self.forma.x, y=self.forma.y,
                                    anchor_x="center", anchor_y="center",
                                    batch=self.batch, group=self.foreground)

        # EVENTOS

        self.mouse_over = False

        # DEBUGGING

        #self.hline = pyglet.shapes.Line(0, self.forma.y, 1600, self.forma.y, color=(0,255,0), batch=self.batch)
        #self.vline = pyglet.shapes.Line(self.forma.x, 0, self.forma.x, 1200, color=(255,0,0), batch=self.batch)
        
    def change_pos(self, x, y):
        self.forma.x = x
        self.forma.y = y
        self.etiq.x = self.forma.x
        self.etiq.y = self.forma.y

    def x(self):
        return self.forma.x
    
    def y(self):
        return self.forma.y
        
        # DEBUGGING
        
        #self.hline.y,self.hline.y2 = y,y
        #self.vline.x,self.vline.x2 = x,x

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_over = self.check_mouse_over(x,y)
        if self.mouse_over:
            self.forma.color = (255, 242, 189)
        else:
            self.forma.color = (255, 255, 255)

    def check_mouse_over(self,x,y):
        m_range_x = x in range(self.forma.x-self.radio,self.forma.x+self.radio)
        m_range_y = y in range(self.forma.y-self.radio,self.forma.y+self.radio)
        return m_range_x and m_range_y

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.mouse_over:
            self.change_pos(x,y)

class GLinea():
    def __init__(self, l_batch, x1, x2, y1, y2,):
        self.batch = l_batch
        # CIRCULO + ETIQUETA
        self.forma = pyglet.shapes.Line(x=x1, y=y1, x2=x2, y2=y2, color=(255,255,255), batch=self.batch)


    
class GrafoPlot(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Grafo")
        self.batch = pyglet.graphics.Batch()
        #self.testText = pyglet.text.Label(text="TEST TEXT", font_size=14,x=300, y=300,batch=self.batch)
        self.nodos = []
        self.nodos.append(GNodo("EQS", self.batch, x=500, y=500, radio=30))
        self.nodos.append(GNodo("TRV", self.batch, x=200, y=500, radio=30))
        self.lineas = []
        self.lineas.append(GLinea(self.batch,x1=self.nodos[0].x(),
                                             x2=self.nodos[1].x(),
                                             y1=self.nodos[0].y(),
                                             y2=self.nodos[1].y()))

        for n in self.nodos:
            super().push_handlers(n.on_mouse_drag)
            super().push_handlers(n.on_mouse_motion)

    def on_draw(self):
        """Clear the screen and draw shapes"""
        self.clear()
        self.batch.draw()

# Main entry point
if __name__ == '__main__':
    gplot = GrafoPlot(800,600)
    pyglet.app.run()
