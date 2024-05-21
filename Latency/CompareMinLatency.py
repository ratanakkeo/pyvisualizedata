import pandas as pd
import matplotlib.pyplot as plt

# Without Differential Privacy
data1 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Min Latency (s)': [0.12, 0.13, 0.10, 0.10, 0.13, 0.10],
}
# With Differential Privacy
data2 = {
    'Transaction': [50, 100, 150, 200, 250, 300],
    'Min Latency (s)': [0.07, 0.12, 0.11, 0.12, 0.15, 0.11],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

plt.plot(df1['Transaction'], df1['Min Latency (s)'], marker='o', label='Without Differential Privacy')
plt.plot(df2['Transaction'], df2['Min Latency (s)'], marker='o', label='With Differential Privacy')
plt.title('Min Latency (s)')
plt.xlabel('Transaction')
plt.ylabel('Seconds')

# Add legend
plt.legend()

# Add grid
plt.grid(True)

plt.savefig('min_latency.png', dpi=300)

# Show the plot
plt.show()
