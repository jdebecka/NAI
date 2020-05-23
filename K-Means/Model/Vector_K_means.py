import string
import numpy as np


class Vector_K_means:
    def __init__(self):
        self.class_vec = list()
        self.coordinate_dick = dict()
        self.alphabet = string.ascii_lowercase

    def add_vec(self, class_vec, list_floats):
        self.class_vec.append(class_vec)
        for letter, vec_cor in zip(self.alphabet, list_floats):
            if letter not in self.coordinate_dick:
                new_list = list()
                self.coordinate_dick[letter] = new_list
            old_list = self.coordinate_dick.get(letter)
            old_list.append(vec_cor)
            self.coordinate_dick[letter] = old_list

    def normalize(self):
        for key in self.coordinate_dick:
            coordinate = self.coordinate_dick.get(key)
            X_min = np.amin(coordinate)
            X_max = np.amax(coordinate)
            X_p = (coordinate - X_min) / (X_max - X_min)

            self.coordinate_dick[key] = X_p