import points
import numpy as np

class Membrane():
    """Membrane 
    Attributes
    ----------
    norm : np.array
        norm vector perpendicular to membrane plane
    
    start_point : np.array
        point to compute equation of membrane plane
    
    width : int
        width of membrane
    
    d1, d2 : np.array
        solutions of the plane equation of the bottom and the top of the membrane respectively

    Methods
    -------
    move_membrane() :
        recompute membran plane equations from new input start_point
    
    point_isin() : -> bool
        returns true if input point coordinates are in the space between the two membrane planes

    """
    def __init__(self,norm:points.Vector,plane_point:points.Coord, width=14):
        self.norm = np.array(norm.get())
        self.start_point = np.array(plane_point.get())
        self.width = width
        self.d1 = np.sum(self.norm * self.start_point)
        self.d2 = np.sum(self.norm * (self.width * self.norm + self.start_point))
    
    def move_membrane (self,plane_point:points.Coord):
        self.start_point = np.array(plane_point.get())
        self.d1 = np.sum(self.norm * self.start_point)
        self.d2 = np.sum(self.norm * (self.width * self.norm + self.start_point))

    def point_isin(self,point:points.Coord):
        p_coord = np.array(point.get())
        if ((np.sum(self.norm*p_coord)>=self.d1) and (np.sum(self.norm*p_coord)<=self.d2)):
            return True
        else : return False