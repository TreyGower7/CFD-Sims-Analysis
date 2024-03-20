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
    n = 64
    r = .5

    while H < (3*(r*2)): 
        H = float(input('Enter H: '))
        if H < 3*(r*2):
            print('Height boundary must be 3 diameters away')

    while Lw < (3*(r*2)): 
        Lw = float(input('Enter Lw: ')) 
        if Lw < 3*(r*2):
            print('Wake boundary must be 3 diameters away')

    while Lf < (3*(r*2)): 
        Lf= float(input('Enter Lf: ')) 
        if Lf < 3*(r*2):
            print('Fore boundary must be 3 diameters away')

    return n, Lf, Lw, r, H

def arc_adjust(lines, vertices, R):
    '''
    Function adjusts the outer radius arcs for recirculation
    '''
    '''
    #arcs = lines[94:126]
    angle = np.pi/8
    A = np.array([[np.cos(angle), -np.sin(angle)],
              [np.sin(angle), np.cos(angle)]])
    x= vertices[7:15,0]
    y=vertices[7:15,1]
    arcs = np.column_stack((x, y))
    arcpoints = np.dot(arcs,A)
    '''
    patterns = [r'arc 8 9 ', r'arc 9 10 ', r'arc 10 11 ', r'arc 11 12 ', r'arc 12 13 ', r'arc 13 14 ', r'arc 14 15 ', r'arc 15 8 ']
     # Collect replacements in a list
    formatted_arc = ''
    z_coords = []
    x_coords = []
    y_coords = []
    for i, line in enumerate(lines):
        for pattern in patterns:
            arc_pattern = re.compile(rf'{pattern}\s*\((.*?)\)')
            matches = arc_pattern.findall(line)
            for match in matches:
                x, y, z = match.split()
                x_coords.append(float(x))
                y_coords.append(float(y))
                z_coords.append(float(z))
    midp = np.zeros((len(x),2))
    #for point 15-8
    x_coords.append(float(x[0]))
    y_coords.append(float(y[0]))
    x_coords = float(x_coords)
    y_coords = float(y_coords)

    for i in range(len(x)-1):
        chord_mid = ((x_coords[i+1]+ x_coords[i])/2, (y_coords[i+1]+ y_coords[i])/2)

        direction_vector = (((x_coords[i+1] - x_coords[i])/2), 
                            (y_coords[i+1] - y_coords[i])/2)

        # Magnitude of direction vector
        direction_vector_len = np.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)

        # Normalize the direction vector
        normalized_vec = (direction_vector[0] / direction_vector_len, 
                        direction_vector[1] / direction_vector_len)

        # Calculate the midpoint of the arc
        arc_midpoint = (chord_mid[0] + normalized_vec[0] * R, 
                        chord_mid[1] + normalized_vec[1] * R)
        midp[i][0] = arc_midpoint[0]
        midp[i][1] = arc_midpoint[1]
    for j in range(len(patterns)):
        for i, line in enumerate(lines):
                match = re.search(patterns[j], line)
                if match:
                    print(midp[j,0])
                    print(midp[j,1])
                    # Replace the matched pattern with the new values
                    formatted_arc = f"{patterns[j]}({midp[j,0]: .5e} {midp[j, 1]: .5e} {float(z_coords[j]): .5e})"
                    lines[i] = formatted_arc + "\n"
                    break

    return lines
def generate_vertices(n,r,H,Lf,Lw):
   #R is outer radius
    R = input("Outer Radius: ")
    R = float(R)
    if R == "n":
        R = 2*r
    # Generate vertices around the circumference of inner cylinder
    #We want 8 vertices around each block so n//8
    z= .05
    angles = np.linspace(0, 2*np.pi, n//8, endpoint=False)
    x = r * np.cos(angles)
    y = r * np.sin(angles)
    zvec = np.zeros_like(x)  # Assuming the inner cylinder is at z = 0
    zvec[:] = -.05
    inner_vertices = np.column_stack((x, y, zvec))
    outer_vertices = inner_vertices.copy()
    outer_vertices[:, 1] = R*np.sin(angles[:])  # Offset y coordinates by y component
    outer_vertices[:, 0] = R*np.cos(angles[:])  # Offset x coordinates by x component

    vertices = np.concatenate((inner_vertices, outer_vertices), axis=0)
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
    
    return vertices, R

def grading(lines):
    """
    Serves to adjust the grading of the mesh
    """
    #preserve the template
    org_data = lines
    block = ""
    new_values = ""
    yorn = None
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
                yorn = input('would you like to change simple grading too (y/n)? ')
                
                #Adjusting simple grading
                if yorn == 'y':
                    simplegrade_pattern = r'\(\s*(\d+\.\d+e[+-]\d+)\s+(\d+\.\d+e[+-]\d+)\s+(\d+\.\d+)\s*\)'
                    # Search for the pattern in the line
                    match_simple = re.search(simplegrade_pattern, org_data[i+1])
                    simple_x = input('simple x grade (or type (s) to keep it the same): ')
                    simple_y = input('simple y grade (or type (s) to keep it the same): ')
                    dim_simple = match_simple.groups()

                    if simple_x == 's':
                        simple_x = dim_simple[0]
                    if simple_y == 's':
                        simple_y = dim_simple[1]
                    simple_newvals = f'({float(simple_x): .5e} {float(simple_y): .5e} {1.0})'
                    pat_simple = f' ( {dim_simple[0]}  {dim_simple[1]} 1.0)'
                
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
                if yorn == 'y':
                    lines[j] = re.sub(simplegrade_pattern, simple_newvals, org_data[j])
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

    #Modifing a specific template and saving as a new output
    
    contents_to_modify = {'vert_template': '   ( 7.0710678118654735e-01 -7.0710678118654768e-01 -5.0000000000000003e-02) // 15',
                          'edge_template': 'arc 0 1 ( 4.61940e-01  1.91342e-01 -5.00000e-02)'}
    
    index = 0;
    
    with open("./blockMeshDict1.template", "r") as file:
        lines = file.readlines()
    
    #inserts formatted string of vertices
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
    if R != 1:
    #Outer radius arc adjustment
        lines = arc_adjust(lines, vertices,R)
  

    meshlet = input("Enter a Letter to name the mesh with: ")
# Write the modified lines back to the file
    with open(f"./blockMeshDict_{meshlet}", "w") as file:
        file.writelines(lines)
    print("\n**************\n")
    print(f"Mesh blockMeshDict_{meshlet} has been generated\n")
    print("**************\n")

def main():
    """ Main entry vertices  """
n, Lf, Lw, r, H = params()
vertices, R = generate_vertices(n,r,H,Lf,Lw)
mesh_file(vertices,R)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
