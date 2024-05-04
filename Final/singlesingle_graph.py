import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Read the data from the singleGraph file into a Pandas DataFrame
data = pd.read_csv('https://raw.githubusercontent.com/TreyGower7/CFD_Code/main/Final/A0/postProcessingLOW/singleGraph/4/forebot_p_T.xy', delim_whitespace=True, header=None)

# Replace 'path/to/your/singleGraph_file' with the actual path to your file
data.info()
# Assign column names to the DataFrame for clarity
data.columns = ['X', 'Y', 'Z', 'p', 'T']

# Generate values for 'vals' based on the length of data

vals = np.arange(len(data)) / len(data)
data.info()
# Plot the data
plt.plot(vals, data['p'], label='')
#plt.plot(data[''], data['Value2'], label='Value2')
plt.xlabel('Percent of surface length')
plt.ylabel('p (Pressure)')
plt.title('Diamond Front-Top Pressure')
plt.legend()
plt.grid(True)
plt.show()