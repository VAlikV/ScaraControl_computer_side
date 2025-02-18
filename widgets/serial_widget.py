from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QByteArray

class SerialWidget(QWidget):

    port_opened = pyqtSignal()
    port_closed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()
        
        self.comport = QComboBox(self)
        self.layout.addWidget(self.comport)

        # =======================================================
        
        self.refresh_button = QPushButton("Refresh", self)
        self.layout.addWidget(self.refresh_button)

        self.connect_button = QPushButton("Connect", self)
        self.layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton("Disconnect", self)
        self.layout.addWidget(self.disconnect_button)
        
        self.setLayout(self.layout)

        # =======================================================  

        self.serial = QSerialPort()   
        self.refreshPorts()
        self.disconnect_button.setEnabled(False)

        self.setConnections()

# -------------------------------------------------------------------------

    def setConnections(self):
        self.refresh_button.clicked.connect(self.refreshPorts)
        self.connect_button.clicked.connect(self.openPort)
        self.disconnect_button.clicked.connect(self.closePort)

# -------------------------------------------------------------------------

    @pyqtSlot()
    def refreshPorts(self):
        self.comport.clear()
        my_ports = QSerialPortInfo()
        ports = my_ports.availablePorts()
        for port in ports:
            self.comport.addItem(port.portName())

# -------------------------------------------------------------------------

    @pyqtSlot()
    def openPort(self):
        if self.comport.count() != 0:
            self.serial.setPortName(self.comport.currentText())
            self.serial.setBaudRate(QSerialPort.BaudRate.Baud115200)
            self.serial.setDataBits(QSerialPort.DataBits.Data8)
            self.serial.setParity(QSerialPort.Parity.NoParity)
            self.serial.setStopBits(QSerialPort.StopBits.OneStop)
            self.serial.setFlowControl(QSerialPort.FlowControl.NoFlowControl)

            if self.serial.open(QSerialPort.OpenModeFlag.ReadWrite):
                self.comport.setEnabled(False)
                self.refresh_button.setEnabled(False)
                self.connect_button.setEnabled(False)
                self.disconnect_button.setEnabled(True)
                self.port_opened.emit()

# -------------------------------------------------------------------------

    @pyqtSlot()
    def closePort(self):
        if self.serial.isOpen():
            self.serial.close()
            self.comport.setEnabled(True)
            self.refresh_button.setEnabled(True)
            self.connect_button.setEnabled(True)
            self.disconnect_button.setEnabled(False)
            self.port_closed.emit()

# -------------------------------------------------------------------------

    @pyqtSlot(str)
    def send(self, msg):
        if self.serial.isOpen():
            self.serial.write(QByteArray(msg.encode('utf-8')))
