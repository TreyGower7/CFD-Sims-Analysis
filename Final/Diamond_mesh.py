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
    Lw = 0
    H =0
    Lf =0
    #we will always have 32 vertices
    n = 32

    H = float(input('Enter H: '))
    L = float(input('Enter L (Length of one side of the domain): ')) 
    alpha_d = float(input('Enter angle of attack in degrees: ')) 
    alpha_r = np.deg2rad(alpha_d)
    return n, L, H, alpha_d

def generate_diamond(alpha):
    '''
    Generates diamond at various angles of attack
    '''
    #Diamond vertices
    theta = np.deg2rad(5)
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
   
def generate_other_verts(diamond, L, H):
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
    v0 = np.array((-L, -H))
    v1 = np.array((x12, -H))
    v2 = np.array((x15, -H))
    v3 = np.array((x14, -H))
    v4 = np.array((L, -H))
    v5 = np.array((L, y14))
    v6 = np.array((L, H))
    v7 = np.array((x14, H))
    v8 = np.array((x13, H))
    v9 = np.array((x12, H))
    v10 = np.array((-L, H))
    v11 = np.array((-L, y12))

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

    return vertices


def vertex_formatter(vertices):
    '''
    formats the vertices for the blockMeshDict file
    '''
    formatted_vertices = []
    for i in range(len(vertices)):
        formatted_vertices.append(f"   ( {vertices[i,0]:.16e} {vertices[i,1]:.16e} {vertices[i,2]:.16e}) // {i}")
    return formatted_vertices


def get_other_verts(diamond_vertices,lines):
    '''
    Gets other vertices based on what vertices we dont want
    '''
    # Define the regular expression pattern to match vertices
    pattern = r"\(([^)]+)\) // (\d+)"

    # Find all vertices in the text
    all_vertices = re.findall(pattern, lines)

    # Convert the diamond vertices set to a set for faster lookup
    diamond_vertices_set = set(diamond_vertices)

    # Filter out the diamond vertices
    non_diamond_vertices = [vertex for vertex in all_vertices if vertex[0] not in diamond_vertices_set]

    # Display the non-diamond vertices
    print("Non-diamond vertices:")
    for vertex in non_diamond_vertices:
        print(vertex)


def mesh_file(new_vertices):
    """ 
    saves the mesh in an openfoam readable format based on the example given
    """
 
    with open("./blockMeshDict.template", "r") as file:
        lines = file.readlines()
    
    

    meshlet = input("Enter a Letter to name the mesh with: ")
# Write the modified lines back to the file
    with open(f"./blockMeshDict_{meshlet}", "w") as file:
        file.writelines(lines)

    print("\n**************\n")
    print(f"Mesh blockMeshDict_{meshlet} has been generated\n")
    print("**************\n")

def main():
    """ Main entry vertices  """
    with open("/Users/treygower/Desktop/blockMeshDict", "r") as file:
        lines = file.readlines()

    n, L, H, alpha = params()
    diamond = generate_diamond(alpha)
    vertices = generate_other_verts(diamond, L, H)
    print(vertices)
    # Plotting vertices
    plt.scatter(vertices[:15, 0], vertices[:15, 1])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Vertices of the Diamond Shape')
    plt.grid(True)
    plt.show()
    formatted_vertices = vertex_formatter(vertices)
    print(formatted_vertices)
    #mesh_file(vertices)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
