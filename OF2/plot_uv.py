import numpy as np
import matplotlib.pyplot as plt
import requests 
from matplotlib.cm import get_cmap
import re
from PIL import Image

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
    url = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/probes110part6/0/U"
    url2 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/probes110part6/0/p"

    response = requests.get(url)
    response2 = requests.get(url2)
    if response.status_code == 200 and response2.status_code == 200:
        lines = response.text.split('\n')  # Split the response into lines
        lines2 = response2.text.split('\n')
    else:
        print("Failed to retrieve content. Status code:", response.status_code)
    pat = r'(\d+\.\d+)\s+\(([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\)\s+\(([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\)'
# Print the first few lines as an example
    for i, line in enumerate(lines[4:]):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            #print(dim[0])
            t.append(float(dim[0]))
            u0.append(float(dim[1]))
            v0.append(float(dim[2]))
            u1.append(float(dim[4]))
            v1.append(float(dim[5]))
        if i > 4:
            p0.append(float(lines2[i][15:27].strip()))
            p1.append(float(lines2[i][30:-1].strip()))
    return t,u0,v0,u1,v1,p0,p1


def plot(t,u0,v0,u1,v1,p0,p1):
    
    f_u = u0[::800]
    f_t = t[::800]
    print(len(f_u))
    print(len(f_t))
    plt.plot(f_t,f_u, '-r',label=u0)
    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.title('v vs y refined, RE=10')
    plt.xlabel('y')
    plt.ylabel('v')
    plt.grid()
    plt.gcf().set_size_inches(8, 6)  # Set width and height in inches as required

    plt.show()



def main():
    """ Main entry point of the app """
    t,u0,v0,u1,v1,p0,p1 = get_data()
    plot(t,u0,v0,u1,v1,p0,p1)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
