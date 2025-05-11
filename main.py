from PyQt6.QtWidgets import QApplication
from gui.interface import FeatureApp
import sys

def main():
    app = QApplication(sys.argv)
    window = FeatureApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()