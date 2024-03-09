import re
import numpy as np

def params():
    """ 
    enter paramters for cylinder
    """
    Lw = 0
    #we will always have 64 vertices
    n = 64
    R = float(input('Enter Radius: '))
    H = float(input('Enter H: '))
    while Lw < (3*(R*2)): 
        Lw = float(input('Enter Lw: ')) 
        if Lw < (3*(R*2)):
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
def arc_adjust(lines, vertices,R):
    """
    Adjust arc midpoints based on radius
    """
    arcs = lines[94:126]
    midpoints = np.zeros((len(arcs),3))
    heads = []
    zpat = r'-?5\.00000e-02'
    # Extract the z-coordinate from each match since these dont change
    z_coords = []
    for string in arcs:
        match = re.search(zpat, string)
        if match:
            z_coords.append(float(match.group()))

    for i in range(len(arcs)):
        pattern = r'arc (\d+) (\d+)'
        match = re.search(pattern, arcs[i])
        if match:
            arc = [match.group(0),int(match.group(1)),int(match.group(2))]
            heads.append(arc[0])
            chord_mid = ((vertices[arc[2]][0]+ vertices[arc[1]][0])/2, 
                        (vertices[arc[2]][1]+ vertices[arc[1]][1])/2)
            direction_vector = (((vertices[arc[2]][0] - vertices[arc[1]][0])/2), 
                                (vertices[arc[2]][1] - vertices[arc[1]][1])/2)
        
            # Magnitude of direction vector
            direction_vector_len = np.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)
            
            # Normalize the direction vector
            normalized_vec = (direction_vector[0] / direction_vector_len, 
                            direction_vector[1] / direction_vector_len)
            
            # Calculate the midpoint of the arc
            arc_midpoint = (chord_mid[0] + normalized_vec[0] * R, 
                            chord_mid[1] + normalized_vec[1] * R)
            midpoints[i][0] = arc_midpoint[0]
            midpoints[i][1] = arc_midpoint[1]
            midpoints[i][2] = 0.05
    #Formating
    formatted_arcs = ''
    for row in range(len(midpoints)):
        formatted_arc = f"{heads[row]} ( {midpoints[row][0]: .5e}  {midpoints[row][1]: .5e} {z_coords[row]: .5e})\n"
        formatted_arcs += formatted_arc    
    return formatted_arcs
        
with open("/Users/treygower/Desktop/blockMeshDict1.example", "r") as file:
    lines = file.readlines()
n, Lf, Lw, R, H, arcs = params()
vertices = generate_vertices(n,R,H,Lf,Lw)
print(arc_adjust(lines, vertices, R))
#with open("/Users/treygower/Desktop/blockMeshDict123_updated.txt", "w") as file:
#        file.write()
