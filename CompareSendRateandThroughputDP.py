import matplotlib.pyplot as plt
import pandas as pd

# With Differential Privacy
data1 = {'Transaction': [50, 100, 150, 200, 250, 300],
         'Send Rate (TPS)': [84.0, 111.5, 117.3, 125.9, 129.4, 139.3]
         }
# With Differential Privacy
data2 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Throughput (TPS)': [81.4, 107.9, 113.9, 118.9, 125.4, 130.3]
}


# Convert the dictionaries to pandas DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Plot the data
plt.figure(figsize=(10,6))
plt.plot(df1['Transaction'], df1['Send Rate (TPS)'], marker='o', label='Send Rate (TPS)')
plt.plot(df2['Transaction'], df2['Throughput (TPS)'], marker='o', label='Throughput (TPS)')

# Add labels and title
plt.xlabel('Transaction')
plt.ylabel('TPS')
plt.title('Send Rate vs Throughput with Differential Privacy')

# Add a legend
plt.legend()

plt.grid(True)

# Show the plot
plt.show()
