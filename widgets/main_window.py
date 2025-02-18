from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
from widgets.serial_widget import SerialWidget
from widgets.control_widget import ControlWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Scara Control by 431Group")
        # self.setGeometry(100, 100, 300, 150)
        
        self.layout = QHBoxLayout()

        self.serial = SerialWidget()
        self.control = ControlWidget()

        self.layout.addWidget(self.serial)
        self.layout.addWidget(self.control)
        
        self.setLayout(self.layout)
    
    def print_text(self):
        print(self.input_field.text())
        