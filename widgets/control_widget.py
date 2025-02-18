from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class ControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QHBoxLayout()
        self.control_layout = QGridLayout()
        # self.file_layout = QHBoxLayout()
        # self.point_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()

        # =======================================================

        self.file_label = QLabel("File: ",self)
        self.file_edit = QLineEdit(self)
        self.file_button = QPushButton("Sent")
        self.control_layout.addWidget(self.file_label,0,0)
        self.control_layout.addWidget(self.file_edit,0,1)
        self.control_layout.addWidget(self.file_button,0,2)

        # =======================================================
        
        self.point_label = QLabel("Point: ",self)
        self.point_edit = QLineEdit(self)
        self.point_button = QPushButton("Sent")
        self.control_layout.addWidget(self.point_label,1,0)
        self.control_layout.addWidget(self.point_edit,1,1)
        self.control_layout.addWidget(self.point_button,1,2)
    
        # =======================================================

        self.start_button = QPushButton("START", self)
        # self.refresh_button.clicked.connect(self.print_text)
        self.button_layout.addWidget(self.start_button)

        # =======================================================

        self.stop_button = QPushButton("STOP", self)
        # self.refresh_button.clicked.connect(self.print_text)
        self.button_layout.addWidget(self.stop_button)

        # =======================================================

        self.layout.addLayout(self.control_layout)
        self.layout.addSpacing(30)
        self.layout.addLayout(self.button_layout)

        # =======================================================
        
        self.setLayout(self.layout)
    
    def print_text(self):
        print(self.input_field.text())