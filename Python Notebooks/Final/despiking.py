import matplotlib.pyplot as plt
from scipy.signal import medfilt

def plot_despiked_data(time, signal_intensity, kernel_size):
    """
    This function takes the time and signal intensity data and applies a median filter
    with the specified kernel size to despike the data. It then plots both the original
    and despiked data.

    Parameters:
    - time: Time data for the x-axis (Pandas Series or list).
    - signal_intensity: Original signal intensity data to be despiked (Pandas Series or list).
    - kernel_size: Size of the kernel to be used in the median filter (integer).

    Returns:
    - median_signal_intensity: The despiked signal intensity data (Pandas Series or list).
    """
    # Call the despiked_signal_intensity function to get median-filtered data
    median_signal_intensity = despiked_signal_intensity(signal_intensity, kernel_size)

    # Plot the original and despiked data
    plt.figure(figsize=(10, 6))
    plt.plot(time, signal_intensity, label='Original Data')
    plt.plot(time, median_signal_intensity, label='Despiked Data', color='red')
    plt.title(f'Despiking Using Median Filter (Kernel Size: {kernel_size})')
    plt.xlabel('Time (min)')
    plt.ylabel('Signal Intensity (V)')
    plt.legend()
    plt.show()
    
    # Return the median-filtered data
    return median_signal_intensity

def despiked_signal_intensity(signal_intensity, kernel_size):
    """
    Applies a median filter to the provided signal intensity data.

    Parameters:
    - signal_intensity: Original signal intensity data (Pandas Series or list).
    - kernel_size: Size of the kernel to be used in the median filter (integer).

    Returns:
    - Median-filtered signal intensity data (Pandas Series or list).
    """
    return medfilt(signal_intensity, kernel_size)