import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton ,QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QPainter, QBrush
from manual_page import MainWindow as Manual_window
from automatic_page import MainWindow as Auto_window
from display_options import MainWindow as Display_window

from PyQt5.QtCore import pyqtSignal
 
class SecondWindow(QMainWindow):
    auto_window_signal = pyqtSignal()
    manual_window_signal = pyqtSignal()
    display_window_signal = pyqtSignal()
    back_window_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 1024, 600)

        # Initialize attributes for different modes
        self.auto_page = None
        self.manual_page = None
        self.display_page = None
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
        frame.setGeometry(38, 140, 944, 384)

        button = QPushButton(frame)
        button.setGeometry(66, 97, 165, 77)
        button.setText("AUTOMATIC")
        font = button.font()
        font.setPointSize(15)
        button.setFont(font)
        button.setStyleSheet("background-color: #C1D8C3;")
        button.clicked.connect(self.auto_window)


        button1 = QPushButton(frame)
        button1.setGeometry(378, 97, 165, 77)
        button1.setText("MANUAL")
        button1.setFont(font)
        button1.setStyleSheet("background-color: #C1D8C3;")
        button1.clicked.connect(self.manual_window)

        button2 = QPushButton(frame)
        button2.setGeometry(694, 97, 165, 77)
        button2.setText("DISPLAY")
        button2.setFont(font)
        button2.setStyleSheet("background-color: #C1D8C3;")
        button2.clicked.connect(self.display_window)

        roundButton = QPushButton(frame)
        roundButton.setGeometry(10, 330, 125, 50)
        roundButton.setText("BACK")
        font = roundButton.font()
        font.setPointSize(12)
        roundButton.setFont(font)
        roundButton.setStyleSheet("background-color: #ffffff;")
        roundButton.clicked.connect(self.back_window)

        

    def auto_mode(self):
        if not self.auto_page:
            self.auto_page = Auto_window()  # Creating an instance of Auto_window from automatic_page
        self.auto_page.show()
        self.hide()

    def manual_mode(self):
        if not self.manual_page:
            self.manual_page = Manual_window()  # Creating an instance of Manual_window from manual_page
        self.manual_page.show()
        self.hide()

    def display_mode(self):
        if not self.display_page:
            self.display_page = Display_window()  # Creating an instance of Display_window from display_options
        self.display_page.show()
        #self.hide()

    def open_mode(self):
        from front_page import MainWindow 
        if not self.second_window:
            self.second_window = MainWindow()  # Creating an instance of SecondWindow from mode_page
        self.second_window.show()
        self.hide()

    def auto_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.auto_window_signal.emit()

    def manual_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.manual_window_signal.emit()

    def display_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.display_window_signal.emit()

    def back_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.back_window_signal.emit()

    def handle_files_button(self):
        print("Files button clicked")
        # Add your code to handle the "Files" button action here

    def handle_settings_button(self):
        print("Settings button clicked")
        # Add your code to handle the "Settings" button action here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SecondWindow()  # Create an instance of SecondWindow
    window.show()
    sys.exit(app.exec_())
