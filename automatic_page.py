import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QCheckBox, QFrame, QHBoxLayout, QScrollArea, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QFont

# Import SecondWindow here
from PyQt5.QtCore import pyqtSignal

class MainWindow(QMainWindow):
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

        frame1_scroll = QScrollArea(rectangle)
        frame1_scroll.setGeometry(48, 155, 930, 280)  # Increased width to 930 pixels
        frame1_scroll.setStyleSheet("background-color: white;")

        scroll_content = QWidget(frame1_scroll)
        scroll_content.setGeometry(0, 0, 580, 303)  # Adjusted width to 580 pixels

        layout = QVBoxLayout(scroll_content)

        # Function to add parameter layout with spacer
        def add_parameter_layout(parameter_name, state="Off"):
            parameter_layout = QHBoxLayout()
            layout.addLayout(parameter_layout)

            text_label = QLabel(parameter_name, scroll_content)
            parameter_layout.addWidget(text_label)

            indicator_text = QLabel(state, scroll_content)
            parameter_layout.addWidget(indicator_text)

            # Square box to indicate state
            indicator = QLabel(scroll_content)
            indicator.setFixedSize(20, 20)  # Decreased size of the indicator box
            if state == "On":
                indicator.setStyleSheet("background-color: green; border: 1px solid black;")
            else:
                indicator.setStyleSheet("background-color: red; border: 1px solid black;")
            parameter_layout.addWidget(indicator)

            # Add spacer between each parameter
            spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            layout.addItem(spacer)

        # Add parameters
        parameters = ["FORWARD", "REVERSE", "RIGHT TURN", "LEFT TURN", "HIGH BEAM", 
                      "LOW BEAM", "WORKING LIGHT", "PTO", "BUZZER", "COOLING FAN", 
                      "TRACTION MOTOR", "PARKING INDICATOR"]
        
        for parameter in parameters:
            add_parameter_layout(parameter)

        frame1_scroll.setWidget(scroll_content)

        roundButton = QPushButton("BACK", rectangle)
        roundButton.setGeometry(50, 460, 125, 50)
        roundButton.setStyleSheet("background-color: #ffffff;")
        roundButton.clicked.connect(self.back_window)

        roundButton1 = QPushButton("NEXT", rectangle)
        roundButton1.setGeometry(850, 460, 125, 50)
        roundButton1.setStyleSheet("background-color: #ffffff;")
        roundButton1.clicked.connect(self.next_window)

    def open_mode(self):
        from mode_selection import SecondWindow 
        if not self.second_window:
            self.second_window = SecondWindow()  # Creating an instance of SecondWindow from mode_page
        self.second_window.show()
        self.hide()

    def back_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.back_window_signal.emit()

    def next_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.next_window_signal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())