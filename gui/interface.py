from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QVBoxLayout, QWidget, QRadioButton, QSlider,
    QHBoxLayout, QLabel, QSpinBox, QFileDialog, QMessageBox, QFrame
)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd

from gui.styles import STYLE_SHEET
from core.feature_extractor import extract_time_features, extract_frequency_features
from core.plotter import plot_segments

class FeatureApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seismic Signal Analyzer")
        self.setGeometry(100, 100, 1100, 800)
        self.setStyleSheet(STYLE_SHEET)

        # === Widgets ===
        self.upload_btn = QPushButton("📁 Load CSV")
        self.upload_btn.clicked.connect(self.load_csv)

        self.time_radio = QRadioButton("Time Domain")
        self.freq_radio = QRadioButton("Frequency Domain")
        self.time_radio.setChecked(True)

        self.extract_btn = QPushButton("⚙️ Extract & Label")
        self.extract_btn.clicked.connect(self.extract_features)
        self.extract_btn.setEnabled(False)

        self.save_btn = QPushButton("💾 Save CSV")
        self.save_btn.clicked.connect(self.save_csv)
        self.save_btn.setEnabled(False)

        self.exit_btn = QPushButton("🚪 Finish & Exit")
        self.exit_btn.clicked.connect(self.close)

        self.label = QLabel("🔹 Please load a CSV file to begin.")
        self.slider_label = QLabel("Threshold: 50")

        self.threshold_slider = QSlider(Qt.Orientation.Horizontal)
        self.threshold_slider.setMinimum(0)
        self.threshold_slider.setMaximum(100)
        self.threshold_slider.setValue(50)
        self.threshold_slider.setTickInterval(5)
        self.threshold_slider.setEnabled(False)
        self.threshold_slider.valueChanged.connect(self.slider_changed)

        self.plot_btn = QPushButton("📊 Plot in N Charts")
        self.plot_btn.clicked.connect(self.plot_signal_multiple)
        self.plot_btn.setEnabled(False)

        self.n_charts_input = QSpinBox()
        self.n_charts_input.setMinimum(1)
        self.n_charts_input.setValue(1)

        self.canvas = FigureCanvas(Figure(figsize=(10, 5)))
        self.ax = self.canvas.figure.subplots()

        # === Layout ===
        layout = QVBoxLayout()
        layout.addWidget(self.make_separator("1. Load Signal"))
        layout.addWidget(self.upload_btn)
        layout.addWidget(self.label)

        layout.addWidget(self.make_separator("2. Select Feature Domain"))
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.time_radio)
        radio_layout.addWidget(self.freq_radio)
        layout.addLayout(radio_layout)

        layout.addWidget(self.make_separator("3. Configure Threshold"))
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.slider_label)
        slider_layout.addWidget(self.threshold_slider)
        layout.addLayout(slider_layout)
        layout.addWidget(self.extract_btn)

        layout.addWidget(self.make_separator("4. Visualization"))
        chart_layout = QHBoxLayout()
        chart_layout.addWidget(QLabel("Number of Charts:"))
        chart_layout.addWidget(self.n_charts_input)
        chart_layout.addWidget(self.plot_btn)
        layout.addLayout(chart_layout)
        layout.addWidget(self.canvas)

        layout.addWidget(self.make_separator("5. Export & Exit"))
        export_layout = QHBoxLayout()
        export_layout.addWidget(self.save_btn)
        export_layout.addWidget(self.exit_btn)
        layout.addLayout(export_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.df = None
        self.features_df = None

    def make_separator(self, text):
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        label = QLabel(f"🔸 {text}")
        label.setStyleSheet("font-weight: bold; font-size: 15px; color: #2c3e50;")
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line)
        wrapper = QWidget()
        wrapper.setLayout(layout)
        return wrapper

    def load_csv(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if path:
            try:
                self.df = pd.read_csv(path, parse_dates=[0])
                self.df.columns = ['Timestamp', 'ADC']
                self.label.setText(f"✅ Loaded {len(self.df)} samples from file.")
                self.extract_btn.setEnabled(True)
                self.plot_btn.setEnabled(True)
                self.threshold_slider.setEnabled(True)
                self.plot_signal_multiple()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load CSV: {str(e)}")

    def plot_signal_multiple(self):
        n = self.n_charts_input.value()
        if self.df is None or n < 1:
            return
        plot_segments(self.canvas, self.df, n)

    def slider_changed(self, value):
        self.slider_label.setText(f"Threshold: {value}")
        if self.features_df is not None:
            self.label_rows()

    def extract_features(self):
        signal = self.df['ADC'].values
        window_size = 100
        n_windows = len(signal) // window_size
        rows = []

        for i in range(n_windows):
            segment = signal[i * window_size: (i + 1) * window_size]
            features = {"Window_ID": i}

            if self.time_radio.isChecked():
                features.update(extract_time_features(segment))
            else:
                features.update(extract_frequency_features(segment))

            rows.append(features)

        self.features_df = pd.DataFrame(rows)
        self.label_rows()
        self.save_btn.setEnabled(True)
        self.label.setText(f"✅ Extracted features for {n_windows} windows.")

    def label_rows(self):
        threshold = self.threshold_slider.value()
        self.features_df["Label"] = self.features_df["Score"].apply(
            lambda x: 1 if x > threshold else 0
        )

    def save_csv(self):
        if self.features_df is None:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Save Labeled CSV", "", "CSV Files (*.csv)")
        if path:
            self.features_df.to_csv(path, index=False)
            self.label.setText(f"💾 Labeled features saved to: {path}")
