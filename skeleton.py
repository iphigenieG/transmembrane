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
                coords = list(residue['CA'].get_coord())
                x.append(coords[0])
                y.append(coords[1])
                z.append(coords[2])

                acc = dssp[dssp.keys()[i]][3]
                self.residue_list.append(Residue(coords,residue.get_resname(),acc))
        self.center_x = sum(x)/len(x)
        self.center_y = sum(y)/len(y)
        self.center_z = sum(z)/len(z)
    
    def content(self):
        for residue in self.residue_list:
            residue.info()
    
    def center(self):
        delta = points.Vector([-self.center_x,-self.center_y,-self.center_z])
        for residue in self.residue_list :
            residue.move(delta)


class Residue:
    """residue in protein"""
    
    def __init__(self,coords, name, acc):
        self.alpha = points.Coord(*coords)
        self.name = name
        self.acc = acc

    def move(self,delta: points.Vector):
        delta.move_point(self.alpha)

    def info(self):
        print(f"{self.name} : {self.alpha.get()} ACC = {self.acc}")

if __name__ == "__main__":
    prot = Skeleton("1JDM","1jdm.pdb")
    prot.content()
    prot.center()
    print(prot.center_x)
    print(prot.center_y)
    print(prot.center_z)
    prot.content()