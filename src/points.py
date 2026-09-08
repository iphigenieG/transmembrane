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
    cross(Vector):
        computes and returns cross product of the two vectors
    dot(Vector):
        computes and returns dot product of the two vectors
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

    def cross(self, other_vector : "Vector"):
        """ cross computes the cross product between this vector and a given vector

        Parameters
        ----------
        other_vector : Vector
            vector to compute cross product with
        """
        a_coords = self.get()
        b_coords = other_vector.get()
        i = a_coords[1]*b_coords[2] - a_coords[2]*b_coords[1]
        j = a_coords[2]*b_coords[0] - a_coords[0]*b_coords[2]
        k = a_coords[0]*b_coords[1] - a_coords[1]*b_coords[0]
        cross_vector = Vector([i,j,k])
        return cross_vector

    def dot(self, other_vector : "Vector"):
            """ dot computes the dot product between this vector and a given vector
    
            Parameters
            ----------
            other_vector : Vector
                vector to compute dot product with
            """
            a_coords = self.get()
            b_coords = other_vector.get()
            return sum(a_i*b_i for a_i, b_i in zip(a_coords, b_coords))