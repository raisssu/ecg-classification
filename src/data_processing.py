from scipy.signal import butter, lfilter
import scipy.io
import numpy as np
import wfdb
import tqdm
import neurokit2 as nk

def bandpass_filter (signal, lowcut, highcut, sampling_rate, order = 2):
    
    nyquist = 0.5 * sampling_rate
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype = "band")
    y = lfilter(b, a, signal)
    return y

# def yo():
#     return "Gurt"
def derivative_filter(ecg_signal, fs = 100):
    kernel = np.array([-1, -2, 0, 1, 2]) * (1/8)
    return np.convolve(ecg_signal, kernel)


def pad_data(data):
    padded = np.empty((len(data), len(data[0])+100, len(data[0][0])))
    for i in range(len(data)):
            for j in range(len(data[0][0])):
                signal = data[i][:,j]
                inverted = nk.ecg_invert(signal, sampling_rate=100)
                padded[i][:,j] = np.pad(inverted[0],(100, 0), 'edge')
    return padded

                
        
