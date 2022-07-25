from plistlib import UID
from PyQt5 import QtCore, QtGui, QtWidgets                                                                                                               
from window import *
import sys


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.showMaximized()
sys.exit(app.exec_())