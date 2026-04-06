import neurokit2 as nk
import numpy as np
import pandas as pd
import tqdm
from data_loader import cleaned_data
from data_processing import pad_data
import ast

if __name__ == "__main__":
    data = cleaned_data()
    padded_data = pad_data(data)
    print(padded_data.shape)



#  [
        
#         waves_peak["ECG_T_Peaks"],
#         waves_peak["ECG_P_Peaks"],
#         waves_peak["ECG_Q_Peaks"],
#         waves_peak["ECG_S_Peaks"],
#         rpeaks["ECG_R_Peaks"],
#     ],
#     ecg_signal,