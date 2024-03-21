import numpy as np
import matplotlib.pyplot as plt
import requests 
from matplotlib.cm import get_cmap
import re
from scipy.fft import fft, ifft

"""
Module Docstring
"""

def get_U():
    u0 = []
    u1 = []
    t = []

    mesh = 'A1'
    line1 = f''
    line2 = f''
    response = requests.get(line1)
    response2 = requests.get(line2)

    if response.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
        lines1 = response.text.split('\n')  # Split the response into lines
        lines2 = response2.text.split('\n')
    else:
        print("Failed to retrieve content. Status code:", response.status_code)
    pat = r'(\d+\.\d+)\s+\(([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\)\s+\(([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\)'

# Print the first few lines as an example
    for i, line in enumerate(lines1):
        match = re.search(pat,line)
        dim = match.groups()
        if dim[0] >= 60:
            u0.append(float(dim[1]))
            t.append(float(dim[0]))

            
    for i, line in enumerate(lines2):
            match = re.search(pat,line)
            dim = match.groups()
            if dim[0] >= 60:
                u1.append(float(dim[1]))

def fast_fourier():

# example y = fft(x)
 
    return u1,v1,u2,v2,u3,v3

def plotrt(vr1,vr2,vr3,vt1,vt2,vt3):
    r = np.linspace(0,3,len(vt3))
    plt.figure(1)
    plt.plot(r,vt3, '-r',label='Probe 1')
    #plt.plot(t,u1, '-b',label='Probe 2')
    
    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.xlabel('t')
    plt.ylabel('u/U')
    plt.grid()

    plt.show()

def main():
    u1,v1,u2,v2,u3,v3 =  get_U()

    vr1,vr2,vr3,vt1,vt2,vt3 = convertrt(u1,v1,u2,v2,u3,v3)
    plotrt(vr1,vr2,vr3,vt1,vt2,vt3)
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()