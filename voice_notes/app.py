"""
Voice Notes Application Core
"""
import sys
from PyQt6.QtWidgets import QApplication
from .ui.main_window import MainWindow
from .styles.theme import LIQUID_QSS
from .utils.platform import apply_window_vibrancy
from PyQt6.QtGui import QIcon
import os

APP_NAME = "Voice Notes"

class VoiceNotesApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setApplicationName(APP_NAME)
        icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.png")
        self.app.setWindowIcon(QIcon(icon_path))
        self.app.setStyleSheet(LIQUID_QSS)
        
        self.main_window = MainWindow()
    
    def run(self):
        self.main_window.show()
        apply_window_vibrancy(self.main_window)
        return self.app.exec()

def main():
    app = VoiceNotesApp()
    sys.exit(app.run())

if __name__ == "__main__":
    main()