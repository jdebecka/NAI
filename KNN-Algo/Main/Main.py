from Data.VectorList import VectorList
from Data.Vector import Vector
from Algorithm.KnnAlgorithm import KnnAlgorithm


def main():
    vector_list_data = VectorList()
    vector_list_test = VectorList()
    knn_algorithm_obj = KnnAlgorithm(vector_list_data, vector_list_test)
    vector_list_data.read_and_create_vector("/Users/juliadebecka/Desktop/4th semester/NAI/Resources/iris.data")
    vector_list_test.read_and_create_vector("/Users/juliadebecka/Desktop/4th semester/NAI/Resources/iris-test.data")

    vector_to_test = vector_list_test.vectorList[44]
    vec = Vector("Iris-Sentosa", [3, 2, None, 2, None])
    test = knn_algorithm_obj.knn_algorithm(100, vec)

    print(test)


if __name__ == "__main__":
    main()
