import pyglet 

from math import atan, sin, cos, pi, sqrt
from random import choice
from Grafo import Grafo

# Enable Antialiasing
pyglet.gl.glEnable(pyglet.gl.GL_LINE_SMOOTH)
pyglet.gl.glEnable(pyglet.gl.GL_POLYGON_SMOOTH)
      
class GNode():
    def __init__(self, name, x, y, r, n_batch):
        self.radius = r
        self.n_name = name
        self.batch = n_batch
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)
        self.mouse_over = False
        self.shape = pyglet.shapes.Circle(x, y, self.radius, 
                                        batch=self.batch, group=self.background)
        self.label = pyglet.text.Label(text=self.n_name, color=(0,0,0,255), 
                                       font_size=12,x=self.shape.x, y=self.shape.y,
                                       anchor_x="center", anchor_y="center",
                                       batch=self.batch, group=self.foreground)
    def change_pos(self, x, y):
        self.shape.x = x
        self.shape.y = y
        self.label.x = self.shape.x
        self.label.y = self.shape.y

    def name(self):
        return self.n_name

    def x(self):
        return self.shape.x
    
    def y(self):
        return self.shape.y

    def r(self):
        return self.radius
        
    def check_mouse_over(self,x,y):
        m_range_x = x in range(self.shape.x-self.radius,self.shape.x+self.radius)
        m_range_y = y in range(self.shape.y-self.radius,self.shape.y+self.radius)
        return m_range_x and m_range_y

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_over = self.check_mouse_over(x,y)
        if self.mouse_over:
            self.shape.color = (255, 242, 189)
        else:
            self.shape.color = (255, 255, 255)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.mouse_over:
            self.change_pos(x,y)

class GArc():
    def __init__(self, node_1, node_2,l_batch, double=False):
        self.n1 = node_1
        self.n2 = node_2    
        self.batch = l_batch
        self.double = double
        self.group = pyglet.graphics.OrderedGroup(-1)
        self.arc = pyglet.shapes.Line(  x=self.n1.x(), y=self.n1.y(), 
                                        x2=self.n2.x(),y2=self.n2.y(), 
                                        color=(255,255,255), batch=self.batch, group=self.group)     
        if not double:
            self.tip = pyglet.shapes.Triangle(x=0, y=0, 
                                        x2=0, y2=0, 
                                        x3=0, y3=0,
                                        color=(255,255,255), batch=self.batch)      
            self.update_tip_pos()
        self.update_arc_pos()

    def calculate_tip_pos(self):
        # ARROW SLOPE
        if (self.arc.y2-self.arc.y) != 0:
            self.slope = (self.arc.x2-self.arc.x)/(self.arc.y2-self.arc.y)
        else:
            self.slope = 999
        # ARROW ANGLE
        if self.n1.y() < self.n2.y():
            angle_t1 = atan(self.slope)+pi          
        else:
            angle_t1 = atan(self.slope) 
        angle_t2 = angle_t1+0.26
        angle_t3 = angle_t1-0.26
        r2 = self.n2.r()+15
        x_tip1 = sin(angle_t1)*self.n2.r()+self.n2.x()
        y_tip1 = cos(angle_t1)*self.n2.r()+self.n2.y()
        x_tip2 = sin(angle_t2)*(r2)+self.n2.x()
        y_tip2 = cos(angle_t2)*(r2)+self.n2.y()
        x_tip3 = sin(angle_t3)*(r2)+self.n2.x()
        y_tip3 = cos(angle_t3)*(r2)+self.n2.y()
        return (x_tip1,y_tip1,x_tip2,y_tip2,x_tip3,y_tip3)

    def update_arc_pos(self):
        self.arc.position = (self.n1.x(),self.n1.y(),self.n2.x(),self.n2.y())

    def update_tip_pos(self):
        self.tip.position = self.calculate_tip_pos()
            
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.update_arc_pos()
        if not self.double:
            self.update_tip_pos()

class GrafoPlot(pyglet.window.Window):
    def __init__(self, width=800, height=600):
        super().__init__(width=width, height=height, caption="Grafo")
        self.batch = pyglet.graphics.Batch()    
        self.nodes = {}
        self.grid = []
        self.placeholders = []

    def init_positions(self,size):
        
        padding = 30
        grid_width =  self.width  - padding
        grid_height = self.height - padding
        grid_node_dist_x = grid_width  // size 
        grid_node_dist_y = grid_height // size 
        grid_offset_x = grid_node_dist_x//2+padding//2
        grid_offset_y = grid_node_dist_y//2+padding//2
        for posx in range(size):
            for posy in range(size):
                self.placeholders.append(pyglet.shapes.Circle(grid_offset_x+grid_node_dist_x*posx,
                                                                grid_offset_y+grid_node_dist_y*posy,
                                                                10,batch=self.batch,color=(0,0,255)))
                self.grid.append((grid_offset_x+grid_node_dist_x*posx,grid_offset_y+grid_node_dist_y*posy))
        print(self.grid)
                
    def push_node_handlers(self, node):
        super().push_handlers(node.on_mouse_drag)
        super().push_handlers(node.on_mouse_motion)

    def push_arc_handlers(self, arc):
        super().push_handlers(arc.on_mouse_drag)

    def add_node(self,label,x,y,r):
        new_node = GNode(label, x, y, r, self.batch)
        self.nodes[new_node.name()] = [new_node]
        self.push_node_handlers(new_node)

    def add_arc(self,node_1,node_2,double=False):
        new_arc = GArc(self.nodes[node_1][0],self.nodes[node_2][0],self.batch, double)
        self.nodes[node_1].append(new_arc)           
        self.push_arc_handlers(new_arc)
 
    def parse_graph(self,graph):
        """Takes a Grafo() object and creates GNode's and GArc's"""
        # Prepare node positions
        size = int(sqrt(graph.n_vertices()))+1
        self.init_positions(size)
        # Add nodes 
        for n in graph.vertices():
            coord = choice(self.grid)
            self.add_node(n,coord[0],coord[1],25)
            self.grid.remove(coord)
            print(coord)
        # Add arcs
        for s in graph.vertices():
            next_one = graph.primer_adyacente(s)
            next_one_list = graph.primer_adyacente(next_one.valor())
            while next_one_list != s and next_one_list != None:
                next_one_list = next_one_list.proximo()





    def push_all_handlers(self):
        for n in self.nodes:
            super().push_handlers(n.on_mouse_drag)
            super().push_handlers(n.on_mouse_motion)

    def on_draw(self):
        self.clear()
        self.batch.draw()

# EJEMPLO
if __name__ == '__main__':
    gplot = GrafoPlot(800,600)
    grafo1 = Grafo()

    grafo1.insertar("ESQ","TRV",True)
    grafo1.insertar("CHL","TRV",True)
    grafo1.insertar("ESQ","TCK",True)
    grafo1.insertar("TCK","TLW",True)
    grafo1.insertar("RWS","TLW",True)
    grafo1.insertar("PTM","RWS",True)
    grafo1.insertar("TLW","CMD",True)
    grafo1.insertar("CMD","TCK",True)

    gplot.parse_graph(grafo1)
    pyglet.app.run()
