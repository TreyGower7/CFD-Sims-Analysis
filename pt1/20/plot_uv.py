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
    url = "https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/pt1/20/line1_U.xy"
    response = requests.get(url)
    #data = []
    if response.status_code == 200:
        data = response.text.split('\n')  # Split the response into lines
        for line in data:
            print(line)  # Example: Print each line
    else:
        print("Failed to retrieve content. Status code:", response.status_code)

    print(data)

def main():
    """ Main entry point of the app """
    data = get_data()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
