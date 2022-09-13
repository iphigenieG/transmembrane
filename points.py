class Coord:
    """Set of cartesian coordinates"""

    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return [self.x,self.y,self.z]

    def set(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
class Vector(Coord):
    def __init__(self, coord_list):
        super().__init__(*coord_list)
    
    def move_point(self, point : Coord):
        coords = point.get()
        delta = self.get()
        for i in range(3):
            coords[i]=coords[i]+delta[i]
        point.set(*coords)

