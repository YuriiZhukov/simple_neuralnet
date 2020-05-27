# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(150, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(180, 280))
        Form.setMaximumSize(QtCore.QSize(180, 280))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(9)
        self.spinBox.setValue(0)
        self.checkButton = QtWidgets.QPushButton(Form)
        self.checkButton.setText("Check")
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setText("Clear")
        self.saveWeigthsButton = QtWidgets.QPushButton(Form)
        self.saveWeigthsButton.setText("Save Weigths")
        self.addTrainDataButton = QtWidgets.QPushButton(Form)
        self.addTrainDataButton.setText("&Add train data")
        self.trainButton = QtWidgets.QPushButton(Form)
        self.trainButton.setText("&Train")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setMinimumSize(QtCore.QSize(52, 52))
        self.graphicsView.setMaximumSize(QtCore.QSize(52, 52))
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.checkButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.clearButton, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.addTrainDataButton, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.trainButton, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.spinBox, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.saveWeigthsButton, 6, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
