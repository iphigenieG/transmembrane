import copy

class Coord:
    """Set of cartesian coordinates to represent point of vector"""

    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return [copy.deepcopy(self.x),copy.deepcopy(self.y),copy.deepcopy(self.z)]

    def set(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
class Vector(Coord):
    """Vector mathematical vector -> extends Coord

    Methods
    -------
    move_point(Coord):
        applies vector transformation to given point
    antimove_point(Coord):
        applies the the vector transformation opposite to this vector to given point
    """
    def __init__(self, coord_list):
        super().__init__(*coord_list)
    
    def move_point(self, point : Coord):
        """move_point applies vector transformation to given point

        Parameters
        ----------
        point : Coord
            Point to be moved
        """
        coords = point.get()
        delta = self.get()
        for i in range(3):
            coords[i]=coords[i]+delta[i]
        point.set(*coords)

    def antimove_point(self, point : Coord):
        """antimove_point applies transformation in opposite direction of vector to given point

        Parameters
        ----------
        point : Coord
            Point to move
        """
        coords = point.get()
        delta = self.get()
        for i in range(3):
            coords[i]=coords[i]-delta[i]
        point.set(*coords)
