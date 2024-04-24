import numpy as np
import re
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
    H =0
    Lf =0
    #we will always have 64 vertices
    n = 32

    H = float(input('Enter H: '))
    Lw = float(input('Enter Lw: ')) 
    Lf= float(input('Enter Lf: ')) 

    return n, Lf, Lw, H
def generate_diamond(lines):
    '''
    Generates diamond at various angles of attack
    '''
    #Diamond vertices
    diamond_template = {
   '(-5.0000000000000000e-01  0.0000000000000000e+00 -5.0000000000000003e-02) // 12',
   '( 0.0000000000000000e+00  4.3744331762962000e-02 -5.0000000000000003e-02) // 13',
   '( 5.0000000000000000e-01  0.0000000000000000e+00 -5.0000000000000003e-02) // 14',
   '( 0.0000000000000000e+00 -4.3744331762962000e-02 -5.0000000000000003e-02) // 15'
    };
    get_other_verts(diamond_template,lines)
    
    
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

'''
def mesh_file(vertices):
    """ 
    saves the mesh in an openfoam readable format based on the example given
    """
    formatted_string = "   ("
    i = 0
    for row in vertices:
        formatted_string += " ".join([f"{val: .16e}" for val in row]) + f") // {i}\n   ("
        i += 1;
    formatted_string = formatted_string[:-2]  # Remove the extra "( " at the end

    #Modifing a specific template and saving as a new output
    
    index = 0;
    
    with open("./blockMeshDict.template", "r") as file:
        lines = file.readlines()

    new_diamond = generate_diamond()
    new_vertices = get_other_verts(new_diamond)

    
    meshlet = input("Enter a Letter to name the mesh with: ")
# Write the modified lines back to the file
    with open(f"./blockMeshDict_{meshlet}", "w") as file:
        file.writelines(lines)
    print("\n**************\n")
    print(f"Mesh blockMeshDict_{meshlet} has been generated\n")
    print("**************\n")
'''
def main():
    """ Main entry vertices  """
    with open("/Users/treygower/Desktop/blockMeshDict", "r") as file:
        lines = file.readlines()

    n, Lf, Lw, H = params()
    generate_diamond(lines)
    #mesh_file(vertices)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
