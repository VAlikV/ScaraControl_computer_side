from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QByteArray

class ControlWidget(QWidget):

    point_send = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        
        self.layout = QHBoxLayout()
        self.control_layout = QGridLayout()
        self.button_layout = QHBoxLayout()

        # =======================================================

        self.file_label = QLabel("File: ",self)
        self.file_edit = QLineEdit(self)
        self.file_edit.setPlaceholderText("file.txt")
        self.file_button = QPushButton("Send")

        self.control_layout.addWidget(self.file_label,0,0)
        self.control_layout.addWidget(self.file_edit,0,1)
        self.control_layout.addWidget(self.file_button,0,2)

        # =======================================================
        
        self.point_label = QLabel("Point: ",self)
        self.point_edit = QLineEdit(self)
        self.point_edit.setPlaceholderText("aa bb cc")
        self.point_button = QPushButton("Send")

        self.control_layout.addWidget(self.point_label,1,0)
        self.control_layout.addWidget(self.point_edit,1,1)
        self.control_layout.addWidget(self.point_button,1,2)
    
        # =======================================================

        self.start_button = QPushButton("START", self)
        self.start_button.setFixedSize(100, 80)
        self.button_layout.addWidget(self.start_button)

        # =======================================================

        self.stop_button = QPushButton("STOP", self)
        self.stop_button.setFixedSize(100, 80)
        self.button_layout.addWidget(self.stop_button)

        # =======================================================

        self.layout.addLayout(self.control_layout)
        self.layout.addSpacing(30)
        self.layout.addLayout(self.button_layout)

        # =======================================================
        
        self.setLayout(self.layout)

        self.closePort()

        self.setConnection()

# -------------------------------------------------------------------------

    def setConnection(self):
        self.point_button.clicked.connect(self.sendPoint)
        self.file_button.clicked.connect(self.sendFile)
        self.start_button.clicked.connect(self.sendStart)
        self.stop_button.clicked.connect(self.sendStop)

# -------------------------------------------------------------------------

    @pyqtSlot()
    def sendStart(self):
        self.point_send.emit("START")

# -------------------------------------------------------------------------

    @pyqtSlot()
    def sendStop(self):
        self.point_send.emit("STOP")


# -------------------------------------------------------------------------

    @pyqtSlot()
    def sendFile(self):
        file = open(self.file_edit.text(), 'r')
        self.point_send.emit("begin")
        for point in file:
            # print(line)
            self.point_send.emit(point)
        self.point_send.emit("end")
        file.close()

# -------------------------------------------------------------------------

    @pyqtSlot()
    def sendPoint(self):
        point = self.point_edit.text()
        self.point_send.emit("begin")
        self.point_send.emit(point)
        self.point_send.emit("end")

# -------------------------------------------------------------------------

    @pyqtSlot()
    def openPort(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.file_button.setEnabled(True)
        self.point_button.setEnabled(True)

# -------------------------------------------------------------------------

    @pyqtSlot()
    def closePort(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.file_button.setEnabled(False)
        self.point_button.setEnabled(False)