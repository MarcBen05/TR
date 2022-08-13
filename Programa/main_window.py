# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from map_painter import MapPainter
from core import *
import os

client_path = os.path.dirname(os.path.realpath(__file__))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1182, 748)
        MainWindow.setMinimumSize(QtCore.QSize(1182, 748))
        MainWindow.setMaximumSize(QtCore.QSize(1182, 748))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mapa = QtWidgets.QLabel(self.centralwidget)
        self.mapa.setGeometry(QtCore.QRect(0, -10, 1011, 751))
        self.mapa.setStyleSheet("border-style:solid;\n"
"border-width:1.5px;\n"
"border-color:rgb(176, 176, 176)")
        self.mapa.setText("")
        self.mapa.setPixmap(QtGui.QPixmap(str(client_path)+"\\assets\\map.png"))
        self.mapa.setScaledContents(True)
        self.mapa.setObjectName("mapa")
        self.mapa_peque = QtWidgets.QLabel(self.centralwidget)
        self.mapa_peque.setGeometry(QtCore.QRect(1030, 540, 131, 101))
        self.mapa_peque.setText("")
        self.mapa_peque.setPixmap(QtGui.QPixmap(str(client_path)+"\\assets\\undraw_map_dark_re_36sy.svg"))
        self.mapa_peque.setScaledContents(True)
        self.mapa_peque.setObjectName("mapa_peque")
        self.modeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.modeComboBox.setGeometry(QtCore.QRect(1100, 220, 69, 22))
        self.modeComboBox.setObjectName("modeComboBox")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeLabel = QtWidgets.QLabel(self.centralwidget)
        self.modeLabel.setGeometry(QtCore.QRect(1030, 220, 47, 20))
        self.modeLabel.setObjectName("modeLabel")
        self.originCoord = QtWidgets.QLabel(self.centralwidget)
        self.originCoord.setGeometry(QtCore.QRect(1030, 270, 101, 51))
        self.originCoord.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-style:solid;\n"
"border-color:rgb(176, 176, 176);\n"
"border-width:1px;\n"
"padding:2px")
        self.originCoord.setText("")
        self.originCoord.setObjectName("originCoord")
        self.originLabel = QtWidgets.QLabel(self.centralwidget)
        self.originLabel.setGeometry(QtCore.QRect(1030, 250, 47, 13))
        self.originLabel.setObjectName("originLabel")
        self.originButton = QtWidgets.QPushButton(self.centralwidget)
        self.originButton.setGeometry(QtCore.QRect(1140, 280, 31, 31))
        self.originButton.setStyleSheet("")
        self.originButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str(client_path)+"\\assets\\marcar_localitzacio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.originButton.setIcon(icon)
        self.originButton.setObjectName("originButton")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(1040, 20, 111, 111))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(str(client_path)+"\\assets\\logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(1040, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nombre.setFont(font)
        self.nombre.setStyleSheet("color:rgb(28, 85, 255)")
        self.nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.nombre.setObjectName("nombre")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(1010, 330, 171, 191))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.goalCoord = QtWidgets.QLabel(self.page)
        self.goalCoord.setGeometry(QtCore.QRect(20, 30, 101, 50))
        self.goalCoord.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-style:solid;\n"
