import numpy as np
import pandas as pd
"""
Mesh generation script for cylinder 
"""

__author__ = "Trey Gower, David Valenzano, Ty Zimmerman"

def params():
    """ 
    enter paramters for cylinder
    """
    s_pole = np.array((0,-.5)) #North pole
    n_pole = np.array((0,.5)) #North pole

    n = int(input('Enter number of vertices: ')) #enter number of vertices
    Lf = int(input('Enter Lf: ')) #enter number of vertices
    Lw = int(input('Enter Lw: ')) 
    R = int(input('Enter R: ')) 
    H = int(input('Enter H: ')) 

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

def generate_vertices(n,R,H,Lw,Lf):
    #South pole included
    vertices = []
    #[0, 0.5, -0.5]

    # Generate vertices around the circumference of inner cylinder
    #We want 8 vertices around each block so n//8
    # Calculate angle increment
    angle_increment = 2 * np.pi / (n//8)

    # Generate vertices around the circumference
    for i in range(n//8):
        angle = i * angle_increment
        x = (R/2) * np.cos(angle)
        y = (R/2) * np.sin(angle)
        z = -0.5 
        vertices.append([x, y, z])

    # Generate vertices around the circumference of outer
    for i in range(n//8):
        angle = i * angle_increment
        x = (R) * np.cos(angle)
        y = (R) * np.sin(angle)
        z = -0.5 
        vertices.append([x, y, z])

    # Add north pole vertex
    vertices.append([0, 0.5, -0.5 + H])

    return vertices
    

def mesh_file(vertices, blocks, edges):
    """ 
    saves the mesh in an openfoam readable format based on the example given
    """
    #Modifing a specific template and saving as a new output
    contents_to_modify = {'vert_template': '// ( 1.0000000000000000e+01 -7.0710678118654746e-01  5.0000000000000003e-02) // 63',
                          'block_template': '// hex (0 8 9 1 32 40 41 33) (10 20 1) simpleGrading ( 2.00000e+00  1.00000e+00 1.0)',
                          'edge_template': '// arc 0 1 ( 4.61940e-01  1.91342e-01 -5.00000e-02)'}
    
    '''Template for vertices, blocks, and edges
    new_values = {'0': '( 5.0000000000000000e-01  0.0000000000000000e+00 -5.0000000000000003e-02) // 0',
                  '1': '( 3.5355339059327379e-01  3.5355339059327373e-01 -5.0000000000000003e-02) // 1',
                  '2': '( 3.0616169978683830e-17  5.0000000000000000e-01 -5.0000000000000003e-02) // 2',
                  '3': '(-3.5355339059327373e-01  3.5355339059327379e-01 -5.0000000000000003e-02) // 3'}
    '''
    #Open the template
    with open('/home1/09043/tagower/CFD_repo/OF2/blockMeshDict.template', 'r') as f:
        content = f.read()

    # Replace old_string with new vertices, blocks, and edges
    for key, value in vertices.items():
        content = content.replace(contents_to_modify['vert_template'], value)

    for key, value in blocks.items():
        content = content.replace(contents_to_modify['block_template'], value)

    for key, value in edges.items():
        content = content.replace(contents_to_modify['edge_template'], value)

    with open('blockMeshDict_' + str(len(vertices)), 'w') as f:
        f.write(content)

    
def main():
    """ Main entry point """
n, Lf, Lw, R, H, arcs = params()
vertices = generate_vertices(n,R,H,Lw,Lf)
print(len(vertices))
print(vertices)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()