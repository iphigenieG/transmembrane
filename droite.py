def atom_is_transmembrane(atom):
    sphere_point = (0,1,0)
    min_point = (xmin,ymin,zmin)
    membraine_width = 14

    d1 = sphere_point[0]*min_point[0]+sphere_point[1]*min_point[1]+sphere_point[2]*min_point[2]
    d2 = sphere_point[0]*(min_point[0]+sphere_point[0]*membraine_width)+sphere_point[1]*(min_point[1]+sphere_point[1]*membraine_width)+sphere_point[2]*(min_point[2]+sphere_point[2]*membraine_width)
    if ((sphere_point[0]*atom.x+sphere_point[1]*atom.y+sphere_point[2]*atom.z>d1) and (sphere_point[0]*atom.x+sphere_point[1]*atom.y+sphere_point[2]*atom.z<d2)):
        return 1 
    else : return 0
