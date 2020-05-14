from Model.Language_Model import Language_Model


class Model_list:
    def __init__(self):
        self.language_model = dict()

    def append_language(self, language, letter_dictionary):
        if language in self.language_model.keys():
            model = self.language_model.get(language)
            model.add_dictionary(letter_dictionary)
        else:
            self.language_model[language] = Language_Model(language, letter_dictionary)
