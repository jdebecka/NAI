
from Model.Vector import Vector
import random
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:

    def __init__(self, vector_data: [Vector], learning_rate, iterations):
        self.test_data: [Vector] = []
        self.weight = []
        self.errors = 0
        self.vector_data: [Vector] = vector_data
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.class_name_dictionary = ({})
        self.first_iter = True
        self.class_int = 0
        self.x_to_plot = [0]
        self.y_to_plot = [self.errors]

    def test(self, test_data: [Vector]):
        self.test_data = test_data
        self.errors = 0
        self.iterations = len(test_data)

        for vector_ in test_data:
            prediction = self.predict(vector_)
            prediction_check = self.class_name_dictionary.get(vector_.class_name) - prediction

            if prediction_check != 0:
                self.errors += 1
        return self.accuracy()

    def print(self):
        print(self.vector_data)
        for vec in self.vector_data:
            print(vec.vectorX, vec.class_name)

    def update_weight_bias(self, vector_test, predicted, actual):
        prediction_check = actual - predicted
        if prediction_check != 0:
            self.errors += 1
            self.weight[0] -= self.learning_rate * prediction_check
            for i in range(len(self.weight[1:])):
                self.weight[i] += self.learning_rate * prediction_check * vector_test[0]

    def train(self):
        i = 0
        for iteration_elapsed in range(0, self.iterations):
            if self.first_iter:
                length = len(self.vector_data[i].vectorX) + 1
                for _ in range(length):
                    self.weight.append(random.random())
                self.first_iter = False

            if self.vector_data[i].class_name not in self.class_name_dictionary:
                self.class_name_dictionary[self.vector_data[i].class_name] = self.class_int
                self.class_int += 1

            prediction = self.predict(self.vector_data[i])
            actual = self.class_name_dictionary.get(self.vector_data[i].class_name)
            self.update_weight_bias(self.vector_data[i].vectorX, prediction, actual)

            i += 1
            self.x_to_plot.append(iteration_elapsed + 1)
            self.y_to_plot.append(self.errors)
            if i >= len(self.vector_data):
                i = 0
        self.plot()
        return self.class_name_dictionary

    def predict(self, vec):
        net = np.dot(np.transpose(self.weight[1:]), vec.vectorX) - self.weight[0]
        if net >= 0:
            return 1
        else:
            return 0

    def accuracy(self):
        return 100 - self.errors * 100 / self.iterations

    def plot(self):
        plt.plot(self.x_to_plot, self.y_to_plot)
        plt.title("Training iterations vs. # of errors")
        plt.grid(True)
        plt.xlabel("Iteration count")
        plt.ylabel("# of errors")
        plt.savefig('/Users/juliadebecka/Documents/GitHub/NAI/Perceptron/Resources/errors_iter.png')

