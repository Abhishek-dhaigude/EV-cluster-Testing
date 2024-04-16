import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFrame, QDialog, QLineEdit, QVBoxLayout, QHBoxLayout ,QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    back_window_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt App")
        self.setGeometry(100, 100, 1024, 600)

        # Background color for the central widget
        self.central_widget = QLabel(self)
        self.central_widget.setStyleSheet("background-color: #87bba2;")
        self.central_widget.resize(1024, 600)

        self.header = QWidget(self.central_widget)
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
        self.nav_bar = QWidget(self.central_widget)
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
        self.footer = QWidget(self.central_widget)
        self.footer.setGeometry(0, 554, 1024, 46)
        self.footer.setStyleSheet("background-color: #6A9C89;")

        self.footer_label = QLabel(self.footer)
        self.footer_label.setGeometry(0, 0, 1024, 40)
        self.footer_label.setText("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.")
        self.footer_label.setStyleSheet("color: black; font-size: 16px;")
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.second_window = None  # Initialize second_window attribute

        # Frame 1
        self.frame_1 = QFrame(self.central_widget)
        self.frame_1.setGeometry(20, 150, 450, 270)
        self.frame_1.setStyleSheet("background-color: #87bba2; border: 1px solid black;")

        self.button_view_report = QPushButton("VIEW REPORT", self.frame_1)
        self.button_view_report.setGeometry(120, 90, 220, 80)
        self.button_view_report.setStyleSheet("background-color: #ffffff;")  # Set background color to white

        # Frame 2
        self.frame_2 = QFrame(self.central_widget)
        self.frame_2.setGeometry(500, 150, 500, 270)
        self.frame_2.setStyleSheet("background-color: #87bba2; border: 1px solid black;")

        self.label_email = QLabel("E-MAIL ID :", self.frame_2)
        self.label_email.setGeometry(40, 50, 100, 30)

        self.textfield_email = QLineEdit(self.frame_2)
        self.textfield_email.setGeometry(40, 90, 370, 40)
        self.textfield_email.setStyleSheet("background-color: #ffffff;")  # Set background color to white
        self.textfield_email.setPlaceholderText("ENTER YOUR E-MAIL ID")

        self.button_export_report = QPushButton("EXPORT REPORT", self.frame_2)
        self.button_export_report.setGeometry(120, 150, 220, 80)
        self.button_export_report.setStyleSheet("background-color: #ffffff;")  # Set background color to white

       

        # Back, Save, and Finish buttons
        self.button_back = QPushButton("BACK", self.central_widget)
        self.button_back.setGeometry(20, 450, 160, 60)
        self.button_back.setStyleSheet("background-color: #ffffff;font-size: 18px;")  # Set background color to white
        self.button_back.clicked.connect(self.back_window)

        self.button_save = QPushButton("SAVE", self.central_widget)
        self.button_save.setGeometry(410, 450, 160, 60)
        self.button_save.setStyleSheet("background-color: #ffffff;font-size: 18px;")  # Set background color to white
        self.button_save.clicked.connect(self.save_report)

        self.button_finish = QPushButton("FINISH", self.central_widget)
        self.button_finish.setGeometry(840, 450, 160, 60)
        self.button_finish.setStyleSheet("background-color: #ffffff;font-size: 18px;")
        self.button_finish.clicked.connect(self.show_thank_you_popup)

        self.show()

    def back_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.back_window_signal.emit()
    
    def save_report(self):
        print("Save button clicked")
        # Implement save functionality here
    
    def show_thank_you_popup(self):
        print("Showing Thank You popup")
        popup = ThankYouPopup()
        popup.exec_()

class ThankYouPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thank You")
        self.setGeometry(400, 200, 300, 100)
        layout = QVBoxLayout()
        label = QLabel("Thank you!")
        layout.addWidget(label)
        self.setLayout(layout)   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
