from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
# from PyQt5.QtSerialPort import QSerialPort

from widgets.serial_widget import SerialWidget
from widgets.control_widget import ControlWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # =======================================================
        
        self.setWindowTitle("Scara Control by 431Group")
        
        self.layout = QHBoxLayout()

        self.serial = SerialWidget()
        self.control = ControlWidget()

        self.layout.addWidget(self.serial)
        self.layout.addWidget(self.control)
        
        self.setLayout(self.layout)

        # =======================================================

        self.setConnectoins()
    
# -------------------------------------------------------------------------

    def setConnectoins(self):
        self.serial.port_opened.connect(self.control.openPort)
        self.serial.port_closed.connect(self.control.closePort)
        self.control.point_send.connect(self.serial.send)

        