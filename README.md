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

## Interface Screenshots

![gui 1](https://github.com/user-attachments/assets/78f21b21-221b-4a2b-a193-b18d27507e2a)
![gui 2](https://github.com/user-attachments/assets/dc7ebdb8-cc0e-4b4d-bb08-548c7b75092f)

## How to Customize
- This application is modular and can be easily extended.

- Feature extraction logic is located in: core/feature_extractor.py

- Plotting logic is in: core/plotter.py

- Interface logic is in: gui/interface.py

- Styles and themes can be modified in: gui/styles.py

### You can customize it for:

- Medical signal analysis (e.g., ECG, EEG)

- Structural vibration monitoring

- Industrial equipment health diagnostics

- Sound event classification

Any other form of time-series signal processing

## How to Run

### 1. Install Python and Required Libraries

Make sure you have Python 3.9 or later installed.

Install the dependencies:

```bash
pip install PyQt6 matplotlib pandas numpy scipy
python main.py
