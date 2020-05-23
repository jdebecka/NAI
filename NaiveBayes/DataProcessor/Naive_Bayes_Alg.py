import numpy as np
from operator import itemgetter
from Model.Confucion_Matrix import Confusion_Matrix


def calculate_probability_class_occurrence(count, length):
    return count / length


def calculate_class_probability(class_len, all_len):
    return class_len / all_len


def test_summary(result: dict):
    for key in result:
        con_matrix = result.get(key)
        recall = calculate_recall(con_matrix.true_pos, con_matrix.false_neg)
        precision = calculate_precision(con_matrix.true_pos, con_matrix.false_pos)
        f_score = calculate_f_score(precision, recall)
        print(f"key = {key}, recall = {recall}, prection = {precision}, f_score = {f_score}")


def calculate_recall(true_pos, false_neg):
    return true_pos / (true_pos + false_neg)


def calculate_accuracy(true_pos, false_neg):
    return true_pos / (true_pos + false_neg)


def calculate_precision(true_pos, false_pos):
    return true_pos / (true_pos + false_pos)


def calculate_f_score(precision, recall):
    return 2 * (precision * recall) / (precision + recall)


def union_list(list_1, list_2):
    if list_1 is None:
        list_1 = []
    set_1 = set(list_1)
    set_2 = set(list_2)

    list_2_items_not_in_list_1 = list(set_2 - set_1)
    combined_list = list_1 + list_2_items_not_in_list_1

    return combined_list


def print_all(actual, predicted, index):
    print(f"Test nr: {index}, Actual class: {actual}, Predicted class: {predicted}")


class Naive_Bayes_Alg:
    def __init__(self, data_dict: dict):
        self.data_dict = data_dict
        self.classifier_data = dict()
        self.trained_dictionary = dict()
        self.class_probability = dict()
        self.unique_values_for_row = dict()
        self.get_unique_for_every_row()

    def calculate_all_len(self):
        sum_all = sum([len(x) for x in self.data_dict.values()])
        return sum_all

    def create_results(self, dic: dict):
        res_class_dict = dict()

        for key in self.data_dict.keys():
            res_class_dict[key] = Confusion_Matrix(key)

        for key in dic:
            values = dic[key]
            index, class_name = key
            res = max(values, key=itemgetter(1))[0]

            print_all(class_name, res, index)
            if res == class_name:
                res_class_dict.get(class_name).add_true_pos()
            else:
                res_class_dict.get(class_name).add_false_neg()
                res_class_dict.get(res).add_false_pos()

        return res_class_dict

    def get_unique_for_every_row(self):
        for key in self.data_dict:
            index = 0
            attributes = self.data_dict.get(key)
            attributes = np.transpose(attributes)
            for row in attributes:
                list_for_row = self.unique_values_for_row.get(index)
                list_unique = np.unique(row)
                self.unique_values_for_row[index] = union_list(list_for_row, list_unique)
                index += 1

    def train(self):
        len_all = self.calculate_all_len()
        for key in self.data_dict:
            self.class_probability[key] = calculate_class_probability(len(self.data_dict.get(key)), len_all)
            val_count_dict = dict()
            index = 0
            car_attributes = self.data_dict.get(key)
            car_attributes = np.transpose(car_attributes)

            for row in car_attributes:
                unique_values, repeated = np.unique(row, return_counts=True)
                if len(unique_values) != len(self.unique_values_for_row.get(index)):
                    for value in self.unique_values_for_row.get(index):
                        if value not in unique_values:
                            unique_values = np.append(unique_values, value, axis=None)
                            repeated = np.append(repeated, 0, axis=None)
                    repeated = np.array(list(map(lambda x: x + 1, repeated)))
                sum_all = sum(repeated)
                for value, count in zip(unique_values, repeated):
                    p_a_b = calculate_probability_class_occurrence(count, sum_all)
                    val_count_dict[(index, value)] = p_a_b
                index += 1

            self.trained_dictionary[key] = val_count_dict

        return self.trained_dictionary

    def test_data(self, test_file: dict):
        dict_all_probabilities = dict()
        count = 0
        for key in test_file:
            test_params = test_file[key]

            for params in test_params:
                dict_all_probabilities[(count, key)] = list()
                for secondKey in self.trained_dictionary:
                    index = 0
                    index_value_probability_dict = self.trained_dictionary.get(secondKey)
                    probability = self.class_probability.get(secondKey)
                    for attribute in params:
                        index_value = (index, attribute)
                        probability *= index_value_probability_dict.get(index_value)

                        index += 1
                    dict_all_probabilities[(count, key)].append((secondKey, probability))
                count += 1
        result = self.create_results(dict_all_probabilities)
        test_summary(result)

        return result
