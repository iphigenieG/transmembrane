import copy
from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
import points

class Skeleton:
    """Skeleton class to represent the Alpha Carbons of the protein chain.

    Attributes
    ----------
    residue_list: list of objets of class Residue
        list of objects representing tha Alpha Carbons of the protein

    start_center: instance of class points.Coord 
        coordinates of the initial center of mass of the protein as in the pdb file

    curr_center: instance of class points.Coord
        coordinates of the center of mass of the protein in its current possition

    ymin_point: instance of class points.Coord
        coordinates of the alpha carbon with the smallest value of y

    ymax_point: instance of class points.Coord
        coordinates of the alpha carbon with the bigest value of y

    Methods
    -------
    get ymin(), get_ymax(): 
        returns a list of values for the coordinates of ymin_point and ymax_point(), respectively

    content():
        returns a copy of the residue_list attribute

    print_content():
        prints information for each alpha carbon of the residue_list

    center(), reset_pos():
        moves the coordinates of the alpha carbons of the residue list to center the protein or reset the coordinates to their initial value

    """

    def __init__(self, prot_id:str, prot_file:str):
        p = PDBParser()
        model = p.get_structure(prot_id, prot_file)[0]
        dssp = DSSP(model, prot_file)
        self.residue_list = []
        x = []
        y = []
        z = []
        for chain in model:
            for i,residue in enumerate(chain):
                acc = dssp[dssp.keys()[i]][3]
                if (acc > 0.25):
                    coords = list(residue['CA'].get_coord())
                    x.append(coords[0])
                    y.append(coords[1])
                    z.append(coords[2])
                self.residue_list.append(Residue(coords,residue.get_resname()))
        center_x = sum(x)/len(x)
        center_y = sum(y)/len(y)
        center_z = sum(z)/len(z)
        self.start_center = points.Coord(center_x,center_y,center_z)
        self.curr_center = points.Coord(center_x,center_y,center_z)
        ymin_index = y.index(min(y))
        self.ymin_point = points.Coord(x[ymin_index],y[ymin_index],z[ymin_index])
        ymax_index = y.index(max(y))
        self.ymax_point = points.Coord(x[ymax_index],y[ymax_index],z[ymax_index])
    
    def get_ymin(self):
        return self.ymin_point.get()

    def get_ymax(self):
        return self.ymax_point.get()

    def content(self):
        return copy.deepcopy(self.residue_list)

    def print_content(self):
        for residue in self.residue_list:
            residue.info()
    
    def center(self):
        delta = points.Vector(self.curr_center.get())
        for residue in self.residue_list :
            residue.antimove(delta)
        self.curr_center = points.Coord(0,0,0)
        delta.antimove_point(self.ymin_point)
        delta.antimove_point(self.ymax_point)

    def reset_pos(self):
        delta = points.Vector(self.start_center.get())
        for residue in self.residue_list :
            residue.move(delta)
        self.curr_center = self.start_center
        delta.move_point(self.ymin_point)
        delta.move_point(self.ymax_point)

class Residue:
    """ Residue class to represent a residue of a protein

    Attributes
    ----------
    alpha : object of class points.Coord
        coordinates of the alpha carbon linked to residue
    name : str
        tree letter code name of residue

    Methods
    -------
    move(): 
        takes input Vector delta and applies its transformation to the coordinates of the alpha attribute
    antimove():
        takes input Vector delta and move the coordinates by the opposite vector to delta
    info():
        prints a message showing attributes of the instance of self
    """
    
    def __init__(self,coords, name):
        self.alpha = points.Coord(*coords)
        self.name = name

    def move(self,delta: points.Vector):
        delta.move_point(self.alpha)
    
    def antimove(self,delta: points.Vector):
        delta.antimove_point(self.alpha)

    def info(self):
        print(f"{self.name} : {self.alpha.get()}")

if __name__ == "__main__":
    prot = Skeleton("1JDM","1jdm.pdb")
    prot.print_content()
    prot.center()
    prot.print_content()
    prot.reset_pos()
    prot.print_content()