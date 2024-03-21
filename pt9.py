import numpy as np
import matplotlib.pyplot as plt
import requests 
from matplotlib.cm import get_cmap
import re
"""
Module Docstring
"""

def get_U():
    u1 = []
    v1 = []
    u2 = []
    v2 = []
    u3 = []
    v3 = []
    mesh = 'A1'
    line1 = f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/mesh{mesh}/30/line1_U.xy'
    line2 = f"https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/mesh{mesh}/30/line2_U.xy"
    line3 = f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/mesh{mesh}/30/line3_U.xy'
    response = requests.get(line1)
    response2 = requests.get(line2)
    response3 = requests.get(line3)

    if response.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
        lines1 = response.text.split('\n')  # Split the response into lines
        lines2 = response2.text.split('\n')
        lines3 = response2.text.split('\n')
    else:
        print("Failed to retrieve content. Status code:", response.status_code)

    pat = r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

# Print the first few lines as an example
    for i, line in enumerate(lines1):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            u1.append(float(dim[3]))
            v1.append(float(dim[4]))
            

    for i, line in enumerate(lines2):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            u2.append(float(dim[3]))
            v2.append(float(dim[4]))

    for i, line in enumerate(lines3):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            u3.append(float(dim[3]))
            v3.append(float(dim[4]))
 
 
    return u1,v1,u2,v2,u3,v3

def convertrt(u1,v1,u2,v2,u3,v3):
    '''
    Convert to radial and tangential
    '''
    VR = []
    VT = []
    vr1 = np.zeros((len(u1),3))
    vr2 = np.zeros((len(u2),3))
    vr3 = np.zeros((len(u3),3))
    vt1 = np.zeros((len(u1),3))
    vt2 = np.zeros((len(u2),3))
    vt3 = np.zeros((len(u3),3))
    theta = [np.pi/4, np.pi/2, 3*(np.pi)/4]

    for j in range(len(theta)):
        for i in range(len(u1)):
            vr1[i,j] = u1[i]* np.cos(theta[j]) + v1[i] * np.sin(theta[j])
            
            # Calculate tangential velocity
            vt1[i,j] = -u1[i] * np.sin(theta[j]) + v1[i] * np.cos(theta[j])

        for i in range(len(u2)):
            vr2[i,j] = u2[i]* np.cos(theta[j]) + v2[i] * np.sin(theta[j])
            
            # Calculate tangential velocity
            vt2[i,j] = -u2[i] * np.sin(theta[j]) + v2[i] * np.cos(theta[j])

        for i in range(len(u3)):
            vr3[i,j] = u3[i]* np.cos(theta[j]) + v3[i] * np.sin(theta[j])
            
            # Calculate tangential velocity
            vt3[i,j] = -u3[i] * np.sin(theta[j]) + v3[i] * np.cos(theta[j])
        
    return vr1,vr2,vr3,vt1,vt2,vt3

def vel_bound():
    """ {Main Description here}
     
     Args:

     Returns: 
    
    """
def seperation_L():
    """ {Main Description here}
     
     Args:

     Returns: 
    
    """

def rate_of_strain():
    """ {Main Description here}
     
     Args:

     Returns: 
    
    """

def main():
    u1,v1,u2,v2,u3,v3 =  get_U()

    vr1,vr2,vr3,vt1,vt2,vt3 = convertrt(u1,v1,u2,v2,u3,v3)

    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()