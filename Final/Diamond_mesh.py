import numpy as np
import re
import matplotlib.pyplot as plt

"""
Mesh generation script for diamond
"""

__author__ = "Trey Gower, David Valenzano, Ty Zimmerman"


def params():
    """ 
    enter paramters 
    """
    Lf = 1
    Lw = 2
    H = 1
    alpha_d =0
    #we will always have 32 vertices
    n = 32

    #H = float(input('Enter H: '))
    #Lw = float(input('Enter Lw (Length of one side of the domain): '))
    alpha_d = float(input('Enter angle of attack in degrees: '))
    alpha_r = np.deg2rad(alpha_d)

    return n, Lf,Lw, H, alpha_r

def generate_diamond(alpha):
    '''
    Generates diamond at various angles of attack
    '''
    #Diamond vertices
    theta = np.deg2rad(3.433)
    v12 = np.array((-.5, 0))
    v13 = np.array((0,.5*np.tan(theta)))
    v14 = np.array((.5,0))
    v15 = np.array((0, -.5*np.tan(theta)))

    # Rotation matrix to account for the angle of attack
    if alpha != 0:
        A = np.array([[np.cos(alpha), np.sin(alpha)],[-np.sin(alpha), np.cos(alpha)]])

        v12 = np.dot(A,v12)
        v13 = np.dot(A,v13)
        v14 = np.dot(A,v14)
        v15 = np.dot(A,v15)

    diamond = [v12,v13,v14,v15]
    return diamond
   
def generate_other_verts(diamond, Lf,Lw, H):
    '''
    generates all other vertices based on the diamond
    '''
    # Unpack diamond vertices
    v12, v13, v14, v15 = diamond

    # Extract x and y coordinates for convenience
    x12, y12 = v12
    x13, y13 = v13
    x14, y14 = v14
    x15, y15 = v15

       # Define other vertices based on diamond
    v0 = np.array((-Lf, -H))
    v1 = np.array((x12, -H))
    v2 = np.array((x15, -H))
    v3 = np.array((x14, -H))
    v4 = np.array((Lw, -H))
    v5 = np.array((Lw, y14))
    v6 = np.array((Lw, H))
    v7 = np.array((x14, H))
    v8 = np.array((x13, H))
    v9 = np.array((x12, H))
    v10 = np.array((-Lf, H))
    v11 = np.array((-Lf, y12))

    # Combine all vertices into a list
    vertices = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15]

    # Create a zero array for z-coordinates
    zvec = np.zeros((len(vertices), 1))
    zvec[:] = -.05
    # Stack vertices and z-coordinates horizontally
    vertices = np.hstack((np.array(vertices), zvec))
    vertices = np.concatenate((vertices, vertices), axis=0)
    vert_half = round(len(vertices)/2)
    vertices[vert_half:,2] = -vertices[vert_half,2]
    print(vertices)
    return vertices


def singlegraph(diamond):
    # Unpack diamond vertices
    v12, v13, v14, v15 = diamond

    # Extract x and y coordinates for convenience
    x12, y12 = v12
    x13, y13 = v13
    x14, y14 = v14
    x15, y15 = v15

    foretop = f'foretop:\n start   ({round(x12+.0005,4)}, {round(y12+.0005,4)}, {0.0})\n end   ({round(x13+.0005,4)}, {round(y13+.0005,4)}, {0.0})'
    forebot = f'forebot:\n start   ({round(x12-.0005,4)}, {round(y12-.0005,4)}, {0.0})\n end   ({round(x15-.0005,4)}, {round(y15-.0005,4)}, {0.0})'
    wakebot = f'wakebot:\n start   ({round(x15-.0005,4)}, {round(y15-.0005,4)}, {0.0})\n end   ({round(x14-.0005,4)}, {round(y14-.0005,4)}, {0.0})'
    waketop = f'waketop:\n start   ({round(x13+.0005,4)}, {round(y13+.0005,4)}, {0.0})\n end   ({round(x14+.0005,4)}, {round(y14+.0005,4)}, {0.0})'

    points = [foretop, forebot, wakebot, waketop]
    return points

def mesh_file():
    """ 
    saves the mesh in an openfoam readable format based on the example given
    """
    n, Lf,Lw, H, alpha = params()
    diamond = generate_diamond(alpha)
    single_graph = singlegraph(diamond)
    vertices = generate_other_verts(diamond, Lf,Lw, H)
    formatted_string = "   ("
    i = 0
    for row in vertices:
        formatted_string += " ".join([f"{val: .16e}" for val in row]) + f") // {i}\n   ("
        i += 1;
    formatted_string = formatted_string[:-2]  # Remove the extra "( " at the end

    contents_to_modify = {'vert_template': '  (-1.0000000000000000e+01 -5.0000000000000000e+00 -5.0000000000000003e-02) // 0', 'info': '// H = 5'}
    highres = '/Users/treygower/Desktop/blockMeshDict_highres.template'
    lowres = '/Users/treygower/Desktop/blockMeshDict.template'
    with open(highres, "r") as file:
        lines = file.readlines()
    
    meshletter = input("Enter a Letter to name the mesh with: ")
    info = f'//Data for blockMeshDict_{meshletter}:\n//Alpha = {np.rad2deg(alpha)} Deg,\n//Turn Angle = 3.433 Deg,\n//Length of Fore = {Lf}m,\n//Length of Wake = {Lw}m,\n//Height = {H}m\n'
#inserts formatted string of vertices
    for i, line in enumerate(lines):
        if contents_to_modify['vert_template'] in line:
            lines[i] = formatted_string
            break
    #inserts formatted string of vertices
    for i, line in enumerate(lines):
        if contents_to_modify['info'] in line:
            lines[i] = info
            break

    print("\n**************\n")
    print(f"Mesh blockMeshDict_{meshletter} has been generated\n")
    print("**************\n\n")
    print(f'Data for blockMeshDict_{meshletter}:\n Alpha = {np.rad2deg(alpha)} Deg, Turn Angle = 3.433 Deg, \n Length of Fore = {Lf}m,\n Length of Wake = {Lw}m,\n Height = {H}m')

    # Write the modified lines back to the file
    with open(f"/Users/treygower/Desktop/blockMeshDict_{meshletter}", "w") as file:
        file.writelines(lines)

     # Plotting vertices
    vis = np.append(vertices[12:16, :2], [[vertices[12, 0], vertices[12, 1]]], axis=0)
    plt.scatter(vis[:,0], vis[:,1])
    plt.plot(vis[:,0], vis[:,1], linestyle='-', color='red')  # Change linestyle and color as needed
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Vertices of the Diamond Shape')
    plt.grid(True)
    plt.show()

    plt.scatter(vertices[:16, 0], vertices[:16, 1])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Vertices of the Diamond/Grid')
    plt.grid(True)
    plt.show()

    for i in range(len(single_graph)):
        print(single_graph[i] + '\n')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    mesh_file()
