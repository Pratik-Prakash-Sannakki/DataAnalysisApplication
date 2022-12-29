from reportlab.pdfgen import canvas
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
import txt_int as tix
import numpy as np
from reportlab.lib import colors
from reportlab.graphics.shapes import *
import statistics
import numpy 


drawing = Drawing(1000,1000)
drawing.add(String(250,900, "DATA ANALYSIS REPORT", fontSize=40, fillColor=colors.blue))
drawing.add(String(45,800, "Parameter:", fontSize=15, fillColor=colors.green))
drawing.add(String(165,800, tix.myparam[0], fontSize=15, fillColor=colors.black))
drawing.add(String(215,800, tix.myparam[1], fontSize=15, fillColor=colors.black))
drawing.add(String(270,800, tix.myparam[2], fontSize=15, fillColor=colors.black))
drawing.add(String(325,800, tix.myparam[3], fontSize=15, fillColor=colors.black))

drawing.add(String(45 ,775, "Maximum value:", fontSize=15, fillColor=colors.green))
drawing.add(String(165 ,775,str(tix.maxhello) , fontSize=15, fillColor=colors.black))
drawing.add(String(215,775,str(tix.maxvol), fontSize=15, fillColor=colors.black))
drawing.add(String(270,775,str(tix.maxcur), fontSize=15, fillColor=colors.black))
drawing.add(String(325,775,str(tix.maxtemp), fontSize=15, fillColor=colors.black))

drawing.add(String(45 ,750, "Minimum value:", fontSize=15, fillColor=colors.green))
drawing.add(String(165 ,750,str(min(tix.hello)), fontSize=15, fillColor=colors.black))
drawing.add(String(215,750,str(min(tix.vol)), fontSize=15, fillColor=colors.black))
drawing.add(String(270,750,str(min(tix.cur)), fontSize=15, fillColor=colors.black))
drawing.add(String(325,750,str(min(tix.temp)), fontSize=15, fillColor=colors.black))

drawing.add(String(45 ,725, "Mean value:", fontSize=15, fillColor=colors.green))
drawing.add(String(165 ,725,str(round(statistics.mean(tix.hello),2)), fontSize=15, fillColor=colors.black))
drawing.add(String(215,725,str(round(statistics.mean(tix.vol),2)), fontSize=15, fillColor=colors.black))
drawing.add(String(270,725,str(round(statistics.mean(tix.cur),2)), fontSize=15, fillColor=colors.black))
drawing.add(String(325,725,str(round(statistics.mean(tix.temp),2)), fontSize=15, fillColor=colors.black))

drawing.add(String(45 ,700, "Standard diviation:", fontSize=15, fillColor=colors.green))
drawing.add(String(165 ,700, str(round(numpy.std(tix.hello,dtype=float),2)), fontSize=15, fillColor=colors.black))
drawing.add(String(215,700,str(round(numpy.std(tix.vol,dtype=float),2)), fontSize=15, fillColor=colors.black))
drawing.add(String(270,700,str(round(numpy.std(tix.cur,dtype=float),2)), fontSize=15, fillColor=colors.black))
drawing.add(String(325,700,str(round(numpy.std(tix.temp,dtype=float),2)), fontSize=15, fillColor=colors.black))

drawing.add(String(505,530, "Fusion:", fontSize=15, fillColor=colors.green))
data = [tix.vol,tix.cur,tix.temp]
to = HorizontalLineChart()
to.x = 500
to.y = 200
to.height = 300
to.width = 400
to.data = data
to.joinedLines = 1
catNames = '0 1 2 3 4 5 6 7'.split(' ')
to.categoryAxis.categoryNames = catNames
to.categoryAxis.labels.boxAnchor = 'n'
to.valueAxis.valueMin = 0
to.valueAxis.valueMax = 60
to.valueAxis.valueStep = 15 
to.lines[0].strokeWidth = 2
to.lines[1].strokeWidth = 1.5

drawing.add(String(45,210, tix.myparam[1], fontSize=15, fillColor=colors.green))
data = [tix.vol]
lc = HorizontalLineChart()
lc.x = 50
lc.y = 50
lc.height = 125
lc.width = 300
lc.data = data
lc.joinedLines = 1
catNames = '0 1 2 3 4 5 6 7'.split(' ')
lc.categoryAxis.categoryNames = catNames
lc.categoryAxis.labels.boxAnchor = 'n'
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 60
lc.valueAxis.valueStep = 15 
lc.lines[0].strokeWidth = 2
lc.lines[1].strokeWidth = 1.5


drawing.add(String(45,410, tix.myparam[2], fontSize=15, fillColor=colors.green))
data1 = [tix.cur]
kc = HorizontalLineChart()
kc.x = 50
kc.y = 250
kc.height = 125
kc.width = 300
kc.data = data1
kc.joinedLines = 1
kc.lineLabelArray=['cars']
catNames = '0 1 2 3 4 5 6 7'.split(' ')
kc.categoryAxis.categoryNames = catNames
kc.categoryAxis.labels.boxAnchor = 'n'
kc.valueAxis.valueMin = 0
kc.valueAxis.valueMax = 60
kc.valueAxis.valueStep = 15
kc.lines[0].strokeWidth = 2
kc.lines[1].strokeWidth = 1.5

drawing.add(String(45,600, tix.myparam[3], fontSize=15, fillColor=colors.green))
data2 = [tix.temp]
ls = HorizontalLineChart()
ls.x = 50
ls.y = 450
ls.height = 125
ls.width = 300
ls.data = data2
ls.joinedLines = 1
catNames = '0 1 2 3 4 5 6 7'.split(' ')
ls.categoryAxis.categoryNames = catNames
ls.categoryAxis.labels.boxAnchor = 'n'
ls.valueAxis.valueMin = 0
ls.valueAxis.valueMax = 60
ls.valueAxis.valueStep = 15
ls.lines[0].strokeWidth = 2
ls.lines[1].strokeWidth = 1.5

drawing.add(to)
drawing.add(ls)
drawing.add(lc)
drawing.add(kc)



from reportlab.graphics import renderPDF
renderPDF.drawToFile(drawing, 'example1.pdf',) 
