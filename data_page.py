import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap, QFont, QColor 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QFrame
from PyQt5.QtCore import pyqtSignal

class MainWindow(QWidget):
    back_window_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Example")
        self.setGeometry(0, 0, 1024, 600)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        rectangle = QWidget(self)
        rectangle.setGeometry(0, 0, 1024, 600)
        rectangle.setStyleSheet("background-color: #87bba2")

        # Header Layout
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # Align to the left and top
        main_layout.addLayout(header_layout)

        # Logo
        logo_label = QLabel(self)
        pixmap = QPixmap("C:\\Users\\vedas\\OneDrive\\Desktop\\twintech\\logo.png")
        logo_label.setPixmap(pixmap.scaledToHeight(69))
        header_layout.addWidget(logo_label)

        # Header Rectangle
        header_rect = QWidget(rectangle)
        header_rect.setGeometry(0, 0, 1024, 85)
        header_rect.setStyleSheet("background-color: #ffffff")

        text1 = QLabel(header_rect)
        text1.setGeometry(257, 27, 511, 32)
        text1.setText("TWINTECH CONTROL SYSTEMS PVT. LTD.")
        font = text1.font()
        font.setPixelSize(24)
        font.setBold(True)
        text1.setFont(font)

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

         # Frames Layout
        frames_layout = QHBoxLayout()
        frames_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.addLayout(frames_layout)

        # Frame 1
        frame_1 = QFrame(self)
        frame_1.setStyleSheet("background-color: #ffffff;")
        frame_1.setGeometry(20, 100, 450, 400)
        frames_layout.addWidget(frame_1)

        layout_frame_1 = QVBoxLayout(frame_1)

        parameters_group_box_1 = [("PARAMETER 1:", "Text Field"), 
                                    ("PARAMETER 2:", "Text Field"), 
                                    ("PARAMETER 3:", "Text Field"), 
                                    ("PARAMETER 4:", "Text Field")]
        for parameter, placeholder in parameters_group_box_1:
            parameter_layout = QHBoxLayout()
            label = QLabel(parameter, self)
            text_field = QLineEdit(self)
            text_field.setPlaceholderText(placeholder)
            
            # Adjust size of text field
            text_field.setMaximumWidth(130)
            
            # Adjust layout margins to reduce spacing
            parameter_layout.setContentsMargins(0, 0, 0, 0)
            
            parameter_layout.addWidget(label)
            parameter_layout.addWidget(text_field)
            layout_frame_1.addLayout(parameter_layout)

         # Frame 2
        frame_2 = QFrame(self)
        frame_2.setStyleSheet("background-color: #ffffff;")
        frame_2.setGeometry(500, 100, 500, 400)
        frames_layout.addWidget(frame_2)

        layout_frame_2 = QVBoxLayout(frame_2)

        parameters_group_box_2 = [("PARAMETER 5:", "Text Field"), 
                                    ("PARAMETER 6:", "Text Field"), 
                                    ("PARAMETER 7:", "Text Field"), 
                                    ("PARAMETER 8:", "Text Field")]
        for parameter, placeholder in parameters_group_box_2:
            parameter_layout = QHBoxLayout()
            label = QLabel(parameter, self)
            text_field = QLineEdit(self)
            text_field.setPlaceholderText(placeholder)
            
            # Adjust size of text field
            text_field.setMaximumWidth(130)
            
            # Adjust layout margins to reduce spacing
            parameter_layout.setContentsMargins(0, 0, 0, 0)
            
            parameter_layout.addWidget(label)
            parameter_layout.addWidget(text_field)
            layout_frame_2.addLayout(parameter_layout)

        # Footer Layout
        footer_layout = QHBoxLayout()
        footer_layout.setContentsMargins(10, 10, 10, 10)
        footer_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(footer_layout)

        self.back_button = QPushButton("BACK", self)
        self.back_button.setStyleSheet("background-color: #ffffff; color: black;")
        self.back_button.setMinimumSize(160, 60)  # Increase button size
        self.back_button.setMaximumSize(160, 60)  # Increase button size
        self.back_button.clicked.connect(self.back_window)

        next_button = QPushButton("NEXT", self)
        next_button.setStyleSheet("background-color: #ffffff; color: black;")
        next_button.setMinimumSize(160, 60)  # Increase button size
        next_button.setMaximumSize(160, 60)  # Increase button size
        
        # Add spacer item
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        footer_layout.addWidget(self.back_button)
        footer_layout.addItem(spacer)
        footer_layout.addWidget(next_button)

        # Apply background color to main widget
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("#BED7DC"))
        self.setPalette(p)

         # Footer background rectangle
        self.footer_rect = QLabel(self)
        self.footer_rect.setStyleSheet("background-color: #6A9C89;")
        self.footer_rect.setGeometry(0, 550, 1064, 50)

        # Footer label
        self.label_footer = QLabel("© 2024 TWINTECH CONTROL SYSTEMS PVT. LTD.", self)
        self.label_footer.setGeometry(340, 560, 400, 30)
        self.label_footer.setStyleSheet("font-size: 16px; background-color: transparent;")

    def back_window(self):
        # Emit a signal to inform the MainApp to switch to the next window
        self.back_window_signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
