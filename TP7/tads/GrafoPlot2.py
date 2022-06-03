import pyglet as pyg
import Grafo         

class GNodo():
    def __init__(self, dato, n_batch, x=200, y=200, radio=20, ):
        self.posx = x
        self.posy = y
        self.radio = radio
        self.bl = x-radio
        self.br = x+radio
        self.bt = y-radio
        self.bb = y+radio
        self.dato = dato
        self.batch = n_batch
        self.etiq = pyg.text.Label(text=dato, color=(255,0,0,0), font_size=14, x=self.posx, y=self.posy,batch=self.batch)
        self.forma = pyg.shapes.Circle(self.posx, self.posy, self.radio, batch=self.batch)
        
    def cambiarPos(self, x, y):
        self.posx = x
        self.posy = y
    
# PYGLET INIT

w_width = 800
w_height = 600

window = pyg.window.Window(w_width, w_height, caption="Test1")
pyg.gl.glClearColor(0, 0, 0, 1.0)
GBatch = pyg.graphics.Batch()

# PROGRAM INIT
nodo1 = GNodo("Hola", GBatch, x=500, y=500, radio=15)

def on_mouse_motion(self, x, y, dx, dy):
    self.posx=x
    self.posy=y

# EVENTS

@window.event
def on_draw():
    window.clear()
    GBatch.draw()

# Main entry point
if __name__ == '__main__':
    pyg.app.run()
