from hydrophobicity import hydrophobicity_score
import points
import membrane
import skeleton
import sphere

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
        """scan_prot _summary_

        Parameters
        ----------
        hemisphere : sphere.Sphere
            _description_
        prot : skeleton.Skeleton
            _description_
        width : int, optional
            _description_, by default 14

        Returns
        -------
        _type_
            _description_
        """
        max_score = 0  
        for p in hemisphere.point_list :
            norm = points.Vector(p.get())
            start_point = points.Coord(*prot.get_ymin())
            start = membrane.Membrane(norm,start_point,self.width)
            v = points.Vector(norm.get())
            v.set(v.x*step,v.y*step,v.z*step)
            while(not(start.point_isin(prot.ymax_point))):
                in_residues = []
                for residue in prot.content():
                    if (start.point_isin(residue.alpha)):
                        in_residues.append(residue.name)
                if (len(in_residues) != 0):
                    max_score = max(hydrophobicity_score(in_residues),max_score)
                v.move_point(start_point)
                start.move_membrane(start_point)
        v.antimove_point(start_point)
        start.move_membrane(start_point)
        return max_score,start