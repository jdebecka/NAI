import numpy as np
from Model.Model_list import Model_list
from Service import Calculations
import random
import matplotlib.pyplot as plt
import string


class Data_School:
    def __init__(self, number_of_languages, model: Model_list, learn_rate, iteration_count):
        self.model_vec_arr = np.identity(number_of_languages)
        self.iteration_count = iteration_count
        self.model_languages = model
        self.weight_matrix = [[random.random() for _ in range(26)] for _ in range(number_of_languages)]
        self.bias_matrix = [random.random() for _ in range(number_of_languages)]
        self.learn_rate = learn_rate
        self.dictionary_language_identifier = dict()
        self.correct = 0
        self.x_to_plot = [0]
        self.y_to_plot = [self.correct]
        self.test_iterations = 0

    def train(self):
        for i in range(self.iteration_count):
            for key, target in zip(self.model_languages.language_model.keys(), self.model_vec_arr):
                if key not in self.dictionary_language_identifier:
                    self.dictionary_language_identifier[key] = target

                single_language = self.model_languages.language_model.get(key)

                normalized_array_for_language = single_language.normalize_and_return()

                for normalized_array in normalized_array_for_language:
                    output = Calculations.output_formula(normalized_array, self.weight_matrix, self.bias_matrix)
                    error = Calculations.error_formula(target, output)
                    self.weight_matrix, self.bias_matrix = Calculations.update_weights(normalized_array, error,
                                                                                       self.weight_matrix,
                                                                                       self.bias_matrix,
                                                                                       self.learn_rate)
                    self.y_to_plot.append(sum(error) / len(error))
                    self.x_to_plot.append(i)
        self.plot()
        print(self.dictionary_language_identifier)

    def test(self, test_model: Model_list):
        self.correct = 0
        self.test_iterations = 0
        prediction = ""
        for key in test_model.language_model.keys():
            if key not in self.dictionary_language_identifier:
                print("Non identidiabel language")
            single_language = self.model_languages.language_model.get(key)
            normalized_array_for_language = single_language.normalize_and_return()
            target = self.dictionary_language_identifier.get(key)

            for normalized_array in normalized_array_for_language:
                output = Calculations.output_formula(normalized_array, self.weight_matrix, self.bias_matrix)
                error = Calculations.error_formula(target, output)

                index_min = np.argmin(error)
                index_max = np.argmax(output)
                error = np.zeros(len(error))
                output = np.zeros(len(output))
                output[index_max] = 1
                error[index_min] = 1

                for key_final in self.dictionary_language_identifier.keys():
                    model_value = self.dictionary_language_identifier.get(key_final)
                    error_string = ' '.join(map(str, error))
                    model_string = ' '.join(map(str, model_value))
                    if error_string == model_string:
                        prediction = key_final
                        if key_final == key:
                            self.correct += 1
                            continue
                self.test_iterations += 1
        return prediction

    def test_custom_text(self, model: Model_list):
        single_model = model.language_model.get("Custom")
        normalized_array_for_language = single_model.normalize_and_return()

        output = Calculations.output_formula(normalized_array_for_language[0], self.weight_matrix, self.bias_matrix)
        index_max = np.argmax(output)

        prediction = np.zeros(len(output))
        prediction[index_max] = 1

        for key in self.dictionary_language_identifier:
            if self.dictionary_language_identifier.get(key).tostring() == prediction.tostring():
                return key

        print(output)

    def accuracy(self):
        return self.correct * 100 / self.test_iterations

    def plot(self):
        plt.plot(self.x_to_plot, self.y_to_plot)
        plt.title("Training iterations vs. # of errors")
        plt.grid(True)
        plt.xlabel("Iteration count")
        plt.ylabel("# of errors")
        plt.savefig(
            '/Users/juliadebecka/Documents/GitHub/NAI/Language_Classifier/Single_Layer_Network/Resources/Plots/errors_iter.png')
