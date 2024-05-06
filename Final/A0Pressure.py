import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
Graphs All plots of pressure vs percent of chord length against each other
'''
mesh = ('A0','A1','A4','A7')
labels = ('HIGH', 'MED', 'LOW')
forebot1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessing/singleGraph/1/forebot_p_T.xy', delim_whitespace=True, header=None)
forebot2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessingMED/singleGraph/4/forebot_p_T.xy', delim_whitespace=True, header=None)
forebot3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessingLOW/singleGraph/4/forebot_p_T.xy', delim_whitespace=True, header=None)
forebot = [forebot1, forebot2,forebot3]

foretop1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessing/singleGraph/1/foretop_p_T.xy', delim_whitespace=True, header=None)
foretop2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessingMED/singleGraph/4/foretop_p_T.xy', delim_whitespace=True, header=None)
foretop3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessingLOW/singleGraph/4/foretop_p_T.xy', delim_whitespace=True, header=None)
foretop = [foretop1, foretop2,foretop3]

wakebot1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessing/singleGraph/1/wakebot_p_T.xy', delim_whitespace=True, header=None)
wakebot2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessingMED/singleGraph/4/wakebot_p_T.xy', delim_whitespace=True, header=None)
wakebot3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessingLOW/singleGraph/4/wakebot_p_T.xy', delim_whitespace=True, header=None)
wakebot = [wakebot1, wakebot2, wakebot3]

waketop1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessing/singleGraph/1/waketop_p_T.xy', delim_whitespace=True, header=None)
waketop2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessingMED/singleGraph/4/waketop_p_T.xy', delim_whitespace=True, header=None)
waketop3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessingLOW/singleGraph/4/waketop_p_T.xy', delim_whitespace=True, header=None)
waketop = [waketop1, waketop2, waketop3]

# Assign column names to the DataFrame for clarity
for i in range(len(waketop)):
    forebot[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    foretop[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    waketop[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    wakebot[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    #wakebot[i] = wakebot[i].drop(wakebot[i].index[-1])


cmap = plt.get_cmap('plasma')

plt.figure()
for i in range(len(foretop)):  # changed range to 4 to iterate over all datasets
    # Plot the data
    vals = np.arange(len(foretop[i])) / len(foretop[i])
    plt.plot(vals, foretop[i]['p'], color = cmap(i/4), label = labels[i])  # corrected accessing the DataFrame
plt.title('Pressure on p1')
plt.xlabel('% of surface length')
plt.ylabel('$P$ (Pressure) $\\alpha=0$\u00b0')
plt.grid(True)
plt.legend()

plt.show()

plt.figure()
for i in range(len(foretop)):  # changed range to 4 to iterate over all datasets
    # Plot the data
    vals = np.arange(len(forebot[i])) / len(forebot[i])
    plt.plot(vals, forebot[i]['p'], color = cmap(i/4), label = labels[i])  # corrected accessing the DataFrame
plt.title('Pressure on p3')
plt.xlabel('% of surface length')
plt.ylabel('$P$ (Pressure) $\\alpha=0$\u00b0')
plt.grid(True)
plt.legend()
plt.show()

plt.figure()
for i in range(len(foretop)):  # changed range to 4 to iterate over all datasets
    # Plot the data
    vals = np.arange(len(wakebot[i])) / len(wakebot[i])
    plt.plot(vals, wakebot[i]['p'], color = cmap(i/4), label = labels[i])  # corrected accessing the DataFrame
plt.title('Pressure on p4')
plt.xlabel('% of surface length')
plt.ylabel('$P$ (Pressure) $\\alpha=0$\u00b0')
plt.grid(True)
plt.legend()

plt.show()

plt.figure()
for i in range(len(foretop)):  # changed range to 4 to iterate over all datasets
    # Plot the data
    vals = np.arange(len(waketop[i])) / len(waketop[i])
    plt.plot(vals, waketop[i]['p'], color = cmap(i/4), label = labels[i])  # corrected accessing the DataFrame
plt.title('Pressure on p2')
plt.xlabel('% of surface length')
plt.ylabel('$P$ (Pressure) $\\alpha=0$\u00b0')
plt.grid(True)
plt.legend()
plt.show()
