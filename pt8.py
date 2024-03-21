import numpy as np
import matplotlib.pyplot as plt
import requests 
from matplotlib.cm import get_cmap
import re
from scipy.fft import fft, ifft, fftfreq

"""
Module Docstring
"""

def get_U():
    u0 = []
    u1 = []
    t = []

    mesh = 'B4'
    line1 = f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF2/mesh{mesh}/U'
    response = requests.get(line1)
    if response.status_code == 200:
        lines1 = response.text.split('\n')  # Split the response into lines
    else:
        print("Failed to retrieve content. Status code:", response.status_code)

    pat = r'(\d+\.\d+)\s+\(([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\)\s+\(([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d+\.\d+(?:[eE][-+]?\d+)?)\)'

# Print the first few lines as an example
    for i, line in enumerate(lines1):
        match = re.search(pat,line)
        if match:
            dim = match.groups()
            if float(dim[0]) >= 65:
                u0.append(float(dim[1])) #probe 1 u vel
                t.append(float(dim[0]))
                u1.append(float(dim[4])) #probe 2 u vel

    return u0,u1,t
def fast_fourier(u0,u1,t):
    N = len(t)
    T = t[1] - t[0]  #uniform time steps
    x = np.linspace(0.0, 0.5 / T, N//2)  # Adjusted x-axis range
    y = u0  # Or any other data to perform FFT on
    y2 = u1
    yf = fft(y)
    yf2 = fft(y2)
    xf = fftfreq(N, T)[:N//2]
    xf2 = fftfreq(N, T)[:N//2]
    plt.plot(xf, 1.0/N * np.abs(yf[0:N//2]), label = 'Probe 1', color='r')
    plt.plot(xf2, 1.0/N * np.abs(yf2[0:N//2]), label = 'Probe 2', color ='b')
    plt.ylabel('Amplitude')
    plt.xlabel(r'Frequency (Hz)')
    plt.legend()
    plt.grid()
    plt.xlim([.06, 1])  # Adjusted x-axis limits
    plt.ylim([0, .2])
    plt.show()
    

# example y = fft(x)
 
    return 0

def main():
    #Getting oscillitory u vels and time steps
    u0,u1,t =  get_U()
    fast_fourier(u0,u1,t)
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()