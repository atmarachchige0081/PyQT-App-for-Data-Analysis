# Seismic Signal Analyzer

Seismic Signal Analyzer is a desktop application built using PyQt6 that enables engineers and researchers to analyze seismic signals from sensors. It provides a simple interface to load time-series data, extract features in time or frequency domains, label the data based on thresholds, and export results for further analysis or machine learning tasks.

This project was created as part of my final year engineering project to help in the classification of seismic activity, specifically focused on detecting low-frequency ground events such as elephant movements or similar environmental signals.

---

## Features

- Load CSV files containing timestamped ADC (Analog-to-Digital Converter) values.
- Visualize the full signal and split it into multiple plots for detailed analysis.
- Extract features from the signal in non-overlapping windows of 100 samples:
  - Time Domain Features:
    - RMS Energy
    - Zero Crossing Rate (ZCR)
    - Peak-to-Peak Amplitude
    - Variance
  - Frequency Domain Features:
    - Peak Frequency
    - Spectral Spread
    - FFT Area
    - Spectral Flatness
- Adjustable threshold slider to label each window as either low or high activity.
- Save extracted features and labels into a new CSV file.
- Modern, user-friendly graphical interface.

---

## How to Run

### 1. Install Python and Required Libraries

Make sure you have Python 3.9 or later installed.

Install the dependencies:

```bash
pip install PyQt6 matplotlib pandas numpy scipy
python main.py



