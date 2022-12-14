""" This script scans a protein to find the best placement for a 14 angstrom wide membrane

    Usage
    -------
    python main.py [pdb filename] | [step](optional)
"""
import sys
from turtle import width
import sphere
import skeleton
import scanner
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("ERREUR : il faut au moins un nom de fichier .pdb en argument.")
    prot_file = sys.argv[1]
    id = prot_file.split(".")[0]
    prot = skeleton.Skeleton(id.capitalize(),prot_file)
    s = sphere.Sphere(25)
    if len(sys.argv) == 3 :
        width= int(sys.argv[2])
        if width <= 0 :
            sys.exit("ERREUR : the membrane width must be strictly superior to zero")
        scan = scanner.Scanner(width = width)
    else : scan = scanner.Scanner()
    prot.center()
    max,best_membrane = scan.scan_prot(s,prot)
    print(max)
    print(best_membrane.start_point)
    for residue in prot.content():
        if(best_membrane.point_isin(residue.alpha)) :
            print(residue.name)


    # plot the membrane and the CA skeleton of the protein together
    vect = best_membrane.norm
    a = vect[0]
    b = vect[1]
    c = vect[2]

    x = np.linspace(-10,10,20)
    y = np.linspace(-10,10,20)

    X,Y = np.meshgrid(x,y)
    Z = (best_membrane.d1 - a*X - b*Y) / c
    Z2 = (best_membrane.d2 - a*X - b*Y) / c
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y, Z) 
    ax.plot_surface(X,Y,Z2)
    
    res_list = prot.content()
    for residue in res_list:
        point = residue.alpha.get()
        ax.scatter(*point, color = "blue")

    plt.show()