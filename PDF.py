import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Replace 'your_file.txt' with the path to your text file
file_path = r"E:\新建文件夹\experimental fluid mechanics\Group 4\Group 4\35% calibrated speed.txt"

# Load the voltage data from the text file (assuming it's in the first column)
voltage_data = np.loadtxt(file_path)

# Perform a Gaussian Kernel Density Estimate (KDE)
kde = gaussian_kde(voltage_data)

# Create a range of values over which to evaluate the KDE
x_grid = np.linspace(voltage_data.min(), voltage_data.max(), 1000)

# Evaluate the KDE to get the PDF values
pdf_values = kde(x_grid)

# Plot the PDF
plt.figure(figsize=(10, 6))
plt.plot(x_grid, pdf_values, label='PDF')
plt.xlabel('Velocity')
plt.ylabel('Probability Density')
plt.title('6Khz calibration')
plt.legend()
plt.show()
