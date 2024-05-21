import pandas as pd
import matplotlib.pyplot as plt

# Without Differential Privacy
data1 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Throughput (TPS)': [90.6, 95.1, 102.7, 109.9, 114.8, 117.2]
}
# With Differential Privacy
data2 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Throughput (TPS)': [81.4, 107.9, 115.9, 120.9, 126.4, 137.3]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Plotting
plt.figure(figsize=(10, 6))

# Plot data
plt.plot(df1['Transaction'], df1['Throughput (TPS)'], marker='o', label='Without Differential Privacy')
plt.plot(df2['Transaction'], df2['Throughput (TPS)'], marker='o', label='With Differential Privacy')

# Set title and labels
plt.title('Throughput (TPS)')
plt.xlabel('Transaction')
plt.ylabel('TPS')

# Add legend
plt.legend()

# Add grid
plt.grid(True)

plt.savefig('throughput.png', dpi=300)

# Show the plot
plt.show()
