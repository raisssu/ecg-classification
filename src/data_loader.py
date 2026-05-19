import numpy as np
import wfdb
import tqdm
import pandas as pd
import ast
# import ast 
# import pandas as pd
from data_processing import bandpass_filter
import neurokit2 as nk

def load_raw_data():
    path = "../data/raw/ptb-xl-1.0.3/"
    sampling_rate = 100

    df = pd.read_csv(path + "ptbxl_database.csv", index_col='ecg_id')
    df.scp_codes = df.scp_codes.apply(lambda x: ast.literal_eval(x))

    if sampling_rate == 100:
        data = [wfdb.rdsamp(path+f) for f in tqdm.tqdm(df.filename_lr)] # .head(100) for testing
    else:
        data = [wfdb.rdsamp(path+f) for f in tqdm.tqdm(df.filename_hr)]
    data = np.array([signal for signal, meta in data])
    return data

def cleaned_data(data=None):
    
    lowcut = 0.5
    highcut = 24.0
    sampling_rate = 100
    
    if data is None:
        data = load_raw_data()
        
    cleaned = [0] * len(data)
    for i in range(len(data)):
        flattened_signal = data[i].flatten()
        filtered_signal = bandpass_filter(flattened_signal, lowcut, highcut, sampling_rate)
        reshaped_data = filtered_signal.reshape(1000, 12)
        cleaned[i] = reshaped_data
        
    
    
    return cleaned


# path = "data/raw/ptb-xl-1.0.3/"
# sampling_rate = 100

# Y = pd.read_csv(path + "ptbxl_database.csv", index_col='ecg_id')
# Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))

# X = load_raw_data(Y, sampling_rate, path)