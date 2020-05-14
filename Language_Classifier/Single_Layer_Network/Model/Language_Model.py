import math
import numpy as np


class Language_Model:
    def __init__(self, language, letter_count_dict: dict):
        self.language = language
        self.letter_count_dict = []
        self.letter_count_dict.append(letter_count_dict)
        self.formula = dict()

    def add_dictionary(self, new_dictionary):
        self.letter_count_dict.append(new_dictionary)

    def normalize_and_return(self):
        normalized_array = []
        for dictionary in self.letter_count_dict:
            array_vec = []
            vac_length = math.sqrt(sum(pow(value, 2) for value in dictionary.values()))
            for value in dictionary.values():
                array_vec.append(value / vac_length)
            normalized_array.append(array_vec)
        return normalized_array
