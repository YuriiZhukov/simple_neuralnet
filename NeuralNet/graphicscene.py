from PyQt5 import QtCore, QtGui, QtWidgets

class GraphicScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.view = QtWidgets.QGraphicsView(self)
        self.pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
        self.previousPoint = QtCore.QPoint(0,0)
        self.rectX = 50
        self.rectY = 50
        self.setSceneRect(0,0,self.rectX, self.rectY)
        self.pixmap = QtGui.QPixmap(self.rectX, self.rectY)
        self.image = QtGui.QImage(self.sceneRect().size().toSize(), QtGui.QImage.Format_RGB32)

    def mousePressEvent(self, ev):
        self.previousPoint = ev.scenePos()

    def mouseMoveEvent(self, ev):
        self.addLine(self.previousPoint.x(), self.previousPoint.y(),
                     ev.scenePos().x(), ev.scenePos().y(),
                     self.pen)
        self.previousPoint = ev.scenePos()