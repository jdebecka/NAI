import csv


def read_csv_data(file_path):
    model_class_dictionary = dict()
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            class_name = row[-1]
            features = row[:-1]
            if class_name not in model_class_dictionary:
                model_class_dictionary[class_name] = list()
            model_class_dictionary.get(class_name).append(features)
    return model_class_dictionary
