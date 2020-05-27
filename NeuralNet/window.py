from PyQt5 import QtCore, QtWidgets
from graphicscene import GraphicScene
from net import NeuralNet
import design
import numpy

class Window(QtWidgets.QWidget, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
        self.scene = GraphicScene(self)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.net = NeuralNet(1,1,1,0)
        self.checkButton.clicked.connect(self.netCheck)
        self.clearButton.clicked.connect(self.clearGraphicsScene)
        self.trainButton.clicked.connect(self.trainNetworkWithCurrentData)
        self.addTrainDataButton.clicked.connect(self.addTrainDataToFile)
        self.saveWeigthsButton.clicked.connect(self.saveWeights)

    def setupNeuralNet(self, net):
        self.net = net

    def saveWeights(self):
        wih_data_file = open("wih.txt", 'w+') 
        who_data_file = open("who.txt", 'w+') 
        
        for i in range(len(self.net.who)):
            for j in range(len(self.net.who[i])):
                if j < len(self.net.who[i]) - 1:
                    who_data_file.write(str(self.net.who[i][j]) + ",")
                else:
                    who_data_file.write(str(self.net.who[i][j]))
            who_data_file.write("\n")

        for i in range(len(self.net.wih)):
            for j in range(len(self.net.wih[i])):
                if j < len(self.net.wih[i]) - 1:
                    wih_data_file.write(str(self.net.wih[i][j]) + ",")
                else:
                    wih_data_file.write(str(self.net.wih[i][j]))
            wih_data_file.write("\n")
  
        wih_data_file.close() 
        who_data_file.close() 


    def clearGraphicsScene(self):
        self.scene.clear()

    def trainNetwork(self):
        self.net.trainByself()

    def trainNetworkWithCurrentData(self):
        #получить картинку (pixmap) из view
        self.scene.pixmap = self.graphicsView.grab(QtCore.QRect(1,1,self.scene.rectX, self.scene.rectY))
        self.scene.image = self.scene.pixmap.toImage()
        #записать цвет каждого пикселя в матрицу размерностью картинки (56x56)
        w = self.scene.image.width()
        h = self.scene.image.height()
        inputs = [0] * (w*h)
        for y in range(h):
            for x in range(w):
                inputs[y*h + x] = self.scene.image.pixelColor(x,y).black()
        target = self.spinBox.value()
        self.net.trainWithCurrentData(inputs, target)
        self.clearGraphicsScene()

    def addTrainDataToFile(self):
        self.scene.pixmap = self.graphicsView.grab(QtCore.QRect(1,1,self.scene.rectX, self.scene.rectY))
        self.scene.image = self.scene.pixmap.toImage()
        #записать цвет каждого пикселя в матрицу размерностью картинки (56x56)
        w = self.scene.image.width()
        h = self.scene.image.height()
        data = [0] * (w*h + 1)
        for y in range(h):
            for x in range(w):
                data[y*h + x + 1] = self.scene.image.pixelColor(x,y).black()
        target = self.spinBox.value()
        data[0] = target
        train_data_file = open("train_data.txt", 'a')
        for i in range(len(data)):
            if i < len(data) - 1:
                train_data_file.write(str(data[i]) + ",")
            else:
                train_data_file.write(str(data[i]))
        train_data_file.write("\n")
        train_data_file.close()
        self.clearGraphicsScene()

    def netCheck(self):
        #получить картинку (pixmap) из view
        self.scene.pixmap = self.graphicsView.grab(QtCore.QRect(1,1,self.scene.rectX, self.scene.rectY))
        self.scene.image = self.scene.pixmap.toImage()
        #записать цвет каждого пикселя в матрицу размерностью картинки (56x56)
        w = self.scene.image.width()
        h = self.scene.image.height()
        all_values = [0] * (w*h)
        for y in range(h):
            for x in range(w):
                all_values[y*h + x] = self.scene.image.pixelColor(x,y).black()

        #отправить список пикселей в нейросеть для проверки
        inputs = (numpy.asfarray(all_values[0:]) / 255.0 * 0.99) + 0.01
        final_outputs = self.net.query(inputs)
 