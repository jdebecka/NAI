from Data.VectorList import VectorList
from Data.Vector import Vector


class KnnAlgorithm:
    def __init__(self, dataSet: VectorList, testSet: VectorList):
        self.dataSet = dataSet
        self.testSet = testSet

    def knn_algorithm(self, k=0, vectors_to_test=None):
        list_distance_class = []

        if vectors_to_test is None:
            vectors_to_test = self.testSet
        if k == 0 or k > len(self.dataSet.vectorList):
            k = len(self.dataSet.vectorList)

        if vectors_to_test.__class__ is VectorList:
            all_the_test = []
            index = 0
            accuracy_for_group = 0

            for vector_test in vectors_to_test.vectorList:
                for vector_data in self.dataSet.vectorList:
                    list_distance_class.append([vector_test.distance(vector_data.vectorSet), vector_data.className])

                list_distance_class.sort()
                accuracy_for_group += is_accurate(vector_test, list_distance_class[:k])
                all_the_test.append(list_distance_class[:k])
                list_distance_class.clear()
                index += 1
            group_accuracy(index, accuracy_for_group)
            return all_the_test
        else:
            for vector_data in self.dataSet.vectorList:
                list_distance_class.append([vectors_to_test.distance(vector_data.vectorSet), vector_data.className])

        list_distance_class.sort()
        acc = is_accurate(vectors_to_test, list_distance_class[:k])
        print(group_accuracy(1, acc))
        return list_distance_class[:k]


def repeat_the_most(listOfNeighbours):
    count_repeat = 0
    max_count = 0
    kind_checked = []
    kind = listOfNeighbours[0][1]

    for i in range(0, len(listOfNeighbours)):
        if kind_checked.__contains__(kind):
            continue
        else:
            kind_checked.append(listOfNeighbours[i][1])
        for j in range(i + 1, len(listOfNeighbours) - 1):
            if listOfNeighbours[i][1] == listOfNeighbours[j][1]:
                count_repeat += 1
        if count_repeat > max_count:
            max_count = count_repeat
            kind = listOfNeighbours[i][1]
        count_repeat = 0
    return kind


def group_accuracy(groupSize, correct):
    print(correct / groupSize * 100)


def is_accurate(testSubject: Vector, listOfNeighbours):
    predicted_kind = repeat_the_most(listOfNeighbours)

    if testSubject.className == predicted_kind:
        return 1
    else:
        return 0
