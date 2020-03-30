import pandas as pd

from Data.Vector import Vector


class VectorList:
    def __init__(self):
        self.vectorList = []

    def read_and_create_vector(self, fileCSV):
        data = pd.read_csv(fileCSV)
        for index, row in data.iterrows():
            vector_set = [row["x"], row["y"], row["z"], row["w"]]
            self.vectorList.append(Vector(row["class"], vector_set))

    def print_data(self):
        for vec in self.vectorList:
            print(f"{vec.className} {vec.vectorSet}")