import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
file_path = r"E:\新建文件夹\experimental fluid mechanics\lab data\Group 4\Group 4\CTA measurements of donwstream of cylinder\35%_voltage_390Hz_x25mm_y5mm-1.txt"
def plot_power_spectrum(file_path, nlags=None, plot_acf=False):
    # Load data
    data = np.loadtxt(file_path)
    time = data[:, 0]
    voltage = data[:, 1]

    # Compute the autocorrelation function
    if nlags is None:
        nlags = len(voltage) - 1  # max lags
    acf_result = sm.tsa.acf(voltage, nlags=nlags, fft=True)

    # Compute the power spectrum using FFT of the autocorrelation function
    power_spectrum = np.fft.fft(acf_result)
    half_spectrum = power_spectrum[:len(power_spectrum) // 2]

    # Calculate the frequency axis for the power spectrum
    sample_spacing = np.mean(np.diff(time))
    freq = np.fft.fftfreq(nlags+1, d=sample_spacing)
    half_freq = freq[:len(freq) // 2]

    # Plotting the power spectrum
    plt.figure(figsize=(14, 6))
    plt.plot(half_freq, np.abs(half_spectrum), marker='o', linestyle='-')
    plt.title('Power Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Find the index and the frequency of the peak in the power spectrum
    peak_index = np.argmax(np.abs(half_spectrum))
    peak_frequency = half_freq[peak_index]
    print(f"The peak frequency is: {peak_frequency:.2f} Hz")

plot_power_spectrum(file_path, nlags=10000, plot_acf=True)

# Example usage:
# plot_power_spectrum('path_to_your_data.txt', nlags=40, plot_acf=True)
