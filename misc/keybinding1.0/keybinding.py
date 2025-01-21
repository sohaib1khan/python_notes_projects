import sys
import pyperclip
import time
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget
)
from PyQt5.QtCore import QTimer

# Function to install missing modules
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["PyQt5", "pyperclip"]

# Install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing missing package: {package}")
        install(package)

class RDPHelperApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RDP Helper App")
        self.setGeometry(100, 100, 600, 400)
        
        # Main widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()

        # Predefined Text
        self.predefined_text = "This is the predefined text!"
        self.predefined_label = QLabel("Predefined Text:")
        self.predefined_display = QTextEdit()
        self.predefined_display.setText(self.predefined_text)
        self.predefined_display.setReadOnly(True)

        # Copy Predefined Text Button
        self.copy_predefined_btn = QPushButton("Copy Predefined Text")
        self.copy_predefined_btn.clicked.connect(self.copy_predefined_text)

        # Live Copy Section
        self.live_copy_label = QLabel("Live Copied Text:")
        self.live_copy_display = QTextEdit()
        self.live_copy_display.setReadOnly(True)

        # Copy and Paste Live Text Button
        self.copy_paste_live_btn = QPushButton("Copy & Paste Live Text")
        self.copy_paste_live_btn.clicked.connect(self.copy_and_paste_live_text)

        # Exit Button
        self.exit_btn = QPushButton("Exit Application")
        self.exit_btn.clicked.connect(self.close)

        # Add widgets to layout
        self.layout.addWidget(self.predefined_label)
        self.layout.addWidget(self.predefined_display)
        self.layout.addWidget(self.copy_predefined_btn)
        self.layout.addWidget(self.live_copy_label)
        self.layout.addWidget(self.live_copy_display)
        self.layout.addWidget(self.copy_paste_live_btn)
        self.layout.addWidget(self.exit_btn)

        # Apply layout
        self.central_widget.setLayout(self.layout)

        # Timer for aggressive pasting
        self.paste_timer = QTimer()
        self.paste_timer.timeout.connect(self.perform_aggressive_paste)

    def copy_predefined_text(self):
        """Copy predefined text to clipboard."""
        pyperclip.copy(self.predefined_text)
        self.show_status("Predefined text copied!")

    def copy_and_paste_live_text(self):
        """Copy live text and aggressively paste it."""
        pyperclip.copy("")  # Clear clipboard
        time.sleep(0.5)  # Ensure clipboard updates
        pyperclip.copy("Live text from clipboard")  # Simulated live copy
        self.live_copy_display.setText(pyperclip.paste())
        self.show_status("Live text copied! Aggressively pasting...")
        
        # Start aggressive pasting
        self.paste_attempts = 0
        self.paste_timer.start(500)  # 500ms interval

    def perform_aggressive_paste(self):
        """Perform aggressive pasting for RDP reliability."""
        if self.paste_attempts < 5:
            pyperclip.copy(pyperclip.paste())  # Refresh clipboard content
            self.paste_attempts += 1
        else:
            self.paste_timer.stop()
            self.show_status("Aggressive pasting completed!")

    def show_status(self, message):
        """Display a status message."""
        self.statusBar().showMessage(message, 3000)  # Show for 3 seconds

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set application stylesheet for a calm theme
    app.setStyleSheet("""
        QWidget {
            background-color: #f5f5f5;
            color: #333;
            font-family: Arial;
            font-size: 14px;
        }
        QPushButton {
            background-color: #d1e7dd;
            border: 1px solid #badbcc;
            padding: 5px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #b6dfc3;
        }
        QTextEdit {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 5px;
            border-radius: 5px;
        }
        QLabel {
            font-weight: bold;
        }
    """)

    window = RDPHelperApp()
    window.show()

    sys.exit(app.exec_())
