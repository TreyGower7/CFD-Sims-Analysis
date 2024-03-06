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
    vertices = np.concatenate((vertices, np.zeros((n//4,3))), axis=0)
    #Manually entering the first quadrant
    #point 16
    vertices[16,0] = Lw 
    vertices[16, 1] = vertices[0,1]
    vertices[16, 2] = -.5  
    #point 17
    vertices[17,0] = Lw
    vertices[17, 1] = vertices[9,1]
    vertices[17, 2] = -.5  
    #point 19
    vertices[19,0] = vertices[9,0]
    vertices[19, 1] = H
    vertices[19, 2] = -.5  
    #point 18
    vertices[18,0] =  vertices[17, 0]
    vertices[18, 1] = H
    vertices[18, 2] = -.5  
    #point 20
    vertices[20,0] = 0
    vertices[20, 1] = H
    vertices[20, 2] = -.5  
    
    #point 21
    vertices[21,0] = -vertices[11,1] 
    vertices[21, 1] = H
    vertices[21, 2] = -.5  
    #point 22
    vertices[22,0] = -Lf
    vertices[22, 1] = H
    vertices[22, 2] = -.5  
    #point 23
    vertices[23,0] = -Lf
    vertices[23, 1] = vertices[11,1] 
    vertices[23, 2] = -.5  
    #point 24
    vertices[24,0] =  -Lf
    vertices[24, 1] = 0
    vertices[24, 2] = -.5  
    j=1
    for i in range(25, 32, 1):
        vertices[i,0] = vertices[i-(2*j),0]
        vertices[i,1] = -vertices[i-(2*j),1]
        vertices[i,2] = -.5
        j +=1;
    vertices = np.concatenate((vertices, vertices), axis=0)
    vertices[32:, 2] = -vertices[32:,2]

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