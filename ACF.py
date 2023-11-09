import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


def plot_autocorrelation(file_path, nlags=40):
    # load file
    data = np.loadtxt(file_path)
    time = data[:, 0]
    voltage = data[:, 1]

    # calculate autocorrelation function
    acf_result = sm.tsa.acf(voltage, nlags=nlags, fft=True)

    # lagtime
    average_time_diff = np.mean(np.diff(time))

    # plot the graph
    plt.figure(figsize=(14, 6))
    lags = np.arange(len(acf_result))
    plt.plot(lags * average_time_diff, acf_result, marker='o', linestyle='-')
    plt.title('Autocorrelation Function')
    plt.xlabel(f'Time delay (seconds, per lag = {average_time_diff:.6f}s)')
    plt.ylabel('Autocorrelation')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# file-path
plot_autocorrelation(r"E:\新建文件夹\experimental fluid mechanics\lab data\Group 4\Group 4\CTA measurements of donwstream of cylinder\35%_voltage_300Hz_x25mm_y5mm-1.txt", nlags=40)

