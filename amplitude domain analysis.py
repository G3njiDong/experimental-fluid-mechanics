import numpy as np
from scipy.stats import skew, kurtosis

def calculate_statistics(file_path):
    # load the data
    try:
        # the second row is speed
        data = np.loadtxt(file_path)
    except Exception as e:
        return f"Error reading the file: {e}"

    # mean
    mean_velocity = np.mean(data)

    # variance
    var_val = np.var(data)

    # RMS of velocities
    rms_val = np.sqrt(np.mean(data ** 2))

    # fluctuations RMS
    rms_fluctuation = np.sqrt(np.mean((data - mean_velocity) ** 2))

    # skewness
    skew_val = skew(data)

    # kurtosis
    kurt_val = kurtosis(data)

    # （Intensity）
    intensity_val = rms_fluctuation / mean_velocity if mean_velocity != 0 else float('inf')

    return mean_velocity, var_val, rms_val, rms_fluctuation, skew_val, kurt_val, intensity_val


file_path = r"E:\新建文件夹\experimental fluid mechanics\Group 4\Group 4\downstream 6Khz.txt"  # file_path
mean_velocity, variance, rms, rms_fluctuation, skewness, kurtosis, intensity = calculate_statistics(file_path)

print(f"Mean Velocity: {mean_velocity}")
print(f"Variance: {variance}")
print(f"RMS (of the entire signal): {rms}")
print(f"RMS Velocity Fluctuation: {rms_fluctuation}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")
print(f"Intensity (based on fluctuation): {intensity}")



