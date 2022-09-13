from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
import points

class Skeleton:
    """alpha carbon skeleton of protein"""

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
        return self.ymin_point

    def get_ymax(self):
        return self.ymax_point

    def content(self):
        return self.residue_list

    def print_content(self):
        for residue in self.residue_list:
            residue.info()
    
    def center(self):
        delta = points.Vector(self.curr_center.get())
        for residue in self.residue_list :
            residue.antimove(delta)
        self.curr_center = points.Coord(0,0,0)

    def reset_pos(self):
        delta = points.Vector(self.start_center.get())
        for residue in self.residue_list :
            residue.move(delta)
        self.curr_center = self.start_center

class Residue:
    """residue in protein"""
    
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