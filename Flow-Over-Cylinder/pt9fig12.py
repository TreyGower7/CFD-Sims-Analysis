import numpy as np
import matplotlib.pyplot as plt
import requests 
from matplotlib.cm import get_cmap
import re
"""
Module Docstring
"""
def get_U(mesh):
    u1 = [] #pi/4
    v1 = []
    u2 = [] #pi/2
    v2 = []
    u3 = [] #3pi/4
    v3 = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    line1 = f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/mesh{mesh}/30/line1_U.xy' #pi/4
    line2 = f"https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/mesh{mesh}/30/line2_U.xy" #pi/2
    line3 = f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/mesh{mesh}/30/line3_U.xy' #3pi/4
    response1 = requests.get(line1)
    response2 = requests.get(line2)
    response3 = requests.get(line3)

    if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
        lines1 = response1.text.split('\n')  # Split the response into lines
        lines2 = response2.text.split('\n')
        lines3 = response3.text.split('\n')
    else:
        print(f"Failed to retrieve content for mesh {mesh}. Status codes:", response1.status_code, response2.status_code, response3.status_code)


    pat = r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

# Print the first few lines as an example
    for i, line in enumerate(lines1):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            x1.append(float(dim[0]))
            y1.append(float(dim[1]))
            u1.append(float(dim[3]))
            v1.append(float(dim[4]))
            

    for i, line in enumerate(lines2):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            x2.append(float(dim[0]))
            y2.append(float(dim[1]))
            u2.append(float(dim[3]))
            v2.append(float(dim[4]))

    for i, line in enumerate(lines3):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            u3.append(float(dim[3]))
            v3.append(float(dim[4]))
            x3.append(float(dim[0]))
            y3.append(float(dim[1]))
 
 
    return u1,v1,u2,v2,u3,v3,x1,y1,x2,y2,x3,y3

def convertrt(u1,v1,u2,v2,u3,v3,x1,y1,x2,y2,x3,y3):
    '''
    Convert to radial and tangential
    '''
    r1 = np.zeros((len(u1),1))
    r2 = np.zeros((len(u2),1))
    r3 = np.zeros((len(u3),1))

    VR = []
    VT = []
    vr1 = np.zeros((len(u1),1))
    vr2 = np.zeros((len(u2),1))
    vr3 = np.zeros((len(u3),1))
    vt1 = np.zeros((len(u1),1))
    vt2 = np.zeros((len(u2),1))
    vt3 = np.zeros((len(u3),1))

    #pi/4
    for i in range(len(u1)):
        r1[i] = np.sqrt(x1[i]**2+y1[i]**2)
        eix = x1[i]/ r1[i]
        eiy = y1[i]/r1[i]
        vr1[i] = u1[i]*eix + v1[i]*eiy 
        # Calculate tangential velocity
        vt1[i] = u1[i]*eiy - v1[i]*eiy
    #pi/2
    for i in range(len(u2)):
        r2[i] = np.sqrt(x2[i]**2+y2[i]**2)
        eix = x2[i]/ r2[i]
        eiy = y2[i]/r2[i]
        vr2[i] = u2[i]*eix + v2[i]*eiy 
        # Calculate tangential velocity
        vt2[i] = u2[i]*eiy - v2[i]*eiy
    #3pi/4
    for i in range(len(u3)):
        r3[i] = np.sqrt(x3[i]**2+y3[i]**2)
        eix = x3[i]/ r3[i]
        eiy = y3[i]/r3[i]
        vr3[i] = u3[i]*eix + v3[i]*eiy 
        # Calculate tangential velocity
        vt3[i] = u3[i]*eiy - v3[i]*eiy
    return vr1,vr2,vr3,vt1,vt2,vt3,r1,r2,r3

def plotrt(vr1,vr2,vr3,vt1,vt2,vt3,r1,r2,r3):
    
    plt.figure(1)
    plt.plot(r1,vr1, '-b',label='pi/4')
    plt.plot(r2,vr2, '-r',label='pi/2')
    plt.plot(r3,-vr3, '-g',label='3pi/4')
    
    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.xlabel('r')
    plt.ylabel('Ur')
    plt.grid()

    plt.show()
    plt.figure(2)
    plt.plot(r1,-vt1, '-b',label='pi/4')
    plt.plot(r2,-vt2, '-r',label='pi/2')
    plt.plot(r3,-vt3, '--g',label='3pi/4')
    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.xlabel('r')
    plt.ylabel(r'$U_{\theta}$')
    plt.grid()

def plot2(delta,utp,urp):
    A1r = [.055, .493, -.226]
    A2r = [-0.15787602, 0.41296502, -0.16492854]
    A3r = [-0.13412008,0.35046986,-0.13064792]
    A1t = [-0.02995898, -0.0275007, -3.0771246]
    A2t = [-0.12366519, 0.36334835, -3.10590308]
    A3t = [-0.10525394, 0.62316254, -3.12113156]
    Api2r = [A1r[0], A2r[0], A3r[0]]
    Api4r = [A1r[1], A2r[1], A3r[1]]
    A3pi4r = [A1r[2], A2r[2], A3r[2]]

    Api2t = [A1t[0], A2t[0], A3t[0]]
    Api4t = [A1t[1], A2t[1], A3t[1]]
    A3pi4t = [A1t[2], A2t[2], A3t[2]]

    plt.figure(0)
    plt.plot(delta[:,0],utp[:,0], '-b',label='pi/4')
    plt.plot(delta[:,1],utp[:,1], '-r',label='pi/2')
    plt.plot(delta[:,2],utp[:,2], '-g',label='3pi/4')
    
    plt.legend()  # Specify loc directly as a keyword argument
    plt.xlabel(r'$\delta$')
    plt.ylabel(r'$e_{r\theta}$')
    plt.grid()
    
    plt.figure(1)
    plt.plot(1/delta[:,0],Api4r, '-b',label='pi/4')
    plt.plot(1/delta[:,1],Api2r, '-r',label='pi/2')
    plt.plot(1/delta[:,2],A3pi4r, '-g',label='3pi/4')
    
    plt.legend()  # Specify loc directly as a keyword argument
    plt.xlabel(r'$\frac{1}{\delta}$')
    plt.ylabel(r'$e_{r\theta}$')
    plt.grid()

    plt.figure(2)
    plt.plot(1/delta[:,0],urp[:,0], '-b',label='pi/4')
    plt.plot(1/delta[:,1],urp[:,1], '-r',label='pi/2')
    plt.plot(1/delta[:,2],urp[:,2], '-g',label='3pi/4')
    
    plt.legend()  # Specify loc directly as a keyword argument
    plt.xlabel(r'$\frac{1}{\delta}$')
    plt.ylabel(r'$e_{rr}$')
    plt.grid()


