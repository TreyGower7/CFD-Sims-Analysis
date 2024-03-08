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
    #we will always have 64 vertices
    n = 64
    R = float(input('Enter Radius: '))
    H = float(input('Enter H: '))
    while Lw < (3*(R*2))+1: 
        Lw = float(input('Enter Lw: ')) 
        if Lw < 3*(R*2):
            print('Lw must be 3 diameters greater')
    Lf= float(input('Enter Lf: ')) 


    arcs = n/2
    return n, Lf, Lw, R, H, arcs

def generate_vertices(n,R,H,Lf,Lw):
    D = R*2
    # Generate vertices around the circumference of inner cylinder
    #We want 8 vertices around each block so n//8
    # Calculate angle increment
    vertices = np.zeros((n//8,3))
    angle_increment = 2 * np.pi / (n//8)
    z= .05
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
                    vertices[i, j] = -z
    vertices1 = np.zeros((n//8,3))
    for i in range(n//8): 
        angle1 = (np.pi*2) * i / (n//8) 
        vertices1[i,0] = np.cos(angle1)
        vertices1[i,1] = np.sin(angle1)
        vertices1[i,2] = -z
    vertices = np.concatenate((vertices, vertices1), axis=0)
    vertices = np.concatenate((vertices, np.zeros((n//4,3))), axis=0)
    #Manually entering the first quadrant
    #point 16
    vertices[16,0] = Lw 
    vertices[16, 1] = vertices[0,1]
    vertices[16, 2] = -z 
    #point 17
    vertices[17,0] = Lw
    vertices[17, 1] = vertices[9,1]
    vertices[17, 2] = -z  
    #point 19
    vertices[19,0] = vertices[9,0]
    vertices[19, 1] = H
    vertices[19, 2] = -z 
    #point 18
    vertices[18,0] =  vertices[17, 0]
    vertices[18, 1] = H
    vertices[18, 2] = -z  
    #point 20
    vertices[20,0] = 0
    vertices[20, 1] = H
    vertices[20, 2] = -z  
    
    #point 21
    vertices[21,0] = -vertices[11,1] 
    vertices[21, 1] = H
    vertices[21, 2] = -z 
    #point 22
    vertices[22,0] = -Lf
    vertices[22, 1] = H
    vertices[22, 2] = -z  
    #point 23
    vertices[23,0] = -Lf
    vertices[23, 1] = vertices[11,1] 
    vertices[23, 2] = -z  
    #point 24
    vertices[24,0] =  -Lf
    vertices[24, 1] = 0
    vertices[24, 2] = -z  
    j=1
    for i in range(25, 32, 1):
        vertices[i,0] = vertices[i-(2*j),0]
        vertices[i,1] = -vertices[i-(2*j),1]
        vertices[i,2] = -z
        j +=1;
    vertices = np.concatenate((vertices, vertices), axis=0)
    vertices[32:, 2] = -vertices[32:,2]

    return vertices
def arc_adjust(lines, vertices):
    """
    Adjust arc midpoints based on radius
    """
    arcs = lines[94:126]

    for i in range(len(arcs)):
        pattern = r'arc (\d+) (\d+)'
        match = re.search(pattern, arcs[i])
        arc = [match.group(0),int(match.group(1)),int(match.group(2))]
        #Calculate midpoints
        quadrant = 
        mid_x = (np.sqrt(r))
        vertices[]

def grading(lines):
    """
    Serves to adjust the grading of the mesh
    """
    #preserve the template
    org_data = lines
    block = ""
    new_values = ""
    while block != 'done' and block != 'd':
        block = ""
        while not block.isdigit() or int(block) >= 20:
            block = input("Input the block to change grading of: ")
            if block == 'done' or block == 'd':
                break

            if not block.isdigit() or int(block) >= 20:
                print("Invalid block number. Please enter an integer less than 20.")
                continue
        if block == 'done' or block == 'd':
            break


        #Finds Pattern for a given block
        for i in range(len(org_data)):
            if f'   // block {block}\n' == org_data[i]:
                print('Current Block org_data:\n' + lines[i+1])
                print(f'Enter desired grading along x or y for block {block}')
                x = input('x grade: ')
                y = input('y grade: ')
                new_values = f'{x} {y} {1}'
                grade_pattern = r'\(\s*(\d+)\s+(\d+)\s+(\d+)\s*\)'
                # Search for the pattern in the line
                match = re.search(grade_pattern, org_data[i+1])
                dim = match.groups()
                pat = f'({dim[0]} {dim[1]} 1)'
                break
        # Go through the file again and replace all matching patterns
        print('Grading Selected and Bordering Blocks:')
        for j in range(len(org_data)):
            if re.search(pat, org_data[j]):
                # Attempt to identify the block number for reporting
                if j > 0 and 'block' in org_data[j-1]:
                    print(org_data[j-1].strip()[3:])
            lines[j] = re.sub(pat, new_values, org_data[j])
    return lines

def mesh_file(vertices, R):
    """ 
    saves the mesh in an openfoam readable format based on the example given
    """
    formatted_string = "   ("
    i = 0
    for row in vertices:
        formatted_string += " ".join([f"{val: .16e}" for val in row]) + f") // {i}\n   ("
        i += 1;
    formatted_string = formatted_string[:-2]  # Remove the extra "( " at the end

    print(formatted_string)
    #Modifing a specific template and saving as a new output
    
    contents_to_modify = {'vert_template': '   ( 7.0710678118654735e-01 -7.0710678118654768e-01 -5.0000000000000003e-02) // 15',
                          'block_template': '// hex (0 8 9 1 32 40 41 33) (10 20 1) simpleGrading ( 2.00000e+00  1.00000e+00 1.0)',
                          'edge_template': '// arc 0 1 ( 4.61940e-01  1.91342e-01 -5.00000e-02)'}
    
    index = 0;
    
    with open("./blockMeshDict1.example", "r") as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        if contents_to_modify['vert_template'] in line:
            lines[i] = formatted_string
            break
    #Adjust grading
    yorn = None
    while yorn != 'y' or yorn != 'n':
        yorn = input('Would you like to change Resolution? (y/n): ')
        if yorn == 'y':
            lines = grading(lines)
            break
        if yorn == 'n':
            break
        else: 
            print('enter y or n')
    #Arc adujstment based on radius
    if R != .5:
        arc_adjust(lines, vertices)

# Write the modified lines back to the file
    with open("./blockMeshDict", "w") as file:
        file.writelines(lines)

    
def main():
    """ Main entry vertices  """
n, Lf, Lw, R, H, arcs = params()
vertices = generate_vertices(n,R,H,Lf,Lw)
mesh_file(vertices,R)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
