import math
from hydrophobicity import hydrophobicity_score
import membrane
import points
import skeleton
import matplotlib.pyplot as plt
import numpy as np

class Sphere ():
    """
    A class to represent points on a hemisphere.

    Attributes
    ----------
    samples : int
        number of point to distribute on the half sphere

    Methods
    -------
    __fibonacci_sphere(samples):
        Generates the points distributed on the hemisphere.

        This method uses the Fibonacci lattice sphere algorithm 
        to generate the hemisphere points distribution
        as implemented here : 
        https://stackoverflow.com/a/26127012 
    """
    def __init__(self,samples=100):
        self.point_list = self.__fibonacci_sphere(samples)

    def __fibonacci_sphere(self,samples):

        point_list = []
        phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

        for i in range(samples):

            y = 1 - (i / float(samples - 1)) # y goes from 1 to 0

            radius = math.sqrt(1 - y * y)  # radius at y

            theta = phi * i  # golden angle increment

            x = math.cos(theta) * radius
            z = math.sin(theta) * radius

            point = points.Coord(x,y,z)
            point_list.append(point)

        return point_list
    
    def show_scatter(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        for point in self.point_list :
            ax.scatter(*(point.get()), color = "blue")
        ax.scatter(0,-1,0, color="red")
        plt.show()

if __name__ == "__main__":

    sphere = Sphere(100)
    sphere.show_scatter()
