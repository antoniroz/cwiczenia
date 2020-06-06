# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cone.ui',
# licensing of 'cone.ui' applies.
#
# Created: Sat Jun  6 08:57:20 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

import math
from PySide2 import QtCore, QtGui, QtWidgets

from cone import Ui_Form


class MyQWidget(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
    def przelicz(self):
        h = self.ui.lineEdit_h.text()
        d = self.ui.lineEdit_d.text()
        
        h = float(h)
        d = float(d)
        V = 1/3 * (d/2)**2 * h
        V = str(V)        
        
        self.ui.lineEdit_V.setText(V)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = MyQWidget()
    Form.show()
    sys.exit(app.exec_())

