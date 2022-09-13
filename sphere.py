import math
from hydrophobicity import hydrophobicity_score
import membrane
import points
import skeleton
#import matplotlib.pyplot as plt

class Sphere ():
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

    def scan_prot(self,prot:skeleton.Skeleton,step=1.5):
        max_score = 0  
        for p in self.point_list :
                norm = points.Vector(p.get())
                start_point = prot.get_ymin()
                start = membrane.Membrane(norm,start_point)
                v = points.Vector(norm.get())
                v.set(v.x*step,v.y*step,v.z*step)
                while(start_point.y<=prot.get_ymax().y):
                    in_residues = []
                    for residue in prot.content():
                        if (start.point_isin(residue.alpha)):
                            in_residues.append(residue.name)
                    if (len(in_residues)!=0):
                        max_score = max(hydrophobicity_score(in_residues),max_score)
                    v.move_point(start_point)
                    start.move_membrane(start_point)
        return max_score,start
#     def show_scatter(self):
#         fig = plt.figure()
#         ax = fig.add_subplot(projection='3d')

#         for point in self.point_list :
#             ax.scatter3D(*(point.get()), color = "blue")
#         ax.scatter(0,-1,0, color="red")
#         plt.show()

# if __name__ == "__main__":
#     sphere = Sphere(100)
#     sphere.show_scatter()

if __name__ == "__main__":
    prot = skeleton.Skeleton("1JDM","1jdm.pdb")
    s = Sphere(25)
    prot.center()
    max,best_membrane = s.scan_prot(prot)
    print(max)
    print(best_membrane.start_point)