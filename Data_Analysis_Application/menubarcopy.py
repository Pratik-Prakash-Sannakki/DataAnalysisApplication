from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import numpy as np
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, uic

import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt

from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas,     NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import numpy as np
import sys
import txt_int as tx
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        """ menu bar and all sub_bars """
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("load file")
        sel=actionFile.addAction("file selection")
        sel.triggered.connect(self.on_click)
        plo=actionFile.addAction("Plot Param")
        menubar.addMenu("Plot Multiple Parameter")
        menubar.addMenu("Param Subplot")
        menubar.addMenu("Report")
        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")
        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()
    def on_click(self):
        
        dlg=QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(["TextFiles (*.txt)"])

        if dlg.exec_():
            filenames=dlg.selectedFiles()
            f =open(filenames[0],'r')

            with f:
                data=f.read()
                self.contents.setText(data)
    
        
        """ this function is for txt file dispay and Paramater display """
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0,0)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500,0)
        button.resize(140,100)
        self.show()
        
        
        
   
    


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
