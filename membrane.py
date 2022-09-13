import points
import numpy as np

class Membrane():
    def __init__(self,norm:points.Vector,plane_point:points.Coord, width=14):
        self.norm = np.array(norm.get())
        self.start_point = np.array(plane_point.get())
        self.width = width
        self.d1 = np.sum(self.norm*self.start_point)
        self.d2 = np.sum(self.norm*self.width*self.start_point)
    
    def move_membrane (self,plane_point:points.Coord):
        self.start_point = np.array(plane_point.get())
        self.d1 = np.sum(self.norm*self.start_point)
        self.d2 = np.sum(self.norm*self.width*self.start_point)

    def point_isin(self,point:points.Coord):
        p_coord = np.array(point.get())
        if ((np.sum(self.norm*p_coord)>=self.d1) and (np.sum(self.norm*p_coord)<=self.d2)):
            return True
        else : return False