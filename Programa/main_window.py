# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets
from map_painter import MapPainter
from core import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1011, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("test_map.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.mouseReleaseEvent = self.mouseReleased

        #Aquest codi d'aqui crea els elements necessaris per a crear
        #un graf. Pots indicar el tipus de graf (simple o dirigit) i
        #assignar un pes a l'aresta
        #"""
        self.cb = QtWidgets.QComboBox(self.centralwidget)
        self.cb.setGeometry(QtCore.QRect(1040, 24, 75, 23))
        self.cb.addItems(["Simple", "Dirigit"])

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1040, 0, 75, 23))
        self.textEdit.setObjectName("textEdit")
        #"""

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.event

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.map_painter = MapPainter("test_map.png")

        #FIXME: TEMPORARY
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)        

        self.firstBtn = 0
        self.firstClick = True

        self.g = Graph()
        self.g_val = list(self.g.vertex_coord.values())
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    #Aquesta funció et permet marcar les interseccions (vertex del graf) al mapa
    #i ho escriu a un archiu .csv per a que després el programa 'metaprogram.py'
    #et doni el codi per els botons i les seves funcions. Aquests t'ajudaran a indicar
    #arestes i els seus pesos
    def mouseReleased(self, QMouseEvent):
        """
        f = open("vertexs.csv", "a")
        f.write(f"{QMouseEvent.x()},{QMouseEvent.y()}\n")
        f.close()

        p = MapPainter('test_map.png')
        p.paint_points(pos=(QMouseEvent.x(),QMouseEvent.y()),r=10)
        self.label.setPixmap(QtGui.QPixmap("test_map.png"))
        """
        #"""
        pass
