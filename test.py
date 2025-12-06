import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample DataFrame
data = {
    'x_values': np.arange(0, 10),
    'y_values': np.random.rand(10).cumsum()
}
df = pd.DataFrame(data)

# Plotting directly using pandas built-in .plot() method
print("Displaying the plot...")
df.plot(x='x_values', y='y_values', title='Sample Line Plot in PyCharm')

# Required to display the plot window
plt.show()