"border-color:rgb(176, 176, 176);\n"
"border-width:1px;\n"
"padding:2px")
        self.goalCoord.setText("")
        self.goalCoord.setObjectName("goalCoord")
        self.goalButton = QtWidgets.QPushButton(self.page)
        self.goalButton.setGeometry(QtCore.QRect(130, 40, 31, 31))
        self.goalButton.setText("")
        self.goalButton.setIcon(icon)
        self.goalButton.setObjectName("goalButton")
        self.calcularButton = QtWidgets.QPushButton(self.page)
        self.calcularButton.setGeometry(QtCore.QRect(20, 110, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.calcularButton.setFont(font)
        self.calcularButton.setObjectName("calcularButton")
        self.goalLabel = QtWidgets.QLabel(self.page)
        self.goalLabel.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.goalLabel.setObjectName("goalLabel")
        self.netejaButton = QtWidgets.QPushButton(self.page)
        self.netejaButton.setGeometry(QtCore.QRect(20, 150, 111, 23))
        self.netejaButton.setObjectName("netejaButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.caractComboBox = QtWidgets.QComboBox(self.page_2)
        self.caractComboBox.setGeometry(QtCore.QRect(20, 40, 111, 22))
        self.caractComboBox.setObjectName("caractComboBox")
        self.caractComboBox.addItem("")
        self.caractComboBox.addItem("")
        self.caractComboBox.addItem("")
        self.caractLabel = QtWidgets.QLabel(self.page_2)
        self.caractLabel.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.caractLabel.setObjectName("caractLabel")
        self.rutaButton = QtWidgets.QPushButton(self.page_2)
        self.rutaButton.setGeometry(QtCore.QRect(20, 80, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rutaButton.setFont(font)
        self.rutaButton.setObjectName("rutaButton")
        self.netejaButton2 = QtWidgets.QPushButton(self.page_2)
        self.netejaButton2.setGeometry(QtCore.QRect(20, 120, 111, 23))
        self.netejaButton2.setObjectName("netejaButton2")
        self.stackedWidget.addWidget(self.page_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1030, 650, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(150, 150, 150)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ### Widgets added by user
                #Indicador per al desti
        self.pinLabel = QtWidgets.QLabel(self.centralwidget)
        self.pinLabel.setScaledContents(True)
        self.pinLabel.setGeometry(QtCore.QRect(0,0,16,26))
        self.pinLabel.setText("")
        self.pinLabel.setObjectName("pinLabel")
        self.pinLabel.setPixmap(QtGui.QPixmap(str(client_path)+"\\assets\\marcador.png"))
        self.pinLabel.hide()

        #Indicador per a l'origen
        self.circleLabel = QtWidgets.QLabel(self.centralwidget)
        self.circleLabel.setScaledContents(True)
        self.circleLabel.setGeometry(QtCore.QRect(0,0,16,16))
        self.circleLabel.setText("")
        self.circleLabel.setObjectName("circleLabel")
        self.circleLabel.setPixmap(QtGui.QPixmap(str(client_path)+"\\assets\\indicador.png"))
        self.circleLabel.hide()

        # 0 = Cami; 1 = Ruta
        self.map_painter = MapPainter(str(client_path)+'\\assets\\map.png')

        #self.mode = self.modeComboBox.currentIndex()

        self.mapa.mouseReleaseEvent = self.mouseReleased
        self.modeComboBox.currentIndexChanged.connect(self.change_mode)
        self.calcularButton.clicked.connect(self.calculate_path)
        self.rutaButton.clicked.connect(self.calculate_route)
        self.netejaButton.clicked.connect(self.reset_route)
        self.netejaButton2.clicked.connect(self.reset_route)
        self.originButton.clicked.connect(self.select_origin)
        self.goalButton.clicked.connect(self.select_goal)

        self.firstClick = True

        self.originVertex = 0
        self.goalVertex = 0

        self.g = Graph()
        self.g_val = list(self.g.vertex_coord.values())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alou"))
        MainWindow.setWindowIcon(QtGui.QIcon(str(client_path)+'\\assets\\logo.png'))
        self.modeComboBox.setItemText(0, _translate("MainWindow", "Camins"))
        self.modeComboBox.setItemText(1, _translate("MainWindow", "Ruta"))
        self.modeLabel.setText(_translate("MainWindow", "Mode:"))
        self.originLabel.setText(_translate("MainWindow", "Origen:"))
        self.nombre.setText(_translate("MainWindow", "Alou"))
        self.calcularButton.setText(_translate("MainWindow", "Calcular camí"))
        self.goalLabel.setText(_translate("MainWindow", "Destí:"))
        self.netejaButton.setText(_translate("MainWindow", "Neteja"))
        self.caractComboBox.setItemText(0, _translate("MainWindow", "Monuments"))
        self.caractComboBox.setItemText(1, _translate("MainWindow", "Llocs emblemàtics"))
        self.caractComboBox.setItemText(2, _translate("MainWindow", "Parcs"))
        self.caractLabel.setText(_translate("MainWindow", "Realitzar la ruta per:"))
        self.rutaButton.setText(_translate("MainWindow", "Calcular ruta"))
        self.netejaButton2.setText(_translate("MainWindow", "Neteja"))
        self.label.setText(_translate("MainWindow", "Aquesta aplicació ha estat desenvolupada per Marc Benaches Magraner (github.com/MarcBen05)"))

###Custom functions
    def mouseReleased(self, QMouseEvent):
        if QMouseEvent.button() != QtCore.Qt.MouseButton.LeftButton:
            return
            
        cv = self.g.find_closest((np.int64(QMouseEvent.x()), np.int64(QMouseEvent.y())))
        x = self.g.vertex_coord[cv][0]
        y = self.g.vertex_coord[cv][1]

        oLat, oLon = self.map_painter.img_to_coord(x,y)

        if self.modeComboBox.currentIndex() == 1:
            self.firstClick = True

        if self.firstClick:
            w = self.circleLabel.geometry().width()
            h = self.circleLabel.geometry().height()

            self.circleLabel.move(x-0.5*w,y-0.5*h)
            self.circleLabel.show()

            self.originCoord.setText(f"Lat: {round(oLat,4)}\nLon: {round(oLon,4)}")
            self.firstClick = False
            self.originVertex = cv
        else:
            w = self.pinLabel.geometry().width()
            h = self.pinLabel.geometry().height()

            self.pinLabel.move(x-(w/2.0),y-h)
            self.pinLabel.show()

            self.goalCoord.setText(f"Lat:{round(oLat,4)}\nLon: {round(oLon,4)}")
            self.firstClick = True
            self.goalVertex = cv

        self.mapa.setFocus()

    def select_origin(self):
        self.firstClick = True

    def select_goal(self):
        self.firstClick = False

    def reset_route(self):
        self.mapa.setPixmap(QtGui.QPixmap(str(client_path)+'\\assets\\map.png'))
        self.pinLabel.hide()
        self.circleLabel.hide()
        
        self.originCoord.setText("")
        self.goalCoord.setText("")

        self.firstClick = True
        self.originVertex = 0
        self.goalVertex = 0

        self.map_painter.set_map(str(client_path)+'\\assets\\map.png')

    def calculate_path(self):
        if self.originVertex == 0 or self.goalVertex == 0:
            return

        originVertex = self.originVertex
        goalVertex = self.goalVertex

        #Els pesos no són utilitzats en aquest lloc, però serà útil per al pròxim
        path, w = Dijkstra(self.g, originVertex, goalVertex)

        if path:
            self.map_painter.set_map(str(client_path)+'\\assets\\map.png')
            self.map_painter.set_route(self.g.route_to_coords(path))
            self.map_painter.paint_map(str(client_path)+'\\assets\\result_map.png')
            self.mapa.setPixmap(QtGui.QPixmap(str(client_path)+'\\assets\\result_map.png'))

        else:
            print("There's no route!")

    def calculate_route(self):
        if self.originVertex == 0 or not self.originCoord.text():
            return
        
        originVertex = self.originVertex
        #routeCaract = str(self.caractComboBox.currentIndex() + 1) #L'índex comença per 0, però necessitem que comenci per 1
        #1 -> Monuments; 2-> Llocs emb; 3-> Parcs;  !!Versió reduida
        routeCaract = 0
        if self.caractComboBox.currentIndex() == 0:
                routeCaract = '1'
        elif self.caractComboBox.currentIndex() == 1:
                routeCaract = '3'
        else:
                routeCaract = '4'
        
        #Dict key is vertex
        dist = {}
        routes = {}

        taggedVertices = self.g.find_vertices_with_tag(routeCaract)

        if not taggedVertices:
            print("ERROR: taggedVertices list is empty!")
            print(f"INFO: caract: {routeCaract}, origin: {originVertex}")
            return

        routeList = []
        routeList.append(originVertex)

        #Busca els camins des del vertex origen fins a tots els que compleixen la caracteristica
        #després, agafa el que té el camí més curt i el posa com a origen a la següent iteració.
        #Quan tots els vèrtex estan ordenats, trenca el bucle
        while True:
            for v in taggedVertices:
                route, w = Dijkstra(self.g, routeList[-1], v)
                dist[v] = w
                routes[v] = route

            vertex = 0
            distance = INFINITY
            if not taggedVertices:
                break

            for v in taggedVertices:
                if dist[v] < distance:
                    distance = dist[v]
                    vertex = v
            routeList.append(vertex)
            taggedVertices.remove(vertex)

        route = []
        #Evita que el camí passi per vèrtexs anteriors per a evitar confusions
        restriction = {}
        for i in range(0, len(routeList)):
            if i == 0:
                continue
            r, w, restr = Dijkstra_Restricted(self.g, routeList[i-1], routeList[i], restriction)
            route += r 
            restriction = restr

        if route:
            self.map_painter.set_map(str(client_path)+'\\assets\\map.png')
            self.map_painter.set_route(self.g.route_to_coords(route))
            self.map_painter.paint_map(str(client_path)+'\\assets\\result_map.png')
            self.mapa.setPixmap(QtGui.QPixmap(str(client_path)+'\\assets\\result_map.png'))
        else:
            print("ERROR: Empty route!")


    def change_mode(self):
        if self.modeComboBox.currentText() == 'Camins':
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)
            self.pinLabel.hide()