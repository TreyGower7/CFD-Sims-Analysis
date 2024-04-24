import pandas as pd
import matplotlib.pyplot as plt

mesh = ('Coarse','meshA','meshB','meshC')
bot1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[0]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
bot2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[1]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
bot3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[2]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
bot4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[3]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
bottom = [bot1, bot2,bot3,bot4]

top1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[0]}/singleGraph/4/top_p_T.xy', delim_whitespace=True, header=None)
top2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[1]}/singleGraph/4/top_p_T.xy', delim_whitespace=True, header=None)
top3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[2]}/singleGraph/4/top_p_T.xy', delim_whitespace=True, header=None)
top4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[3]}/singleGraph/4/top_p_T.xy', delim_whitespace=True, header=None)
top = [top1, top2,top3,top4]
f1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[0]}/singleGraph/4/stepfront_p_T.xy', delim_whitespace=True, header=None)
f2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[1]}/singleGraph/4/stepfront_p_T.xy', delim_whitespace=True, header=None)
f3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[2]}/singleGraph/4/stepfront_p_T.xy', delim_whitespace=True, header=None)
f4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[3]}/singleGraph/4/stepfront_p_T.xy', delim_whitespace=True, header=None)
stepfront = [f1, f2,f3,f4]

st1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[0]}/singleGraph/4/steptop_p_T.xy', delim_whitespace=True, header=None)
st2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[1]}/singleGraph/4/steptop_p_T.xy', delim_whitespace=True, header=None)
st3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[2]}/singleGraph/4/steptop_p_T.xy', delim_whitespace=True, header=None)
st4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[3]}/singleGraph/4/steptop_p_T.xy', delim_whitespace=True, header=None)
steptop = [st1, st2,st3,st4]

names = ['Bottom', 'Top', 'Step Top', 'Step Front']
# Assign column names to the DataFrame for clarity
stepf = []
for i in range(len(mesh)):
    bottom[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    top[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    steptop[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    stepfront[i].columns = ['X', 'Y', 'Z', 'p', 'T']

# Filter rows where 'Y' >= 0.2
# Filter rows where 'Y' is less than or equal to 0.2
    filtered = stepfront[i][stepfront[i]['Y'] <= 0.2]
    stepf.append(filtered)

cmap = plt.get_cmap('gist_rainbow')
# Plotting
plt.figure()
for i in range(4):  # changed range to 4 to iterate over all datasets
    plt.subplot(2,2,i+1)
    # Plot the data
    plt.plot(bottom[i]['X'], bottom[i]['p'])  # corrected accessing the DataFrame
    plt.xlabel('X')
    plt.ylabel('Pressure (p)')
    plt.grid(True)

plt.title(names[0])  # Adding titles
plt.show()

plt.figure()
for i in range(4):  # changed range to 4 to iterate over all datasets
    #plt.subplot(2,2,i+1)
    # Plot the data

    plt.plot(top[i]['X'], top[i]['T'], color = cmap(i/4), label = mesh[i])  # corrected accessing the DataFrame
    plt.xlabel('X')
    plt.ylabel('Temperature (K)')
    plt.grid(True)

plt.legend()
plt.title('Temperature vs. X Coordinate in The Top of The Domain')  # Adding titles
plt.show()

plt.figure()
for i in range(4):  # changed range to 4 to iterate over all datasets
    plt.subplot(2,2,i+1)
    # Plot the data
    plt.plot(steptop[i]['X'], steptop[i]['p'])  # corrected accessing the DataFrame
    plt.xlabel('X')
    plt.ylabel('Pressure (p)')
    plt.grid(True)

plt.title(names[2])  # Adding titles
plt.show()

plt.figure()
for i in range(4):  # changed range to 4 to iterate over all datasets
    plt.subplot(2,2,i+1)
    # Plot the data
    plt.plot(stepf[i]['Y'], stepf[i]['p'])  # corrected accessing the DataFrame
    plt.xlabel('Y')
    plt.ylabel('Pressure (p)')
    plt.grid(True)

plt.title(names[3])  # Adding titles
plt.show()
