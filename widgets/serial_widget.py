from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton

class SerialWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()
        
        self.comport = QComboBox(self)
        self.layout.addWidget(self.comport)
        
        self.refresh_button = QPushButton("Refresh", self)
        # self.refresh_button.clicked.connect(self.print_text)
        self.layout.addWidget(self.refresh_button)

        self.connect_button = QPushButton("Connect", self)
        # self.refresh_button.clicked.connect(self.print_text)
        self.layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton("Disconnect", self)
        # self.refresh_button.clicked.connect(self.print_text)
        self.layout.addWidget(self.disconnect_button)
        
        self.setLayout(self.layout)
    
    def print_text(self):
        print(self.input_field.text())