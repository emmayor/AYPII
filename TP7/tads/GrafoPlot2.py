import pyglet 

from math import atan, sin, cos, pi

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
                                       font_size=14,x=self.shape.x, y=self.shape.y,
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
        self.arc = pyglet.shapes.Line(x=self.n1.x(), y=self.n1.y(), 
                                       x2=self.n2.x(),y2=self.n2.y(), 
                                        color=(255,255,255), batch=self.batch)     

        self.tip = pyglet.shapes.Triangle(x=0, y=0, 
                                        x2=0, y2=0, 
                                        x3=0, y3=0,
                                        color=(255,255,255), batch=self.batch)      
        if double:
            self.tip2 = pyglet.shapes.Triangle(x=0, y=0, 
                                        x2=0, y2=0, 
                                        x3=0, y3=0,
                                        color=(255,255,255), batch=self.batch)   
            
        self.update_pos()

    def calculate_tip_pos(self,node):
        # ARROW SLOPE
        if (self.arc.y2-self.arc.y) != 0:
            self.slope = (self.arc.x2-self.arc.x)/(self.arc.y2-self.arc.y)
        # ARROW ANGLE
        if self.n1.y() < self.n2.y():
            angle_t1 = atan(self.slope)          
        else:
            angle_t1 = atan(self.slope)+pi 
        if node == self.n2:
            angle_t1 += pi
        angle_t2 = angle_t1+0.26
        angle_t3 = angle_t1-0.26

        x_tip1 = sin(angle_t1)*node.r()+node.x()
        y_tip1 = cos(angle_t1)*node.r()+node.y()
        x_tip2 = sin(angle_t2)*(node.r()+15)+node.x()
        y_tip2 = cos(angle_t2)*(node.r()+15)+node.y()
        x_tip3 = sin(angle_t3)*(node.r()+15)+node.x()
        y_tip3 = cos(angle_t3)*(node.r()+15)+node.y()
        return (x_tip1,y_tip1,x_tip2,y_tip2,x_tip3,y_tip3)

    def update_pos(self):
        self.arc.position = (self.n1.x(),self.n1.y(),self.n2.x(),self.n2.y())
        self.tip.position = self.calculate_tip_pos(self.n2)
        if self.double:
            self.tip2.position = self.calculate_tip_pos(self.n1)
            
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.update_pos()

class GrafoPlot(pyglet.window.Window):
    def __init__(self, width=800, height=600):
        super().__init__(width=width, height=height, caption="Grafo")
        self.batch = pyglet.graphics.Batch()    
        self.nodes = {}
        self.arcs = []
        self.grid = []
        self.push_node_handlers
        self.push_arc_handlers

    def generateGrid(self, size):
        padding = 30
        grid_width =  self.width  - 2*padding
        grid_height = self.height - 2*padding
        grid_node_dist_x = grid_width  // size 
        grid_node_dist_y = grid_height // size 

        for posx in range(size):
            for posy in range(size):
                self.grid.append((padding+grid_node_dist_x*posx,
                                  padding+grid_node_dist_y*posy))

    def push_node_handlers(self, node):
        super().push_handlers(node.on_mouse_drag)
        super().push_handlers(node.on_mouse_motion)

    def push_arc_handlers(self, arc):
        super().push_handlers(arc.on_mouse_drag)

    def addNode(self,label,x,y,r):
        new_node = GNode(label, x, y, r, self.batch)
        self.nodes[new_node.name()] = [new_node]
        self.push_node_handlers(new_node)
        #print(self.nodes)
        return new_node

    def addArc(self,node_1,node_2,double=False):
        new_arc = GArc(self.nodes[node_1][0], self.nodes[node_2][0],self.batch, double)
        self.nodes[node_1].append(new_arc)           
        self.push_arc_handlers(new_arc)
        print(self.nodes)
        

    def push_all_handlers(self):
        for n in self.nodes:
            super().push_handlers(n.on_mouse_drag)
            super().push_handlers(n.on_mouse_motion)
        for l in self.arrows:
            super().push_handlers(l.on_mouse_drag)

    def on_draw(self):
        self.clear()
        self.batch.draw()

# EXAMPLE
if __name__ == '__main__':
    gplot = GrafoPlot(800,600)
    gplot.addNode("EQS",500,400,30)
    gplot.addNode("TRV",200,500,30)
    gplot.addNode("TCK",300,500,30)
    gplot.addNode("BSA",100,60,30)
    
    gplot.addArc("EQS", "TRV")
    gplot.addArc("EQS", "TCK")
    gplot.addArc("EQS", "BSA", True)
    
    pyglet.app.run()
