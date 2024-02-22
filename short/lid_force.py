import numpy as np
import matplotlib.pyplot as plt
import requests 
from matplotlib.cm import get_cmap

"""
plotting u vs v for x =.5 and y = [0:1]
"""

__author__ = "Trey Gower, David Valenzano, Ty Zimmerman"

def get_data():
    """ Get Data from Github
     
     Args:

     Returns: 
    
    """
    Re=10;
    uvec = []
    vvec = []
    xvec = []
    yvec = []

    url_l1 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/short/RE" + str(Re) + "/line1_U.xy"
    url_l2 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/short/RE" + str(Re) + "/line2_U.xy"
    url_l3 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/short/RE" + str(Re) + "/line3_U.xy"
    urls = [url_l1,url_l2,url_l3]
    data = []

    for i in range(3):
        response = requests.get(urls[i])

        if response.status_code == 200:                    
            # Split the response into lines
            data.append(response.text.split('\n')) 
        else:
            print("Failed to retrieve content. Status code:", response.status_code)
    for k in range(3):
        u = np.zeros([len(data[0]),1])
        v = np.zeros([len(data[0]),1])
        x = np.zeros([len(data[0]),1])
        for i in range(len(data[0])-1):
            u[i] = float((data[k][i].split())[3])
            v[i] = float((data[k][i].split())[4])
            x[i] = float((data[k][i].split())[0])
        #Weird but okay getting rid of random zero
        u = u[:-1]
        v = v[:-1]
        x = x[:-1]
        uvec.append(u)
        vvec.append(v)
        xvec.append(x)
        #Weird but okay getting rid of random zero
    #index to next grid size
    return uvec,vvec,xvec

def evaluate_F(u):
    """
    Evaluates the one sided finite difference to approximate partial(u)/partial(y)
    """
    u_prime = np.zeros([len(u[0]),1])
    A = -46/15
    B = 15/4
    C = -5/6
    D = 3/20
    u1 = 1
    for i in range(len(u[0])):
        u_prime[i] = (A*u1)+(B*u[0][i]) + (C*u[1][i]) + (D*u[2][i])

    u_prime = u_prime
    F = sum(u_prime)
    return F

def main():
    """ Main entry point of the app """
    u,v,x = get_data()
    F = evaluate_F(u)
    print(F)
    #plot_F_RE(u,v,y)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
