def hydrophobicity_score(residues):
    hydrophobicity = {"PHE":1, "GLY":1, "ILE":1, "LEU":1, "MET":1, "VAL":1, "TRP":1 ,"TYR":1,
    "ALA":0, "CYS":0, "ASP":0, "GLU":0, "HIS":0, "LYS":0, "ASN":0, "PRO":0, "GLN":0, "ARG":0, "SER":0 ,"THR":0}
    score = sum([hydrophobicity[residue] for residue in residues])/len(residues)
    return score

