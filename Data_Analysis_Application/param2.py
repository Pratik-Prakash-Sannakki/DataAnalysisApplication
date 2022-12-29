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
import txt_int as tix
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example '
        self.width = 640
        self.height = 400
        self.initUI()
        widget =  QWidget(self)
        self.setCentralWidget(widget)
        vlay = QVBoxLayout(widget)
        hlay = QHBoxLayout()
        vlay.addLayout(hlay)
        m = WidgetPlot(self)
        vlay.addWidget(m)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        m = WidgetPlot(self)
        m.move(0,0)
        self.show()
class WidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.canvas = PlotCanvas(self, width=10, height=8)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)        
        
        
        

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=100, height=100, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        canvas=FigureCanvas.__init__(self, fig)
        self.setParent(parent)


        
        #comments
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
       
        ax = self.figure.add_subplot(111)
        self.axes.set_xlabel("Time ")
        self.axes.set_ylabel(tix.myparam[2])
        
        ax.plot(tix.cur,'go--')
        
        self.draw()


air = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())




