from Bio.PDB import PDBParser as p
import points
class Skeleton:
    """alpha carbon skeleton of protein"""

    def __init__(self, prot_id:str, prot_file:str):
        model = p.get_structure(prot_id, prot_file)[0]
        self.residue_list = []
        for chain in model:
            for residue in chain:
                coords = list(residue['CA'].get_coord())
                self.residue_list.append(Residue(coords,residue['CA'].get_resname()))

class Residue:
    """residue in protein"""
    
    def __init__(self,coords, name):
        self.alpha = points.Point(coords)
        self.name = name