def rate_of_strain(ur1,ur2,ur3,ut1,ut2,ut3,x1,y1,x2,y2,x3,y3,r1,r2,r3):
    xc1= .5*np.cos(np.pi/4)
    yc1 =.5*np.sin(np.pi/4)
    xc2= .5*np.cos(np.pi/2)
    yc2 =.5*np.sin(np.pi/2)
    xc3= .5*np.cos(3*np.pi/4)
    yc3 =.5*np.sin(3*np.pi/4)

    # defining h values
    h1 = np.sqrt((x1[1] - xc1)**2 + (y1[1] - yc1)**2)
    h2 = np.sqrt((x2[1] - xc2)**2 + (y2[1] - yc2)**2)
    h3 = np.sqrt((x3[1] - xc3)**2 + (y3[1] - yc3)**2)
    # i values
    i1 = np.sqrt((x1[2] - x1[1])**2 + (y1[2] - y1[1])**2)/h1
    i2 = np.sqrt((x2[2] - x2[1])**2 + (y2[2] - y2[1])**2)/h2
    i3 = np.sqrt((x3[2] - x3[1])**2 + (y3[2] - y3[1])**2)/h3
    # j values
    j1 = np.sqrt((x1[3] - x1[2])**2 + (y1[3] - y1[2])**2)/h1
    j2 = np.sqrt((x2[3] - x2[2])**2 + (y2[3] - y2[2])**2)/h2
    j3 = np.sqrt((x3[3] - x3[2])**2 + (y3[3] - y3[2])**2)/h3

    u = np.array([0,1,0,0])
    A1 = np.array([[1,1,1,1], [0,1,i1 + j1,1+i1+j1], [0,1,(i1+j1)**2,(1+i1+j1)**2], [0,1,(i1+j1)**3,(1+i1+j1)**3]])
    A2 = np.array([[1,1,1,1], [0,1,i2 + j2,1+i2+j2], [0,1,(i2+j2)**2,(1+i2+j2)**2], [0,1,(i2+j2)**3,(1+i2+j2)**3]])
    A3 = np.array([[1,1,1,1], [0,1,i3 + j3,1+i3+j3], [0,1,(i3+j3)**2,(1+i3+j3)**2], [0,1,(i3+j3)**3,(1+i3+j3)**3]])

    c1 = np.linalg.solve(A1, u)
    c2 = np.linalg.solve(A2, u)
    c3 = np.linalg.solve(A3, u)
    
    urprime1 = (c1[1]*ur1[1] + c1[2]*ur1[2] + c1[3]*ur1[3])/h1
    urprime2 = (c2[1]*ur2[1] + c2[2]*ur2[2] + c2[3]*ur2[3])/h2
    urprime3 = (c3[1]*ur3[1] + c3[2]*ur3[2] + c3[3]*ur3[3])/h3

    utprime1 = (c1[1]*(ut1[1]/r1[1]) + c1[2]*(ut1[2]/r1[2]) + c1[3]*(ut1[3]/r1[3]))/h1
    utprime2 = (c2[1]*(ut2[1]/r2[1]) + c2[2]*(ut2[2]/r2[2]) + c2[3]*(ut2[3]/r2[3]))/h2
    utprime3 = (c3[1]*(ut3[1]/r3[1]) + c3[2]*(ut3[2]/r3[2]) + c3[3]*(ut3[3]/r3[3]))/h3

    delta = np.array([[np.sqrt(i1*(h1**2))], [np.sqrt(i2*(h2**2))], [np.sqrt(i3*(h3**2))]])
    urp = np.array([[urprime1], [urprime2], [urprime3]])
    utp = np.array([[.25*utprime1], [.25*utprime2], [.25*utprime3]]) 
    return delta, utp, urp



def main():
    deltav = np.zeros((3,3))
    utpv = np.zeros((3,3))
    urpv = np.zeros((3,3))
    meshes = ['A1', 'A2', 'A3']  
    for i in range(len(meshes)):
        u1, v1, u2, v2, u3, v3, x1, y1, x2, y2, x3, y3 = get_U(meshes[i])

        vr1,vr2,vr3,vt1,vt2,vt3,r1,r2,r3 = convertrt(u1,v1,u2,v2,u3,v3,x1,y1,x2,y2,x3,y3)
        #plotrt(vr1,vr2,vr3,vt1,vt2,vt3,r1,r2,r3)

        delta,utp,urp = rate_of_strain(vr1,vr2,vr3,vt1,vt2,vt3,x1,y1,x2,y2,x3,y3,r1,r2,r3)
        for k in range(len(meshes)):
            deltav[i,k] = delta[k]
            utpv[i,k] = utp[k]
            urpv[i,k] = urp[k]
    print(deltav)
    plot2(deltav, utpv, urpv)
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()