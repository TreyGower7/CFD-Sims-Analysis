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
    url = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt2/RE10/line1_U.xy"
    response = requests.get(url)
    #data = []
    if response.status_code == 200:
        data = response.text.split('\n')  # Split the response into lines
        for line in data:
            print(line)  # Example: Print each line
    else:
        print("Failed to retrieve content. Status code:", response.status_code)
    u = np.zeros([len(data),1])
    v = np.zeros([len(data),1])
    for i in range(len(data)-1):
        u[i] = float((data[i].split())[3])
        v[i] = float((data[i].split())[4])

    #Weird but okay getting rid of random zero
    u = u[:-1]
    v = v[:-1]
def main():
    """ Main entry point of the app """
    data = get_data()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
