import numpy as np
import matplotlib.pyplot as plt
import requests 
from matplotlib.cm import get_cmap

"""
plotting u vs v for x =.5 and y = [0:1]
"""

__author__ = "Trey Gower, David Valenzano, Ty Zimmerman"

def get_data(urls):
    """ Get Data from Github
     
     Args:

     Returns: 
    
    """
    uvec = []
    vvec = []
    xvec = []
    yvec = []
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
    return F, u_prime

def plot(tao,x):
    """Plotting for u vs v with x=.5
    """
    cmap = get_cmap('gist_rainbow')
    for i in range(3):
        color = cmap(i / 3)
        plt.plot(x[i][i], tao[i], label=('tao'  + str(i+1)),color=color)
    
    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.title('tao vs x')
    plt.xlabel('x')
    plt.ylabel('tao')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    """ Main entry point of the app """
    Re = [10,100,250,500]
    F = np.zeros([4,1])
    tao = []
    x = []
    for i in range(4):
        url_l1 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt2/RE" + str(Re[i]) + "/line1_U.xy"
        url_l2 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt2/RE" + str(Re[i]) + "/line2_U.xy"
        url_l3 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt2/RE" + str(Re[i]) + "/line3_U.xy"
        urls = [url_l1,url_l2,url_l3]
        u,v,xtemp = get_data(urls)
        x.append(xtemp)
        Ftemp, taotemp = evaluate_F(u)
        F[i] = Ftemp
        tao.append(taotemp)
    plot(tao, x)
    print(F)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
