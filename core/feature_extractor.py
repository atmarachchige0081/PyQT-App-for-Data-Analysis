import numpy as np
from scipy.fft import fft

def extract_time_features(signal):
    return {
        "RMS_Energy": np.sqrt(np.mean(signal ** 2)),
        "ZCR": ((signal[:-1] * signal[1:]) < 0).sum(),
        "Peak_to_Peak": np.ptp(signal),
        "Variance": np.var(signal),
        "Score": np.sqrt(np.mean(signal ** 2))
    }

def extract_frequency_features(signal):
    fft_vals = np.abs(fft(signal))[:len(signal)//2]
    return {
        "Peak_Frequency": np.argmax(fft_vals),
        "Spectral_Spread": np.std(fft_vals),
        "FFT_Area": np.sum(fft_vals),
        "Spectral_Flatness": (
            np.exp(np.mean(np.log(fft_vals + 1e-12))) /
            (np.mean(fft_vals) + 1e-12)
        ),
        "Score": np.argmax(fft_vals)
    }