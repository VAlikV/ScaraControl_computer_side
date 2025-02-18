import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,400,300)
    win.setWindowTitle("Pyqt5 Tutorial")
    win.show()
    sys.exit(app.exec_())
    
main()