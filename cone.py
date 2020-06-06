# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cone.ui',
# licensing of 'cone.ui' applies.
#
# Created: Sat Jun  6 09:27:58 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 255)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 111, 20))
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 111, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 111, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_h = QtWidgets.QLineEdit(Form)
        self.lineEdit_h.setGeometry(QtCore.QRect(140, 20, 113, 20))
        self.lineEdit_h.setObjectName("lineEdit_h")
        self.lineEdit_d = QtWidgets.QLineEdit(Form)
        self.lineEdit_d.setGeometry(QtCore.QRect(140, 60, 113, 20))
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.lineEdit_V = QtWidgets.QLineEdit(Form)
        self.lineEdit_V.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.lineEdit_V.setObjectName("lineEdit_V")
        self.label_1.setBuddy(self.lineEdit_h)
        self.label_2.setBuddy(self.lineEdit_d)
        self.label_3.setBuddy(self.lineEdit_V)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.lineEdit_h, QtCore.SIGNAL("textChanged(QString)"), Form.przelicz)
        QtCore.QObject.connect(self.lineEdit_d, QtCore.SIGNAL("textChanged(QString)"), Form.przelicz)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Obliczanie objętości stożka", None, -1))
        self.label_1.setText(QtWidgets.QApplication.translate("Form", "Wysokość h:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Średnica podstawy d:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Objętość:", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

