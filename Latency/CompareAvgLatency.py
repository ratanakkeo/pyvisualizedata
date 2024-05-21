import pandas as pd
import matplotlib.pyplot as plt

# Without Differential Privacy
data1 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Avg Latency (s)': [0.29, 0.57, 0.80, 0.99, 1.24, 1.46]
}
# With Differential Privacy
data2 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Avg Latency (s)': [0.34, 0.61, 0.81, 1.01, 1.42, 1.49],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

plt.plot(df1['Transaction'], df1['Avg Latency (s)'], marker='o', label='Without Differential Privacy')
plt.plot(df2['Transaction'], df2['Avg Latency (s)'], marker='o', label='With Differential Privacy')
plt.title('Avg Latency (s)')
plt.xlabel('Transaction')
plt.ylabel('Seconds')

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Save the plot with high resolution
plt.savefig('avg_latency.png', dpi=300)

# Show the plot
plt.show()
