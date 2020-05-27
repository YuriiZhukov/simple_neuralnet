import sys
from PyQt5 import QtWidgets
from net import NeuralNet
from window import Window
import numpy

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()

    #create net
    n = 50
    input_nodes = n*n
    hidden_nodes = int(n*n/10)
    output_nodes = 10
    learning_rate = 0.3
    net = NeuralNet(input_nodes, hidden_nodes, output_nodes, learning_rate)
    
    wih_data_file = open("wih.txt", 'r') 
    wih_data_list = wih_data_file.readlines() 
    wih_data_file.close() 
    who_data_file = open("who.txt", 'r') 
    who_data_list = who_data_file.readlines() 
    who_data_file.close()

    if (len(wih_data_list) == len(net.wih) and len(who_data_list) == len(net.who)):
        for i in range(len(wih_data_list)):
            string_values = wih_data_list[i].split(',')
            float_values = numpy.asfarray(string_values)
            net.wih[i] = float_values

        for i in range(len(who_data_list)):
            string_values = who_data_list[i].split(',')
            float_values = numpy.asfarray(string_values)
            net.who[i] = float_values

    #set net to GUI app
    window.setupNeuralNet(net)

    app.exec_()

if __name__ == '__main__': main()
