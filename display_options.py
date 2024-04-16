import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton ,QHBoxLayout

from PyQt5.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    battery_window_signal = pyqtSignal()
    motor_window_signal = pyqtSignal()
    back_window_signal = pyqtSignal()
    next_window_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 1024, 600)
        self.second_window = None

        rectangle = QWidget(self)
        rectangle.setGeometry(0, 0, 1024, 600)
        rectangle.setStyleSheet("background-color: #87bba2")

        self.header = QWidget(rectangle)
        self.header.setGeometry(0, 0, 1024, 85)
        self.header.setStyleSheet("background-color: #ffffff;")

        self.logo = QLabel(self.header)
        self.logo.setGeometry(8, 8, 190, 69)
        pixmap = QPixmap("C:\\Users\\vedas\\OneDrive\\Desktop\\twintech\\logo.png")  # Replace with the actual path to your logo
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)

        self.title = QLabel(self.header)
        self.title.setGeometry(277, 26, 500, 35)
        self.title.setText("TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = QFont()
        font.setPixelSize(24)
        font.setBold(True)
        self.title.setFont(font)

        # Navigation Bar
        self.nav_bar = QWidget(rectangle)
        self.nav_bar.setGeometry(0, 85, 1024, 50)
        self.nav_bar.setStyleSheet("background-color: #c9e4ca;")  # Dark blue color

        files_label = QLabel("Files", self.nav_bar)
        settings_label = QLabel("Settings", self.nav_bar)

        nav_layout = QHBoxLayout(self.nav_bar)
        nav_layout.addWidget(files_label)
        nav_layout.addWidget(settings_label)
        nav_layout.addStretch(1)

        files_label.setGeometry(10, 0, 100, 20)
        settings_label.setGeometry(120, 0, 100, 20)

        files_label.setStyleSheet("color: black; font-size: 16px; padding: 2px;")
        settings_label.setStyleSheet("color: black; font-size: 16px; padding: 2px;")

         # Footer
        self.footer = QWidget(rectangle)
        self.footer.setGeometry(0, 554, 1024, 46)
        self.footer.setStyleSheet("background-color: #6A9C89;")

        self.footer_label = QLabel(self.footer)
        self.footer_label.setGeometry(0, 0, 1024, 40)
        self.footer_label.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        self.footer_label.setStyleSheet("color: black; font-size: 16px;")
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.second_window = None  # Initialize second_window attribute

        frame = QWidget(rectangle)
        frame.setGeometry(55, 135, 909, 364)

        button = QPushButton(frame)
        button.setGeometry(210, 111, 150, 70)
        button.setText("BATTERY")
        font = button.font()
        font.setPointSize(15)
        button.setStyleSheet("background-color: #C1D8C3;")
        button.setFont(font)
        button.clicked.connect(self.battery_window)

        button1 = QPushButton(frame)
        button1.setGeometry(540, 111, 150, 70)
        button1.setText("MOTOR")
        button1.setStyleSheet("background-color: #C1D8C3;")
        button1.setFont(font)
        button1.clicked.connect(self.motor_window)

        roundButton = QPushButton(frame)
        roundButton.setGeometry(5, 310, 150, 50)
        roundButton.setText("BACK")
        font = roundButton.font()
        font.setPointSize(12)
        roundButton.setFont(font)
        roundButton.setStyleSheet("background-color: #ffffff;")
        roundButton.clicked.connect(self.back_window)

        

    def back_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.back_window_signal.emit()

    def next_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.next_window_signal.emit()

    def battery_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.battery_window_signal.emit()

    def motor_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.motor_window_signal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
