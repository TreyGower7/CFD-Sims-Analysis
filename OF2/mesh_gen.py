import numpy as np
import math
from collections import OrderedDict
"""
Mesh generation script for cylinder 
"""

__author__ = "Trey Gower, David Valenzano, Ty Zimmerman"

def params():
    """ 
    enter paramters for cylinder
    """
    Lw = 0
    #we will always have 64 vertices
    n = 64
    R = float(input('Enter R: ')) 
    H = int(input('Enter H: '))
    while Lw < 3*(R*2): 
        Lw = int(input('Enter Lw: ')) 
        if Lw < 3*(R*2):
            print('Lw must be 3 diameters greater')
    Lf= int(input('Enter Lf: ')) 


    arcs = n/2
    #blocks = generate_blocks(n)
    return n, Lf, Lw, R, H, arcs

def generate_blocks(n):
    """
    Generate the blocks
    """
    #Assumes each cube has 192 vertices
    blocks = []
    cubes = n+1 // 24
    for i in range(cubes):
        for j in range(8):
            for k in range(8):
                # Calculate the indices of the vertices
                v0 = i*8*8 + j*8 + k
                v1 = v0 + 1
                v2 = v0 + 8
                v3 = v2 + 1
                v4 = v0 + 8*8
                v5 = v4 + 1
                v6 = v4 + 8
                v7 = v6 + 1
                
                # Create a block using the calculated vertex indices
                block = f'hex ({v0} {v1} {v3} {v2} {v4} {v5} {v7} {v6}) (1 1 1)'
                blocks.append(block)
    return blocks

def generate_vertices(n,R,H,Lf,Lw):
    D = R*2
    # Generate vertices around the circumference of inner cylinder
    #We want 8 vertices around each block so n//8
    # Calculate angle increment
    vertices = np.zeros((n//8,3))
    angle_increment = 2 * np.pi / (n//8)
    k=0; l =0
    for i in range((n//8)):
        angle = i * angle_increment
        if i <= 8:
            for j in range(3):
                if j == 0:
                    vertices[i, j] = R* np.cos(angle)
                if j == 1:
                    vertices[i, j] = R* np.sin(angle)
                if j ==2:
                    vertices[i, j] = -.5
    vertices1 = np.zeros((n//8,3))
    for i in range(n//8): 
        angle1 = (np.pi*2) * i / (n//8) 
        vertices1[i,0] = np.cos(angle1)
        vertices1[i,1] = np.sin(angle1)
        vertices1[i,2] = -.5 
    vertices = np.concatenate((vertices, vertices1), axis=0)
    grid_start = np.array((6, 0 ,-.5))
    vertices = np.concatenate((vertices, np.zeros((n//4,3))), axis=0)
    for i in range((n//4)-1, , 1):
        #x vertices
        if i == 15 or k == 2:
            #Vertex 16 will always be this:
            vertices[i,0] = Lw 
            vertices[i, 1] = vertices[0,1]
            vertices[i, 2] = -.5
            if k == 2 and l != 4:
                l +=1
                vertices[i, 0] = vertices[i-1, 0] - (D+R+Lw)
            if l ==4:
                k = 0
        else:
        #y vertices
            if k!=2 and l==0:
                vertices[i, 0] = vertices[i-1,0]
                vertices[i, 1] = (D+R+Lw) + vertices[i-1, 1]
                vertices[i, 2] = -.5
                k += 1
            #Final few vertices for upper half of grid
            if l ==4 and k ==0:
                vertices[i, 0] = vertices[i-1,0]
                vertices[i, 1] = vertices[i-1, 1] - (D+R+Lw)
                vertices[i, 2] = -.5

    return vertices
        

def mesh_file(vertices, blocks, edges):
    """ 
    saves the mesh in an openfoam readable format based on the example given
    """
    #Modifing a specific template and saving as a new output
    contents_to_modify = {'vert_template': '// ( 1.0000000000000000e+01 -7.0710678118654746e-01  5.0000000000000003e-02) // 63',
                          'block_template': '// hex (0 8 9 1 32 40 41 33) (10 20 1) simpleGrading ( 2.00000e+00  1.00000e+00 1.0)',
                          'edge_template': '// arc 0 1 ( 4.61940e-01  1.91342e-01 -5.00000e-02)'}
    
    index = 0;
    str_ver = ''
    with open("/Users/treygower/Desktop/blockMeshDict.template", "r") as file:
        lines = file.readlines()
    for i in range(len(vertices)):
        str_ver = str_ver + str(tuple(vertices[i])) + f' // {i}\n'
    # Iterate over the lines and replace the specified line
    for i, line in enumerate(lines):
        if contents_to_modify['vert_template'] in line:
            lines[i] = str_ver
            break
    

# Write the modified lines back to the file
    with open("/Users/treygower/Desktop/blockMeshDict_updated.txt", "w") as file:
        file.writelines(lines)

    
def main():
    """ Main entry vertices  """
n, Lf, Lw, R, H, arcs = params()
vertices = generate_vertices(n,R,H,Lf,Lw)
print(len(vertices))
print(vertices)
mesh_file(vertices, H, R)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()