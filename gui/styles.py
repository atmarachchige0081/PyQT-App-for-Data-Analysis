STYLE_SHEET = """
QMainWindow { background-color: #f0f4f8; }

QPushButton {
    background-color: #4a90e2; color: white; font-weight: bold;
    border-radius: 6px; padding: 6px;
}
QPushButton:hover { background-color: #357ABD; }

QLabel {
    font-size: 14px;
    color: #2c3e50;
}

QRadioButton {
    font-size: 14px;
    color: #2c3e50;
    spacing: 10px;
}
QRadioButton::indicator:checked {
    background-color: #27ae60;
    border: 1px solid #27ae60;
}

QSlider::groove:horizontal {
    background: #ddd;
    height: 8px;
}
QSlider::handle:horizontal {
    background: #e67e22;
    width: 18px;
    margin: -5px 0;
    border-radius: 4px;
}

QSpinBox {
    background-color: white;
    border: 1px solid #ccc;
    padding: 4px;
    font-size: 13px;
}
"""