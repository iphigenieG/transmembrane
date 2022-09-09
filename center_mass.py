from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
p = PDBParser()
structure = p.get_structure("1JDM", "1jdm.pdb")
model = structure[0]

CA = {"x":[],"y":[],"z":[]}

for chain in model:
    for residue in chain:
        coord = residue['CA'].get_coord()
        CA["x"].append(coord[0])
        CA["y"].append(coord[1])
        CA["z"].append(coord[2])
center_x = sum(CA["x"])/len(CA["x"])
center_y = sum(CA["y"])/len(CA["y"])
center_z = sum(CA["z"])/len(CA["z"])

min_x= min(CA["x"])
max_x= max(CA["x"])

min_y= min(CA["y"])
max_y= max(CA["y"])

min_z= min(CA["z"])
max_z= max(CA["z"])