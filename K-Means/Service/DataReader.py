import csv
from Model.Vector_K_means import Vector_K_means


def read_and_save(file_path):
    vector_obj = Vector_K_means()
    features: [float]
    class_name = ""
    with open(file_path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            features = []
            for value in row:
                try:
                    float_number = float(value)
                    features.append(float_number)
                except:
                    class_name = value
            vector_obj.add_vec(class_name, features)
    return vector_obj
