import csv
from Model.Vector import Vector


def read_and_save(file_path):
    features: [float]
    class_name = ""
    data: [Vector] = []
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
            data.append(Vector(class_name, features))
    return data
