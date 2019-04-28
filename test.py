# -*- coding: utf-8 -*-

import app
from app import Cascada
import sys
from PyQt5 import QtWidgets

App = QtWidgets.QApplication(sys.argv)
_app = Cascada()
_app.load_template("layout.html")

if __name__ == '__main__':
    _app.run()
    sys.exit(App.exec_())