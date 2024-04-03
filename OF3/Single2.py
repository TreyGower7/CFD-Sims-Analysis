import pandas as pd
import matplotlib.pyplot as plt

mesh = ('Coarse','meshA','meshB','meshC')
bot1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[0]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
bot2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[1]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
bot3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[2]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
bot4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[3]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
bottom = (bot1, bot2,bot3,bot4)

top1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[0]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
top2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[1]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
top3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[2]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
top4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[3]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
top = (top1, top2,top3,top4)
f1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[0]}/singleGraph/4/top_p_T.xy', delim_whitespace=True, header=None)
f2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[1]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
f3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[2]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
f4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[3]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
stepfront = (f1, f2,f3,f4)

st1 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[0]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
st2 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[1]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
st3 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[2]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
st4 = pd.read_csv(f'https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/OF3/{mesh[3]}/singleGraph/4/bottom_p_T.xy', delim_whitespace=True, header=None)
steptop = (st1, st2,st3,st4)

names = ('Bottom', 'Top', 'Step Top', 'Step Front')
# Assign column names to the DataFrame for clarity
stepf = []  # Create an empty list to store filtered DataFrames

for i in range(len(mesh)):
    bottom[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    top[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    steptop[i].columns = ['X', 'Y', 'Z', 'p', 'T']
    stepfront[i].columns = ['X', 'Y', 'Z', 'p', 'T']

    # Filter rows where 'Y' <= 0.2 in each stepfront DataFrame
    filtered_stepfront = stepfront[i][stepfront[i]['Y'] <= 0.2]

    # Append the filtered DataFrame to the stepf list
    stepf.append(filtered_stepfront)

# Plotting
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for i in range(len(mesh)):
    row_index = i // 2
    col_index = i % 2
    ax = axes[row_index, col_index]
    ax.plot(bottom[i]['X'], bottom[i]['p'])
    ax.set_xlabel('X')
    ax.set_ylabel('Pressure (p)')
    ax.set_title(names[0])

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for i in range(len(mesh)):
    row_index = i // 2
    col_index = i % 2
    ax = axes[row_index, col_index]
    ax.plot(top[i]['X'], top[i]['p'])
    ax.set_xlabel('X')
    ax.set_ylabel('Pressure (p)')
    ax.set_title(names[1])

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for i in range(len(mesh)):
    row_index = i // 2
    col_index = i % 2
    ax = axes[row_index, col_index]
    ax.plot(steptop[i]['X'], steptop[i]['p'])
    ax.set_xlabel('X')
    ax.set_ylabel('Pressure (p)')
    ax.set_title(names[2])

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for i in range(len(mesh)):
    row_index = i // 2
    col_index = i % 2
    ax = axes[row_index, col_index]
    ax.plot(stepf[i]['Y'], stepf[i]['p'])  # Use stepf for plotting
    ax.set_xlabel('Y')
    ax.set_ylabel('Pressure (p)')
    ax.set_title(names[3])

plt.tight_layout()
plt.show()
