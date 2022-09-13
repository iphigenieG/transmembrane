from hydrophobicity import hydrophobicity_score
import points
import membrane
import skeleton
import sphere

class Scanner():
    def __init__(self,step = 1.5):
        self.step = step
    
    def scan_prot(self,hemisphere:sphere.Sphere,prot:skeleton.Skeleton):
        max_score = 0  
        for p in hemisphere.point_list :
                norm = points.Vector(p.get())
                start_point = prot.get_ymin()
                start = membrane.Membrane(norm,start_point)
                v = points.Vector(norm.get())
                v.set(v.x*self.step,v.y*self.step,v.z*self.step)
                while(start_point.y<=prot.get_ymax().y):
                    in_residues = []
                    for residue in prot.content():
                        if (start.point_isin(residue.alpha)):
                            in_residues.append(residue.name)
                    if (len(in_residues)!=0):
                        max_score = max(hydrophobicity_score(in_residues),max_score)
                    v.move_point(start_point)
                    start.move_membrane(start_point)
        return max_score,start