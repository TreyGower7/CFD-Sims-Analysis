import numpy as np
import matplotlib.pyplot as plt
import requests 
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
    for k in range(4):
        url = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt1/" + str(ind) + "/line1_U.xy"
        response = requests.get(url)
        data = []
        if response.status_code == 200:
            data = response.text.split('\n')  # Split the response into lines
            for line in data:
                print('')  # Example: Print each line
        else:
            print("Failed to retrieve content. Status code:", response.status_code)
        u = np.zeros([len(data),4])
        v = np.zeros([len(data),4])
        y = np.zeros([len(data),4])
        x = np.zeros([len(data),4])
        for i in range(len(data)-1):
            u[i,k] = float((data[i].split())[3])
            v[i,k] = float((data[i].split())[4])
            x[i,k] = float((data[i].split())[0])
            y[i,k] = float((data[i].split())[1])
        ind *= 2
        #Weird but okay getting rid of random zero
    u = u[:-1, :]
    v = v[:-1, :] 
    x = x[:-1, :]
    y = y[:-1, :]
    #index to next grid size
    return u,v,x,y
def plot(u,v,y):
    """Plotting for u vs v with x=.5
    """
    plt.plot(y, u, '-b', label='u vel')
    plt.plot(y, v, '-r', label='v vel')
    plt.legend(loc='upper left')  # Specify loc directly as a keyword argument
    plt.title('velocity vs y, grid size 20, RE=10')
    plt.xlabel('y')
    plt.ylabel('Velocity')
    plt.grid()
    plt.show()

    plt.plot(y,v, '-r')
    plt.title('v vs y, grid size 20, RE=10')
    plt.xlabel('y')
    plt.ylabel('v')
    plt.grid()
    plt.show()


def main():
    """ Main entry point of the app """
    u,v,x,y = get_data()

    print('u0')
    print(u[1:20,1])

    #plot(u,v,y)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
