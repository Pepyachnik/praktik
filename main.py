import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import math

app = QtWidgets.QApplication(sys.argv)


MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def ur():
    global x1
    global x2
    a = int(ui.a_is.text())
    b = int(ui.B_is.text())
    c = int(ui.C_is.text())
 
    D = b ** 2 - 4 * a * c
    if D < 0:
        ui.korniNF.setText("Корней нет")
    elif D == 0:
        x = -b / 2 * a
        ui.X_is.setText(str("X = " + str(x)))
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)

        
        
        

        file = open("log.txt","a", encoding="utf-8")
        file.write("Пользователь ввел a = " + str(a) + "\n")
        file.write("Пользователь ввел b = " + str(b) + "\n")
        file.write("Пользователь ввел c = " + str(c) + "\n")
        file.write("Пользователь получил D = " + str(D) + "\n")
        file.write("Пользователь получил x1 = " + str(x1) + "\n")
        file.write("Пользователь получил x2 = " + str(x2) + "\n")
        file.write("\n")
        
    ui.D_is.setText(str("D = " + str(round(D , 3))))
    ui.x1_is.setText(str("X1 = " + str(round(x1 , 3))))
    ui.x2_is.setText(str("X2 = " + str(round(x2 , 3))))

    

ui.pushButton.clicked.connect(ur)

sys.exit(app.exec_())
