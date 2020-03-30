from Data.VectorList import VectorList
from Data.Vector import Vector
from Algorithm.KnnAlgorithm import KnnAlgorithm


class Main:
    def __init__(self):
        self.vector_list_data = VectorList()
        self.vector_list_test = VectorList()

    def data_file(self, filepath="/Users/juliadebecka/Documents/GitHub/NAI/KNN-Algo/Resources/iris.data"):
        self.vector_list_data.read_and_create_vector(filepath)
        print(filepath)

    def test_file(self, filepath="/Users/juliadebecka/Documents/GitHub/NAI/KNN-Algo/Resources/iris-test.data"):
        self.vector_list_test.read_and_create_vector(filepath)
        print(filepath)

    def initialize_knn(self):
        self.knn_algorithm_obj = KnnAlgorithm(self.vector_list_data, self.vector_list_test)

    def test_custom(self, list_float, k=0):
        self.data_file()
        self.initialize_knn()
        vec = Vector("None", list_float)
        return self.knn_algorithm_obj.knn_algorithm(k, vec)

    def test(self, k=0):
        self.initialize_knn()
        return self.knn_algorithm_obj.knn_algorithm()
