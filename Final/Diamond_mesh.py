import numpy as np
import re
import matplotlib.pyplot as plt

"""
Mesh generation script for cylinder 
"""

__author__ = "Trey Gower, David Valenzano, Ty Zimmerman"


def params():
    """ 
    enter paramters 
    """
    Lf = 2
    Lw = 6
    H = 5
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
        A = np.array((np.cos(alpha), np.sin(alpha)),(-np.sin(alpha), np.cos(alpha)))
        #A = np.array((np.cos(alpha), -np.sin(alpha)), (np.sin(alpha), np.cos(alpha)))

        v12 = A*v12
        v13 = A*v13
        v14 = A*v14
        v15 = A*v15

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



def mesh_file():
    """ 
    saves the mesh in an openfoam readable format based on the example given
    """
    n, Lf,Lw, H, alpha = params()
    diamond = generate_diamond(alpha)
    vertices = generate_other_verts(diamond, Lf,Lw, H)
    formatted_string = "   ("
    i = 0
    for row in vertices:
        formatted_string += " ".join([f"{val: .16e}" for val in row]) + f") // {i}\n   ("
        i += 1;
    formatted_string = formatted_string[:-2]  # Remove the extra "( " at the end

    contents_to_modify = {'vert_template': '  (-1.0000000000000000e+01 -5.0000000000000000e+00 -5.0000000000000003e-02) // 0', 'info': '// H = 5'}

    with open("/Users/treygower/Desktop/blockMeshDict.template", "r") as file:
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
    plt.scatter(vertices[12:16, 0], vertices[12:16, 1])
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


if __name__ == "__main__":
    """ This is executed when run from the command line """
    mesh_file()
