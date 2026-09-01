from hydrophobicity import hydrophobicity_score
import points
import membrane
import skeleton
import sphere
import numpy as np
import copy

class Scanner():
    """Scanner class to compare scores for each membrane position and return best result
    Attributes
    ----------
    width : int
        width of the lipid membrane

    Methods
    -------
    scan_prot():
        scans the protein to find best membrane position (more with command help(scan_prot))

    """
    def __init__(self,width = 14):
        self.width = width
    
    def scan_prot(self,hemisphere:sphere.Sphere,prot:skeleton.Skeleton,step=1):
        """Scan the protein along every direction sampled on the hemisphere by sliding a
        membrane-width band from one extremity of the protein to the other and score each position (see hydrophobicity.py)

        Parameters
        ----------
        hemisphere : sphere.Sphere
            Set of directions of plane for the "scannning" membrane
        prot : skeleton.Skeleton
            The protein to scan
        step : int, optional
            Step size, size of the "jump" between score computation, default 1 Angstrom

        Returns
        -------
        tuple[float, membrane.Membrane]
            The best hydrophobicity score found, and the membrane position that achieved it.
        """
        max_score = 0  
        best_membrane = None
        ymin_coord = prot.get_ymin()
        ymax_coord = prot.get_ymax()

        for p in hemisphere.point_list :
            norm = points.Vector(p.get())
            norm_arr = np.array(norm.get())
            if np.dot(norm_arr, ymin_coord) <= np.dot(norm_arr, ymax_coord):
                start_coord, target_coord = ymin_coord, ymax_coord
            else:
                start_coord, target_coord = ymax_coord, ymin_coord
            start_point = points.Coord(*start_coord)
            end_point = points.Coord(*target_coord)
            start = membrane.Membrane(norm,start_point,self.width)
            v = points.Vector(norm.get())
            v.set(v.x*step,v.y*step,v.z*step)
            while(not(start.point_isin(end_point))):
                in_residues = []
                for residue in prot.content():
                    if (start.point_isin(residue.alpha)):
                        in_residues.append(residue.name)
                if (len(in_residues) != 0):
                    score = hydrophobicity_score(in_residues)
                    if score > max_score:
                        max_score = score
                        best_membrane = copy.deepcopy(start)
                v.move_point(start_point)
                start.move_membrane(start_point)
        v.antimove_point(start_point)
        start.move_membrane(start_point)
        return max_score,best_membrane