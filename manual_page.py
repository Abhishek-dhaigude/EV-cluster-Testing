import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QFrame, QScrollArea, QHBoxLayout, QLineEdit, QCheckBox
from PyQt5.QtGui import QPixmap, QFont

class CustomCheckBoxLineEdit(QWidget):
    def __init__(self, text):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.checkbox = QCheckBox()
        self.checkbox.setChecked(True)  # Set default state
        layout.addWidget(self.checkbox)

        self.line_edit = QLineEdit()
        self.line_edit.setText(text)
        layout.addWidget(self.line_edit)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    back_window_signal = pyqtSignal()
    next_window_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.second_window = None  # Initialize second_window attribute

        self.setWindowTitle("PyQt Example")
        self.setGeometry(100, 100, 1024, 600)

        rectangle = QWidget(self)
        rectangle.setGeometry(0, 0, 1024, 600)
        rectangle.setStyleSheet("background-color: #87bba2")

        self.header = QWidget(rectangle)
        self.header.setGeometry(0, 0, 1024, 85)
        self.header.setStyleSheet("background-color: #ffffff;")

        self.logo = QLabel(self.header)
        self.logo.setGeometry(8, 8, 190, 69)
        pixmap = QPixmap("C:\\Users\\vedas\\OneDrive\\Desktop\\twintech\\logo.png")
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

        self.footer = QWidget(rectangle)
        self.footer.setGeometry(0, 554, 1024, 46)
        self.footer.setStyleSheet("background-color: #6A9C89;")

        self.footer_label = QLabel(self.footer)
        self.footer_label.setGeometry(0, 0, 1024, 40)
        self.footer_label.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        self.footer_label.setStyleSheet("color: black; font-size: 16px;")
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.second_window = None  # Initialize second_window attribute

        scroll_area1 = QScrollArea(rectangle)
        scroll_area1.setGeometry(49, 150, 422, 300)
        scroll_area1.setStyleSheet("background-color: #ffffff; border: none;")
        scroll_area1.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        frame1 = QFrame()
        frame1.setStyleSheet("background-color: #ffffff;")
        frame1.setFrameShape(QFrame.Shape.StyledPanel)

        layout1 = QVBoxLayout(frame1)
        layout1.setSpacing(20)

        heading1 = QLabel("Parameters", frame1)
        heading1.setStyleSheet("font-size: 14px; font-weight: bold;text-align: center;")
        heading1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout1.addWidget(heading1)

        text_input_data = [
            "FORWARD:  ",
            "REVERSE :  ",
            "RIGHT TURN : ",
            "LEFT TURN: ",
            "HIGH BEAM: ",
            "LOW BEAM: ",
            "WORKING LIGHT INDICATOR: ",
            "PTO: ",
            "PARKING INDICATOR: ",
            "HAND BRAKE: ",
            "BUZZER: ",
            "COOLING FAN: ",
            "TRACTION MOTOR CONTRACTOR: "
        ]

        for data in text_input_data:
            custom_widget = CustomCheckBoxLineEdit(data)
            layout1.addWidget(custom_widget)

        button = QPushButton("RUN TEST", frame1)
        button.setGeometry(275, 240, 115, 50)
        button.setStyleSheet("background-color: #C1D8C3;")

        scroll_area1.setWidget(frame1)
        scroll_area1.setWidgetResizable(True)

        scroll_area2 = QScrollArea(rectangle)
        scroll_area2.setGeometry(549, 150, 412, 300)
        scroll_area2.setStyleSheet("background-color: #ffffff; border: none;")
        scroll_area2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        frame2 = QFrame()
        frame2.setStyleSheet("background-color: #ffffff;")
        frame2.setFrameShape(QFrame.Shape.StyledPanel)

        layout2 = QVBoxLayout(frame2)

        heading2 = QLabel("Results", frame2)
        heading2.setStyleSheet("font-size: 14px; font-weight: bold;text-align: center;")
        heading2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout2.addWidget(heading2)

        page = QWidget()
        page_layout = QVBoxLayout(page)

        text_input_data = [
            "FORWARD:  running",
            "REVERSE :  running",
            "RIGHT TURN : running",
            "LEFT TURN: running",
            "HIGH BEAM: running",
            "LOW BEAM: running",
            "WORKING LIGHT INDICATOR: running",
            "PTO: running",
            "PARKING INDICATOR: running",
            "HAND BRAKE: running",
            "BUZZER: running",
            "COOLING FAN: running",
            "TRACTION MOTOR CONTRACTOR: running"
        ]

        for data in text_input_data:
            text_input = QLineEdit(page)
            text_input.setText(data)
            text_input.setStyleSheet("background-color: white;")
            font = text_input.font()
            font.setPixelSize(12)
            text_input.setFont(font)
            page_layout.addWidget(text_input)
            page_layout.addSpacing(10) 

        page.setLayout(page_layout)
        layout2.addWidget(page)

        scroll_area2.setWidget(frame2)
        scroll_area2.setWidgetResizable(True)

        button1 = QPushButton("BACK", rectangle)
        button1.setGeometry(50, 465, 125, 50)
        button1.setStyleSheet("background-color: #ffffff;")
        button1.clicked.connect(self.back_window)

        button2 = QPushButton("NEXT", rectangle)
        button2.setGeometry(850, 465, 125, 50)
        button2.setStyleSheet("background-color: #ffffff;")
        button2.clicked.connect(self.next_window)

    def back_window(self):
        self.back_window_signal.emit()

    def next_window(self):
        self.next_window_signal.emit()

    def open_mode(self):
        from mode_selection import SecondWindow 
        if not self.second_window:
            self.second_window = SecondWindow()  # Creating an instance of SecondWindow from mode_page
        self.second_window.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
