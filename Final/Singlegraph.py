import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mesh = ('A0','A1','A4','A7')
forebot1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessing/singleGraph/1/forebot_p_T.xy', delim_whitespace=True, header=None)
forebot2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[1]}/postProcessing/singleGraph/1/forebot_p_T.xy', delim_whitespace=True, header=None)
forebot3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[2]}/postProcessing/singleGraph/1/forebot_p_T.xy', delim_whitespace=True, header=None)
forebot4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[3]}/postProcessing/singleGraph/1/forebot_p_T.xy', delim_whitespace=True, header=None)
forebot = [forebot1, forebot2,forebot3,forebot4]

foretop1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessing/singleGraph/1/foretop_p_T.xy', delim_whitespace=True, header=None)
foretop2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[1]}/postProcessing/singleGraph/1/foretop_p_T.xy', delim_whitespace=True, header=None)
foretop3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[2]}/postProcessing/singleGraph/1/foretop_p_T.xy', delim_whitespace=True, header=None)
foretop4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[3]}/postProcessing/singleGraph/1/foretop_p_T.xy', delim_whitespace=True, header=None)
foretop = [foretop1, foretop2,foretop3,foretop4]

wakebot1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessing/singleGraph/1/wakebot_p_T.xy', delim_whitespace=True, header=None)
wakebot2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[1]}/postProcessing/singleGraph/1/wakebot_p_T.xy', delim_whitespace=True, header=None)
wakebot3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[2]}/postProcessing/singleGraph/1/wakebot_p_T.xy', delim_whitespace=True, header=None)
wakebot4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[3]}/postProcessing/singleGraph/1/wakebot_p_T.xy', delim_whitespace=True, header=None)
wakebot = [wakebot1, wakebot2, wakebot3,wakebot4]

waketop1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[0]}/postProcessing/singleGraph/1/waketop_p_T.xy', delim_whitespace=True, header=None)
waketop2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[1]}/postProcessing/singleGraph/1/waketop_p_T.xy', delim_whitespace=True, header=None)
waketop3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[2]}/postProcessing/singleGraph/1/waketop_p_T.xy', delim_whitespace=True, header=None)
waketop4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/{mesh[3]}/postProcessing/singleGraph/1/waketop_p_T.xy', delim_whitespace=True, header=None)
waketop = [waketop1, waketop2,waketop3,waketop4]

names = ['foretop', 'forebot', 'wakebot', 'waketop']
# Assign column names to the DataFrame for clarity
for i in range(len(mesh)):
    forebot[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    foretop[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    waketop[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    wakebot[i].columns = ['X', 'Y', 'Z', 'p', 'T']

vals = np.arange(len(forebot1)) / len(forebot1)

#cmap = plt.get_cmap('giwaketop_rainbow')

# plt.figure()
# for i in range(4):  # changed range to 4 to iterate over all datasets
# #plt.subplot(2,2,i+1)
# # Plot the data

# plt.plot(foretop[i]['X'], foretop[i]['T'], color = cmap(i/4), label = mesh[i])  # corrected accessing the DataFrame
# plt.xlabel('X')
# plt.ylabel('Temperature (K)')
# plt.grid(True)

# plt.legend()
# plt.title('Temperature vs. X Coordinate in The foretop of The Domain')  # Adding titles
# plt.show()

# Plotting
plt.figure()
for i in range(4):  # changed range to 4 to iterate over all datasets
    plt.subplot(2,2,i+1)
    # Plot the data
    plt.plot(vals, forebot[i]['p'])  # corrected accessing the DataFrame
    plt.xlabel('Percent of surface length')
    plt.ylabel('p (Pressure) on Front Bot')
    #plt.title('Pressure on Diamonds Front Bottom')
    plt.grid(True)

#plt.title(names[0])  # Adding titles
plt.show()

plt.figure()
for i in range(4):  # changed range to 4 to iterate over all datasets
    plt.subplot(2,2,i+1)
    # Plot the data
    plt.plot(vals, foretop[i]['p'])  # corrected accessing the DataFrame
    plt.xlabel('Percent of surface length')
    plt.ylabel('p (Pressure) on Front Top')
    #plt.title('Pressure on Diamonds Front Top')
    plt.grid(True)

#plt.title(names[2])  # Adding titles
plt.show()

plt.figure()
for i in range(4):  # changed range to 4 to iterate over all datasets
    plt.subplot(2,2,i+1)
    vals = np.arange(len(int(f'waketop{i}'))) / len(waketop1)

    # Plot the data
    plt.plot(vals, waketop[i]['p'])  # corrected accessing the DataFrame
    plt.xlabel('Percent of surface length')
    plt.ylabel('p (Pressure) on Back Top')
    #plt.title('Pressure on Diamonds Back Top')
    plt.grid(True)

#plt.title(names[3])  # Adding titles
plt.show()

plt.figure()
for i in range(4):  # changed range to 4 to iterate over all datasets
    plt.subplot(2,2,i+1)
    # Plot the data
    plt.plot(vals, wakebot[i]['p'])  # corrected accessing the DataFrame
    plt.xlabel('Percent of surface length')
    plt.ylabel('p (Pressure) on Back Bot')
    plt.grid(True)

#plt.title('Pressure on Diamonds Back Top')
plt.show()