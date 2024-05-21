import pandas as pd
import matplotlib.pyplot as plt

# Without Differential Privacy
data1 = {
        'Transaction': [50, 100, 150, 200, 250, 300],
        'Send Rate (TPS)': [93.3, 98.0, 105.5, 114.0, 118.8, 123.6]
        }

# With Differential Privacy
data2 = {'Transaction': [50, 100, 150, 200, 250, 300],
         'Send Rate (TPS)': [84.0, 111.5, 117.3, 125.9, 129.4, 139.3]
         }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Plotting
plt.figure(figsize=(10, 6))

# Plot data
plt.plot(data1['Transaction'], data1['Send Rate (TPS)'], marker='o', label='Without Differential Privacy')
plt.plot(data2['Transaction'], data2['Send Rate (TPS)'], marker='o', label='With Differential Privacy')

# Set title and labels
plt.title('Send Rate (TPS)')
plt.xlabel('Transaction')
plt.ylabel('TPS')

# Add legend
plt.legend()
# Add grid
plt.grid(True)

plt.savefig('send_rate.png', dpi=300)
# Show the plot
plt.show()
