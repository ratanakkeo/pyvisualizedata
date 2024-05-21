import pandas as pd
import matplotlib.pyplot as plt

# Without Differential Privacy
data1 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Max Latency (s)': [2.07, 2.19, 2.47, 2.31, 2.77, 2.94],
}
# With Differential Privacy
data2 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Max Latency (s)': [2.18, 2.22, 2.53, 2.63, 3.37, 3.53],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

plt.plot(df1['Transaction'], df1['Max Latency (s)'], marker='o', label='Without Differential Privacy')
plt.plot(df2['Transaction'], df2['Max Latency (s)'], marker='o', label='With Differential Privacy')
plt.title('Max Latency (s)')
plt.xlabel('Transaction')
plt.ylabel('Seconds')

# Add legend
plt.legend()

# Add grid
plt.grid(True)

plt.savefig('max_latency.png', dpi=300)

# Show the plot
plt.show()