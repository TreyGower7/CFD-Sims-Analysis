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
    ind=[10,100,250,500];
    uvec = [[]]
    vvec = [[]]
    xvec = [[]]
    yvec = [[]]
    for k in range(4):

        url_l1 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt2/RE" + str(ind[k]) + "/line1_U.xy"
        url_l2 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt2/RE" + str(ind[k]) + "/line2_U.xy"
        url_l3 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt2/RE" + str(ind[k]) + "/line3_U.xy"
        url_l4 = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt2/RE" + str(ind[k]) + "/line4_U.xy"
        urls = [url_l1,url_l2,url_l3,url_l4]
        data = []
        data_RE = []

        for i in range(4):
            response = requests.get(urls[i])

            if response.status_code == 200:
                for i in range(4):
                    # Split the response into lines
                    data.append(response.text.split('\n')) 
            else:
                print("Failed to retrieve content. Status code:", response.status_code)
       #u = np.zeros([len(data),1])
        #v = np.zeros([len(data),1])
        #x = np.zeros([len(data),1])
        #y = np.zeros([len(data),1])
        #for i in range(len(data)-1):
        #    u[i] = float((data[i].split())[3])
        #    v[i] = float((data[i].split())[4])
        #    x[i] = float((data[i].split())[0])
        #    y[i] = float((data[i].split())[1])
        #Weird but okay getting rid of random zero
        #u = u[:-1]
        #v = v[:-1]
        #x = x[:-1]
        #y = y[:-1]
        #uvec.append(u)
        #vvec.append(v)
        #xvec.append(x)
        #yvec.append(y)
        #clear urls and data for next iteration
        del urls
        data_RE.append(data)
        del data
        #Weird but okay getting rid of random zero
    #index to next grid size
    print(data_RE[1])
    #return uvec,vvec,xvec,yvec

def evaluate_F():
    """
    Evaluates the one sided finite difference to approximate partial(u)/partial(y)
    """
def plot_F_RE(u,v,y):
    """
    Plotting for F vs RE
    """

def main():
    """ Main entry point of the app """
    get_data()
    #u,v,x,y = get_data()
    #plot_F_RE(u,v,y)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
