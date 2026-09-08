""" This script scans a protein to find the best placement for a 14 angstrom wide membrane

    Usage
    -------
    python main.py [pdb filename] | [step](optional)
"""
import sys
import sphere
import skeleton
import scanner
import points
import matplotlib.pyplot as plt
import numpy as np

def plane_points(d, norm, S, T, u, v):
    p0 = points.Coord(0,0,0)
    delta = points.Vector([c * d for c in norm.get()])
    delta.move_point(p0)
    
    list_u = u.get()
    list_v = v.get()
    list_p0 = p0.get()

    X = list_p0[0] + S*list_u[0] + T*list_v[0]
    Y = list_p0[1] + S*list_u[1] + T*list_v[1]
    Z = list_p0[2] + S*list_u[2] + T*list_v[2]
    return X, Y, Z

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("ERREUR : il faut au moins un nom de fichier .pdb en argument.")
    prot_file = sys.argv[1]
    id = prot_file.split(".")[0].split("/")[1]
    prot = skeleton.Skeleton(id.capitalize(),prot_file)
    s = sphere.Sphere(100)
    if len(sys.argv) == 3 :
        width= int(sys.argv[2])
        if width <= 0 :
            sys.exit("ERREUR : the membrane width must be strictly superior to zero")
        scan = scanner.Scanner(width = width)
    else : scan = scanner.Scanner()
    prot.center()
    max_score,best_membrane = scan.scan_prot(s,prot)
    if best_membrane is None:
        sys.exit("No membrane-spanning region could be identified for this protein ")

    print(max_score)
    print(best_membrane.start_point)

    for residue in prot.content():
        if(best_membrane.point_isin(residue.alpha)) :
            print(residue.name)

    ## Plotting alternative without zero division risk
    # We will use vector equation instead of scalar
    # First, we get two spanning vectors of the plane
    norm = points.Vector(best_membrane.norm)
    vector_lambda = points.Vector([0,1,0])
    u = norm.cross(vector_lambda)
    if(u.dot(u) <= 1e-10):
        vector_lambda.set(1,0,0)
        u = norm.cross(vector_lambda)

    v = u.cross(norm)

    scaled_u = points.Vector([c / np.sqrt(u.dot(u)) for c in u.get()])
    scaled_v = points.Vector([c / np.sqrt(v.dot(v)) for c in v.get()])

    # Then we get a vector as a proxy for the Y-axis "size" of the protein in order 
    # to use a comparable scale for plotting our membrane planes
    prot_vector = points.Vector([hi-lo for hi,lo in zip(prot.get_ymax(), prot.get_ymin())])
    size_prot = np.sqrt(prot_vector.dot(prot_vector))
    extent = size_prot / 2 + 5
    lsp = np.linspace(-extent, extent, 30)

    # Finally we get our plane points and grid using the parametric eqation of the plane p = p_0 + s * u + t * v
    S,T = np.meshgrid(lsp,lsp)
    X1,Y1,Z1 = plane_points(best_membrane.d1,norm,S,T,scaled_u,scaled_v)
    X2,Y2,Z2 = plane_points(best_membrane.d2,norm,S,T,scaled_u,scaled_v)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X1, Y1, Z1) 
    ax.plot_surface(X2,Y2,Z2)
    
    res_list = prot.content()
    for residue in res_list:
        point = residue.alpha.get()
        in_membrane = best_membrane.point_isin(residue.alpha)
        ax.scatter(*point, color='red' if in_membrane else 'steelblue', s=45)
    ax.set_aspect("equal")
    ax.set_xlabel("X(Å)")
    ax.set_ylabel("Y(Å)")
    ax.set_zlabel("Z(Å)")
    ax.set_title(f"Predicted transmembrane section of {id}")

    plt.show()


    # # plot the membrane and the CA skeleton of the protein together
    # vect = best_membrane.norm
    # a = vect[0]
    # b = vect[1]
    # c = vect[2]

    # x = np.linspace(-15,15,30)
    # y = np.linspace(-15,15,30)

    # X,Y = np.meshgrid(x,y)
    # Z = (best_membrane.d1 - a*X - b*Y) / c
    # Z2 = (best_membrane.d2 - a*X - b*Y) / c
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d', autoscale_on=False)

    # ax.plot_surface(X, Y, Z) 
    # ax.plot_surface(X,Y,Z2)
    
    # res_list = prot.content()
    # for residue in res_list:
    #     point = residue.alpha.get()
    #     in_membrane = best_membrane.point_isin(residue.alpha)
    #     ax.scatter(*point, color='red' if in_membrane else 'steelblue', s=45)

    # plt.show()


    