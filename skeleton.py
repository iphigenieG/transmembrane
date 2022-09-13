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
        for chain in model:
            for i,residue in enumerate(chain):
                coords = list(residue['CA'].get_coord())
                acc = dssp[dssp.keys()[i]][3]
                self.residue_list.append(Residue(coords,residue.get_resname(),acc))
    
    def content(self):
        for residue in self.residue_list:
            residue.info()

class Residue:
    """residue in protein"""
    
    def __init__(self,coords, name, acc):
        self.alpha = points.Point(coords)
        self.name = name
        self.acc = acc

    def info(self):
        print(f"{self.name} : {self.alpha.get()} ACC = {self.acc}")


if __name__ == "__main__":
    prot = Skeleton("1JDM","1jdm.pdb")
    prot.content()