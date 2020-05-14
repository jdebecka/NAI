import string

from Service.FileHandler import FileHandler
from Service.Data_School import Data_School
from Model.Model_list import Model_list
import os


class Main:
    def __init__(self, language_letters=None):
        if language_letters is None:
            language_letters = list(string.ascii_lowercase)
        self.language_letters = language_letters
        self.file_handler = FileHandler(language_letters)
        self.keys = set()
        self.data_school: Data_School

    def walk_through_languages(self, resource_directory_path):
        model = Model_list()
        for (dir_path, dir_names, filenames) in os.walk(resource_directory_path):
            for dir_name in dir_names:
                for (dir_path_in, dir_names_in, filenames_in) in os.walk(f"{dir_path}/{dir_name}"):
                    for filename in filenames_in:
                        if filename.endswith('.txt'):
                            counted_dict = self.file_handler.read_file_count_letters(f"{dir_path_in}/{filename}")
                            model.append_language(dir_name, counted_dict)
                            self.keys.add(dir_name)
        return model

    def train(self, resource_path, iteration_count=15, learning_rate=0.01):
        data_model_list = self.walk_through_languages(resource_path)
        self.data_school = Data_School(len(data_model_list.language_model.keys()), data_model_list, learning_rate,
                                       iteration_count)
        self.data_school.train()
        return self.keys

    def test(self, resource_path):
        test_model_list = self.walk_through_languages(
            resource_path)
        self.data_school.test(test_model_list)
        return self.data_school.accuracy()

    def custom_text(self, text, name):
        custom_path = "/Users/juliadebecka/Documents/GitHub/NAI/Language_Classifier/Single_Layer_Network/Resources/Custom/Custom/cutom.txt"
        f = open(custom_path, "w+")
        f.write(text)
        f.close()
        custom_dir_path = "/Users/juliadebecka/Documents/GitHub/NAI/Language_Classifier/Single_Layer_Network/Resources/Custom/"
        test_model_list = self.walk_through_languages(custom_dir_path)
        prediction = self.data_school.test_custom_text(test_model_list)
        return prediction




