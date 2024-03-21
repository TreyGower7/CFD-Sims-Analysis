import numpy as np
import matplotlib.pyplot as plt
import requests 
from matplotlib.cm import get_cmap
import re

"""
plotting u vs v for x =.5 and y = [0:1]
"""

__author__ = "Trey Gower, David Valenzano, Ty Zimmerman"

def get_data():
    """ Get Data from Github
     
     Args:

     Returns: 
    
    """
    ind=20;
    t = []
    u0 = []
    v0 = [] 
    u1 = []
    v1 = [] 
    p0 = []
    p1 = []
    tp = []

    url = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/probespart6/0/U"
    url2 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/probespart6/0/p"

    response = requests.get(url)
    response2 = requests.get(url2)
    if response.status_code == 200 and response2.status_code == 200:
        lines = response.text.split('\n')  # Split the response into lines
        lines2 = response2.text.split('\n')
    else:
        print("Failed to retrieve content. Status code:", response.status_code)
    pat = r'(\d+\.\d+)\s+\(([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\)\s+\(([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\)'
    pat2 = r'(\S+)\s+(\S+)\s+(\S+)'
# Print the first few lines as an example
    for i, line in enumerate(lines[4:]):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            t.append(float(dim[0]))
            u0.append(float(dim[1]))
            v0.append(float(dim[2]))
            u1.append(float(dim[4]))
            v1.append(float(dim[5]))

    for i, line in enumerate(lines2[4:]):
        match = re.search(pat2,line)
        if match:
            dim = match.groups()
            p0.append(float(dim[1]))
            p1.append(float(dim[2]))
            tp.append(float(dim[0]))
 
    return t,u0,v0,u1,v1,p0,p1,tp


def plot(t,u0,v0,u1,v1,p0,p1,tp):
    
   
    plt.figure(1)
    plt.plot(t,u0, '-r',label='Probe 1')
    plt.plot(t,u1, '-b',label='Probe 2')

    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.xlabel('t')
    plt.ylabel('u/U')
    plt.grid()

    plt.show()

    plt.figure(2)
    plt.plot(t,v0, '-r',label='Probe 1')
    plt.plot(t,v1, '-b',label='Probe 2')

    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.xlabel('t')
    plt.ylabel('v/U')
    plt.grid()

    plt.show()

    plt.figure(3)
    plt.plot(tp,p0, '-r',label='Probe 1')
    plt.plot(tp,p1, '-b',label='Probe 2')

    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.xlabel('t')
    plt.ylabel('p/U')
    plt.grid()
    plt.xlim([0,100])
    plt.show()





def main():
    """ Main entry point of the app """
    t,u0,v0,u1,v1,p0,p1,tp= get_data()
   
    plot(t,u0,v0,u1,v1,p0,p1,tp)
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
