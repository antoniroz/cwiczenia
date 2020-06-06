# -*- coding: utf-8 -*-

import math
from PySide2 import QtCore, QtGui, QtWidgets

from cone import Ui_Form


class MyQWidget(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
    def przelicz(self):
        h = self.ui.lineEdit_h.text()
        d = self.ui.lineEdit_d.text()
        
        h = float(h)
        d = float(d)
        V = 1/3 * (d/2)**3 * h
        V = str(V)        
        
        self.ui.lineEdit_V.setText(V)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = MyQWidget()
    Form.show()
    sys.exit(app.exec_())

