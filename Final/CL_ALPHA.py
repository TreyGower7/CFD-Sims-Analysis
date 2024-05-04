import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the singleGraph file into a Pandas DataFrame
data = pd.read_csv('/Users/treygower/Desktop/example/postProcessing/singleGraph/1/backbottom_p_T.xy', delim_whitespace=True, header=None)
# Replace 'path/to/your/singleGraph_file' with the actual path to your file
data.info()
# Assign column names to the DataFrame for clarity
data.columns = ['X', 'Y', 'Z', 'p', 'T']
data.info()
# Plot the data
plt.plot(data['p'], data['X'], label='')
#plt.plot(data[''], data['Value2'], label='Value2')
plt.xlabel('X')
plt.ylabel('Values')
plt.title('Data Visualization')
plt.legend()
plt.grid(True)
plt.show()