from Service import DataReader
from Model import Vector
from Service.Perceptron import Perceptron
from Model.Vector import Vector


class Main:

    def __init__(self):
        self.data = []
        self.perceptron: Perceptron
        self.test_data = []
        self.default_data_path = "/Users/juliadebecka/Documents/GitHub/NAI/Perceptron/Resources/perceptron.data"
        self.default_test_path = "/Users/juliadebecka/Documents/GitHub/NAI/Perceptron/Resources/perceptron.test.data"
        self.default_iterations = 1000
        self.default_learining_rate = .1

    def data_file(self, filepath=''):
        filepath_check = self.check_filepath(filepath, 'd')
        return DataReader.read_and_save(filepath_check)

    def test(self):
        accuracy = self.perceptron.test(self.test_data)
        return accuracy

    def perceptron_set_up(self, learning_rate, iterations):
        if iterations == 0:
            iterations = self.default_iterations
        if learning_rate == 0:
            learning_rate = self.default_learining_rate
        self.data = self.data_file()
        self.perceptron = Perceptron(self.data, learning_rate, iterations)

    def test_custom(self, list_float, vector_name):
        if len(self.data) == 0:
            self.data_file()
        vec = [Vector(list_float, vector_name)]
        return self.perceptron.test(vec)

    def test_file(self, filepath=''):
        filepath_check = self.check_filepath(filepath, 't')
        self.test_data = DataReader.read_and_save(filepath_check)

    def check_filepath(self, filepath, kind):
        if filepath == '':
            if kind == 'd':
                return self.default_data_path
            if kind == 't':
                return self.default_test_path
        else:
            return filepath

    def train(self, iter=0, learning_r=0):
        self.perceptron_set_up(learning_r, iter)
        choices = self.perceptron.train()
        return list(choices.keys())
