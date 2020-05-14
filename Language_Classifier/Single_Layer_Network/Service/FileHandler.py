import string


class FileHandler:

    # specify what alphabet you want. Adjusting to languages with different letters
    def __init__(self, alphabet):
        self.alphabet = alphabet

    # input: filepath of .txt file
    # output: Dictionary (letter : # of occurrences)
    # reads file and counts occurrences of each letter
    def read_file_count_letters(self, filepath):
        dictLetters = dict.fromkeys(self.alphabet)
        with open(filepath) as fp:
            file = fp.read()

            for letter in self.alphabet:
                file_as_list = file.count(letter.upper().lower())
                dictLetters[letter] = file_as_list
        return dictLetters
