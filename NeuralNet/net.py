import scipy.special
import numpy

class NeuralNet:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        self.train_data = []

    def trainWithCurrentData(self, input, target):
        #добавляется список target int + 10'000 пикселей 
        #[[target, int, int...],[target, int, int...]]
        data = []
        data.append(target)
        for val in range(len(input)):
            data.append(input[val])
        
        inputs = (numpy.asfarray(data[1:]) / 255.0 * 0.99) + 0.01
        targets = numpy.zeros(self.onodes) + 0.01
        targets[int(data[0])] = 0.99
        self.train(inputs, targets)

    def train(self, inputs_list, targets_list):
        targets = numpy.array(targets_list, ndmin=2).T
        
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = scipy.special.expit(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = scipy.special.expit(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)
        self.who += self.lr * numpy.dot((output_errors * final_outputs * 
            (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * 
            (1.0 - hidden_outputs)), numpy.transpose(inputs))

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = scipy.special.expit(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = scipy.special.expit(final_inputs)
        value = 0.0
        result = 0
        for i in range(len(final_outputs)):
            if final_outputs[i] > value:
                value = final_outputs[i]
                result = i
   #     print("out = ", final_outputs)
        print("res = ", result)

        return final_outputs