import pandas as pd

data = pd.read_csv('vertexs.csv', names=['LATITUD', 'LONGITUD'], sep=",", comment="#")
graph_data = tuple(zip(data['LATITUD'].values, data['LONGITUD'].values))


f = open("test.py", "w")
"""
i = 1
for d in graph_data:
    x,y = d

    f.write(f"self.button{i} = QtWidgets.QPushButton(self.centralwidget)\n")
    f.write(f"self.button{i}.clicked.connect(self.button{i}_clicked)\n")
    f.write(f"self.button{i}.setObjectName('{i}')\n")
    f.write(f"self.button{i}.move({x},{y})\n")
    f.write(f"\n")

    i += 1
f.write("\n")

"""
i = 1
for d in graph_data:
    x,y = d

    f.write(f"def button{i}_clicked(self):\n")

    f.write(f"\tprint(self.button{i}.objectName())\n")
    f.write("\tif self.firstClick:\n")
    f.write(f"\t\tself.firstBtn = self.g_val.index(({x},{y}))\n")
    f.write("\t\tself.firstClick = False\n")

    f.write(f"\t\tself.map_painter.insert_into_route({x},{y})\n")

    f.write("\telse:\n")

    f.write("\t\tif self.cb.currentText() == 'Dirigit':\n")
    f.write("\t\t\tf = open('arestes.csv', 'a')\n")
    f.write('\t\t\tf.write(f"{self.firstBtn},'+f'{i}'+',{float(self.textEdit.toPlainText())}\\n")\n')
    f.write("\t\t\tf.close()\n")

    f.write("\t\telse:\n")
    f.write("\t\t\tf = open('arestes.csv', 'a')\n")
    f.write('\t\t\tf.write(f"{self.firstBtn},'+f'{i}'+',{float(self.textEdit.toPlainText())}\\n")\n')
    f.write('\t\t\tf.write(f"'f'{i},'+'{self.firstBtn},'+'{float(self.textEdit.toPlainText())}\\n")\n')
    f.write("\t\t\tf.close()\n")

    f.write(f"\t\tself.map_painter.insert_into_route({x},{y})\n")

    f.write(f"\t\tif self.cb.currentText() == 'Dirigit':\n")
    f.write("\t\t\tself.map_painter.paint_map('test_map.png')\n")
    f.write(f"\t\telse:\n")
    f.write("\t\t\tself.map_painter.paint_map('test_map.png',(0,0,255))\n")


    f.write("\t\tself.map_painter.points.clear()\n")
    f.write("\t\tself.label.setPixmap(QtGui.QPixmap('test_map.png'))\n")

    f.write("\t\tself.firstClick = True\n")
    f.write("\n")

    i = i + 1
#"""
f.close()

#TODO: Afegir una seleccio de graph simple o dirigit al creador de grafs i posar
#en les conexions 1->2,2->1 si es simple, 1->2 només si es dirigit

"""
if self.cb.currentText() == "Dirigit":

else:

"""