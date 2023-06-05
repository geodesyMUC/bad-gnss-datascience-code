import pandas as pd
import numpy as np

# Generate sample data for 3 hours with one data point every second
timestamps = pd.date_range('2023-01-01 00:00:00', periods=3*60*60, freq='S')

# Generate random values for number of satellites with a logical pattern
num_satellites = [np.random.randint(0, 36)]
for _ in range(1, len(timestamps)):
    change = np.random.choice([-1, 0, 1], p=[0.2, 0.6, 0.2])  # Control the chance of sudden jumps
    new_value = max(0, min(35, num_satellites[-1] + change))  # Limit the value between 0 and 35
    num_satellites.append(new_value)

# Generate random values for PDOP with some outliers
pdop_values = np.random.normal(1, 0.2, len(timestamps))
pdop_values[np.random.choice(len(timestamps), size=50, replace=False)] = np.random.normal(10, 1, 50)

# Create a DataFrame with the generated data
df = pd.DataFrame({'timestamp': timestamps, 'num_satellites': num_satellites, 'pdop': pdop_values})

# Save the DataFrame to a CSV file
df.to_csv('sample_data.csv', index=False)
