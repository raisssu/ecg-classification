from scipy.signal import butter, lfilter
import scipy.io
import numpy as np
import wfdb
import tqdm

def bandpass_filter (signal, lowcut, highcut, sampling_rate, order = 2):
    
    nyquist = 0.5 * sampling_rate
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype = "band")
    y = lfilter(b, a, signal)
    return y

def yo():
    return "Gurt"
def derivative_filter(ecg_signal, fs = 100):
    kernel = np.array([-1, -2, 0, 1, 2]) * (1/8)
    return np.convolve(ecg_signal, kernel)
