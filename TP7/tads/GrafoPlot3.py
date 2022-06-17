import pyglet 

from math import atan, sin, cos, pi, sqrt
from random import choice
from Grafo import Grafo

# Enable Antialiasing
pyglet.gl.glEnable(pyglet.gl.GL_LINE_SMOOTH)
pyglet.gl.glEnable(pyglet.gl.GL_POLYGON_SMOOTH)

colors = {
    "node_bg":      (36, 32, 25),
    "node_bg_hover":(69, 58, 40),
    "node_fg":      (255, 255, 255, 255),
    "window_bg":    (20, 18, 18),
    "arc_fg":       (255, 255, 255, 255)
}
      
class GNode():
    """ Creates a visible node. Use 'value' for naming the node, 'x' and 'y' for initial position, 'r' for radius and
    'n_batch' for specifying a drawing batch"""
    def __init__(self, value, x, y, r, n_batch):
        self.radius = r
        self.n_value = value
        self.batch = n_batch
        self.bg_color = colors["node_bg"]
        self.fg_color = colors["node_fg"]
        self.bg_hover_color = colors["node_bg_hover"]
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)
        self.mouse_over = False
        self.shape = pyglet.shapes.Circle(x, y, self.radius, color=(36, 32, 25),
                                        batch=self.batch, group=self.background)
        self.label = pyglet.text.Label(text=self.n_value, color=self.fg_color, 
                                       font_size=12,x=self.shape.x, y=self.shape.y,
                                       anchor_x="center", anchor_y="center",
                                       batch=self.batch, group=self.foreground)
    def update_pos(self, x, y):
        """ Changes the position of the node using 'x' and 'y' """
        self.shape.x = x
        self.shape.y = y
        self.label.x = self.shape.x
        self.label.y = self.shape.y

    def value(self):
        """ Returns the current value of the node"""
        return self.n_value

    def x(self):
        """ Returns the current x position of the node"""
        return self.shape.x
    
    def y(self):
        """ Returns the current y position of the node"""
        return self.shape.y

    def r(self):
        """ Returns the current radius of the node"""
        return self.radius
        
    def check_boundaries(self,x,y):
        """ Checks if (x,y) coordinates overlap with the node's shape area"""
        m_range_x = x in range(self.shape.x-self.radius,self.shape.x+self.radius)
        m_range_y = y in range(self.shape.y-self.radius,self.shape.y+self.radius)
        return m_range_x and m_range_y

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handler for mouse movement. """
        self.mouse_over = self.check_boundaries(x,y)
        if self.mouse_over:
            self.shape.color = self.bg_hover_color
        else:
            self.shape.color = self.bg_color

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """ Handler for mouse click and drag. """
        if self.mouse_over:
            self.update_pos(x,y)

class GArc():
    """ Creates a visible arc as an arrow if double == False or as a line if double == False, and connects it between two existing nodes."""
    def __init__(self, node_1, node_2,l_batch, double=False):
        self.n1 = node_1
        self.n2 = node_2    
        self.batch = l_batch
        self.double = double
        self.group = pyglet.graphics.OrderedGroup(-1)
        self.arc = pyglet.shapes.Line(x=self.n1.x(), y=self.n1.y(), 
                                        x2=self.n2.x(),y2=self.n2.y(), 
                                        color=(255,255,255), batch=self.batch, group=self.group)     
        self.update_arc_pos()
        if not double:
            self.tip = pyglet.shapes.Triangle(x=0, y=0, 
                                        x2=0, y2=0, 
                                        x3=0, y3=0,
                                        color=(255,255,255), batch=self.batch)      
            self.update_tip_pos()

    def calculate_tip_pos(self):
        """ Calculates the tip position of the arrow depending on the slope of the line """
        # Calculate line slope
        if (self.arc.y2-self.arc.y) != 0:
            self.slope = (self.arc.x2-self.arc.x)/(self.arc.y2-self.arc.y)
        elif self.arc.x2 > self.arc.x:
            self.slope = -999
        else:
            self.slope = 999
        # Calculate tip position
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
        """ Updates the arc position according to the affected nodes positions"""
        self.arc.position = (self.n1.x(),self.n1.y(),self.n2.x(),self.n2.y())

    def update_tip_pos(self):
        """ Updates the tip position """
        self.tip.position = self.calculate_tip_pos()
            
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """ Handler for mouse click and drag """
        self.update_arc_pos()
        if not self.double:
            self.update_tip_pos()

class GraphPlot(pyglet.window.Window):
    """ Creates a pyglet.window and initializes a GraphPlot object"""
    def __init__(self, width=800, height=600):
        super().__init__(width=width, height=height, caption="Grafo")
        self.bgColor = colors["window_bg"]
        pyglet.gl.glClearColor(self.bgColor[0]/255, self.bgColor[1]/255, self.bgColor[2]/255, 1.0)
        self.batch = pyglet.graphics.Batch()    
        self.nodes = {}
        self.grid = []
        self.placeholders = []

    def init_positions(self,size):
        """ Pre-calculates a grid of positions for the nodes, according to how many there are. The positions will
        always be random."""
        padding = 30
        grid_width =  self.width  - padding
        grid_height = self.height - padding
        grid_node_dist_x = grid_width  // size 
        grid_node_dist_y = grid_height // size 
        grid_offset_x = grid_node_dist_x//2+padding//2
        grid_offset_y = grid_node_dist_y//2+padding//2
        for posx in range(size):
            for posy in range(size):
                self.grid.append((grid_offset_x+grid_node_dist_x*posx,grid_offset_y+grid_node_dist_y*posy))
        print(self.grid)

    def run(self):
        """ Shows the plot """
        pyglet.app.run()
                
    def push_node_handlers(self, node):
        """ Passes the handlers from the Window to the specified node """
        super().push_handlers(node.on_mouse_drag)
        super().push_handlers(node.on_mouse_motion)

    def push_arc_handlers(self, arc):
        """ Passes the handlers from the Window to the specified arc"""
        super().push_handlers(arc.on_mouse_drag)

    def add_node(self,label,x,y,r):
        """ Adds a node to the graph """
        new_node = GNode(label, x, y, r, self.batch)
        self.nodes[new_node.value()] = [new_node]
        self.push_node_handlers(new_node)

    def add_arc(self,node_1,node_2,double=False):
        """ Adds an arc to the graph """
        if node_1 in self.nodes and node_2 in self.nodes:
            new_arc = GArc(self.nodes[node_1][0],self.nodes[node_2][0],self.batch, double)
            self.nodes[node_1].append(new_arc)           
            self.push_arc_handlers(new_arc)
        else:
            raise IndexError("Couldn't find one or both nodes!")
 
    def parse_graph(self,graph):
        """ Parses a graph from the Grafo() class seen in TP7 """ 
        # Prepare node positions
        size = int(sqrt(graph.n_vertices()))+1
        arc_list = []
        self.init_positions(size)
        # Add nodes 
        for n in graph.vertices():
            coord = choice(self.grid)
            self.add_node(n,coord[0],coord[1],25)
            self.grid.remove(coord)
        # Gather every single arc
        for n1 in graph.vertices():
            n_list = graph.primer_adyacente(n1)
            if n_list != None:
                for n2 in n_list:
                    arc_list.append((n1,n2.valor(),False))

        # Search for non-oriented graphs
        for arc1 in arc_list:
            for arc2 in arc_list:
                if arc1[0] == arc2[1] and arc1[1] == arc2[0]:
                    arc_list.remove(arc2)
                    arc_list[arc_list.index(arc1)] = (arc1[0],arc1[1],True)

        # Add the arcs
        for arc in arc_list:
            self.add_arc(arc[0],arc[1],arc[2])

    def push_all_handlers(self):
        for n in self.nodes:
            super().push_handlers(n.on_mouse_drag)
            super().push_handlers(n.on_mouse_motion)

    def on_draw(self):
        self.clear()
        self.batch.draw()

# EJEMPLO
if __name__ == '__main__':
    grafo1 = Grafo()
    grafo1.insertar("ESQ","TRV",True)
    grafo1.insertar("CHL","ESQ")
    grafo1.insertar("ESQ","BSA")
    grafo1.insertar("GCA","BSA")
    grafo1.insertar("BSA","GCA")

    gplot = GraphPlot(800,600)
    gplot.parse_graph(grafo1)
    gplot.run()
