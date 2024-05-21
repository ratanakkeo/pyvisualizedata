import matplotlib.pyplot as plt
import pandas as pd


# Without Differential Privacy
data1 = {
        'Transaction': [50, 100, 150, 200, 250, 300],
        'Send Rate (TPS)': [93.3, 98.0, 105.5, 114.0, 118.8, 123.6]
        }
# Without Differential Privacy
data2 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Throughput (TPS)': [90.6, 95.1, 102.7, 109.9, 114.8, 117.2]
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
plt.title('Send Rate vs Throughput without Differential Privacy')

# Add a legend
plt.legend()

plt.grid(True)

# Show the plot
plt.show()
