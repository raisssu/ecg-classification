from concurrent.futures import ProcessPoolExecutor

import neurokit2 as nk
import numpy as np
import pandas as pd
import tqdm
from data_loader import cleaned_data
from data_processing import pad_data
import ast

def clean_peaks(peaks):
    return [int(peak) for peak in peaks if not np.isnan(peak) and peak < 5000]

def process_sample(padded_sample, sample, i=0, j=0):
    
    # print(padded_sample)
    # return padded_sample
    _, rpeaks = nk.ecg_peaks(padded_sample, sampling_rate=100)
    
    if len(rpeaks["ECG_R_Peaks"]) < 4:
        _, rpeaks = nk.ecg_peaks(padded_sample, sampling_rate=100, method="elgendi2010")

    rpeaks["ECG_R_Peaks"] = rpeaks["ECG_R_Peaks"]-100
    
    try:
        _, waves_peak = nk.ecg_delineate(sample, rpeaks, sampling_rate=100)
        
        
        cleaned_r = clean_peaks(rpeaks["ECG_R_Peaks"])
        cleaned_q = clean_peaks(waves_peak["ECG_Q_Peaks"])
        cleaned_s = clean_peaks(waves_peak["ECG_S_Peaks"])
        cleaned_t = clean_peaks(waves_peak["ECG_T_Peaks"])
        cleaned_p = clean_peaks(waves_peak["ECG_P_Peaks"])
        
        peaks = {
            "ECG_R_Peaks": cleaned_r,
            "ECG_Q_Peaks": cleaned_q,
            "ECG_S_Peaks": cleaned_s,
            "ECG_T_Peaks": cleaned_t,
            "ECG_P_Peaks": cleaned_p,
        }
        
        return peaks
    except:
        return ("failed at sample ", i)
    
    
#  
#     ecg_signal,