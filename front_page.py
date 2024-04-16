import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QFrame
from PyQt5.QtGui import QPixmap, QFont, QPainter, QBrush
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout

from mode_selection import SecondWindow

class RoundButton(QPushButton):
    def __init__(self, text, parent=None):
        super(RoundButton, self).__init__(text, parent)
        self.setFixedSize(129, 40)  # Adjust size as needed

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Draw rounded button
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(Qt.white))  # Change color as needed
        painter.drawRoundedRect(self.rect(), 10, 10)

        # Draw text
        painter.setPen(Qt.black)
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class MainWindow(QWidget):
    skip_window_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Generated from QML")
        self.setGeometry(0, 0, 1024, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Main Frame
        self.main_frame = QWidget()
        self.main_frame.setGeometry(0, 0, 1024, 600)
        self.main_frame.setStyleSheet("background-color: #87bba2;border: none;")
        self.layout.addWidget(self.main_frame)

        self.layout.setContentsMargins(0, 0, 0, 0)

        # Header Rectangle
        self.header = QWidget(self.main_frame)
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
        self.nav_bar = QWidget(self.main_frame)
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

        # Frame
        self.frame = QWidget(self.main_frame)
        self.frame.setGeometry(40, 140, 954, 386)

        self.customer_type_label = QLabel("Customer type :", self.frame)
        self.customer_type_label.setGeometry(90, 30, 126, 24)
        self.customer_type_combobox = QComboBox(self.frame)
        self.customer_type_combobox.setStyleSheet("border: 1px solid white;")
        self.customer_type_combobox.setStyleSheet("background-color: white; border: 1px solid white;")
        self.customer_type_combobox.setGeometry(240, 22, 165, 40)
        self.customer_type_combobox.addItem("New Customer")
        self.customer_type_combobox.addItem("Existing Customer")

        self.part_number_label = QLabel("Part Number :", self.frame)
        self.part_number_label.setGeometry(90, 118, 120, 21)
        self.part_number_combobox = QComboBox(self.frame)
        self.part_number_combobox.setStyleSheet("background-color: white; border: 1px solid white;")
        self.part_number_combobox.setGeometry(240, 109, 165, 40)
        self.part_number_combobox.addItem("1234")
        self.part_number_combobox.addItem("1603")
        self.part_number_combobox.addItem("1213")
        self.part_number_combobox.addItem("3026")

        self.serial_number_label = QLabel("Serial Number :", self.frame)
        self.serial_number_label.setGeometry(90, 208, 126, 21)
        self.serial_number_textfield = QLineEdit(self.frame)
        self.serial_number_textfield.setStyleSheet("background-color: white; border: 1px solid white;")
        self.serial_number_textfield.setGeometry(240, 199, 165, 40)

        self.customer_id_label = QLabel("Customer ID :", self.frame)
        self.customer_id_label.setGeometry(550, 34, 115, 20)
        self.customer_id_textfield = QLineEdit(self.frame)
        self.customer_id_textfield.setStyleSheet("background-color: white; border: 1px solid white;")
        self.customer_id_textfield.setGeometry(670, 22, 165, 40)

        self.checked_by_label = QLabel("Checked By :", self.frame)
        self.checked_by_label.setGeometry(550, 123, 115, 26)
        self.checked_by_textfield = QLineEdit(self.frame)
        self.checked_by_textfield.setStyleSheet("background-color: white; border: 1px solid white;")
        self.checked_by_textfield.setGeometry(670, 109, 165, 40)

        current_date = QDate.currentDate()
        current_date_string = current_date.toString(Qt.ISODate)
        self.date_label = QLabel("Date : " + current_date_string, self.frame)
        self.date_label.setGeometry(550, 207, 200, 24)

        self.skip_button = RoundButton("SKIP", self.frame)
        self.skip_button.setGeometry(10, 345, 129, 40)
        self.skip_button.setStyleSheet("background-color: #ffffff;")

        self.submit_button = RoundButton("SUBMIT", self.frame)
        self.submit_button.setGeometry(400, 345, 129, 40)
        self.submit_button.setStyleSheet("background-color: #ffffff;")
        self.submit_button.clicked.connect(self.submit_action)

        self.next_button = RoundButton("NEXT", self.frame)
        self.next_button.setGeometry(810, 345, 122, 40)
        self.next_button.setStyleSheet("background-color: #ffffff;")

        self.footer = QWidget(self.main_frame)
        self.footer.setGeometry(0, 554, 1024, 46)
        self.footer.setStyleSheet("background-color: #6A9C89;")

        self.footer_label = QLabel(self.footer)
        self.footer_label.setGeometry(0, 0, 1024, 40)
        self.footer_label.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        self.footer_label.setStyleSheet("color: black; font-size: 16px;")
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.second_window = None

    def open_mode(self):
        if not self.second_window:
            self.second_window = SecondWindow()
        self.second_window.show()
        self.hide()

    def skip_window(self):
        self.skip_window_signal.emit()

    def submit_action(self):
        print("Submit button clicked")

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
