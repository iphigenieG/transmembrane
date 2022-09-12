class Coord:
    """Set of cartesian coordinates"""

    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return list(self.x,self.y,self.z)

    def set(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Point(Coord):
    def __init__(self, coord_list):
        super().__init__(coord_list[0], coord_list[1], coord_list[2])

class Vector(Coord):
    def __init__(self, coord_list):
        super().__init__(coord_list[0], coord_list[1], coord_list[2])
    
    def move_point(self, point : Point):
        coords = point.get()
        delta = self.get()
        for i in range(3):
            coords[i]=coords[i]+delta[i]
        point.set(coords)

