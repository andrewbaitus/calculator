# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(262, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_number = QtWidgets.QLineEdit(self.centralwidget)
        self.input_number.setGeometry(QtCore.QRect(10, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_number.setFont(font)
        self.input_number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_number.setObjectName("input_number")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(10, 110, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(60, 110, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(110, 110, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(10, 160, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(60, 160, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(110, 160, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 210, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(60, 210, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(110, 210, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(10, 260, 91, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(110, 260, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(160, 260, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.btn_umnoz = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umnoz.setGeometry(QtCore.QRect(160, 210, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_umnoz.setFont(font)
        self.btn_umnoz.setObjectName("btn_umnoz")
        self.btn_min = QtWidgets.QPushButton(self.centralwidget)
        self.btn_min.setGeometry(QtCore.QRect(160, 160, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_min.setFont(font)
        self.btn_min.setObjectName("btn_min")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(160, 110, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_answer = QtWidgets.QPushButton(self.centralwidget)
        self.btn_answer.setGeometry(QtCore.QRect(210, 209, 40, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_answer.setFont(font)
        self.btn_answer.setObjectName("btn_answer")
        self.btn_pow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pow.setGeometry(QtCore.QRect(210, 160, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_pow.setFont(font)
        self.btn_pow.setObjectName("btn_pow")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(210, 110, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.btn_backspace = QtWidgets.QPushButton(self.centralwidget)
        self.btn_backspace.setGeometry(QtCore.QRect(109, 60, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_backspace.setFont(font)
        self.btn_backspace.setObjectName("btn_backspace")
        self.btn_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sqrt.setGeometry(QtCore.QRect(9, 60, 91, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setObjectName("btn_sqrt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор v 1.0"))
        self.input_number.setText(_translate("MainWindow", "0"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_del.setText(_translate("MainWindow", "/"))
        self.btn_umnoz.setText(_translate("MainWindow", "*"))
        self.btn_min.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_answer.setText(_translate("MainWindow", "="))
        self.btn_pow.setText(_translate("MainWindow", "^"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_backspace.setText(_translate("MainWindow", "BACKSPACE"))
        self.btn_sqrt.setText(_translate("MainWindow", "SQRT"))
