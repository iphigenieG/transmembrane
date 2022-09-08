from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
p = PDBParser()
structure = p.get_structure("1JDM", "1jdm.pdb")
model = structure[0]
dssp = DSSP(model, "1jdm.pdb")

for residue in dssp.keys()[0:10] :
    print(f"residue {residue[1][1]} {dssp[residue][1]} : ACC = {dssp[residue][3]}")