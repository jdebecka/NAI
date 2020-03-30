import math


class Vector:
    def __init__(self, className, vectorSet):
        self.className = className
        self.vectorSet = vectorSet

    def distance(self, vectorCompare):
        distance_from_a_vector = 0.0
        index = 0
        for vector in vectorCompare:
            if self.vectorSet[index] is None:
                index += 1
                continue
            distance_argument = pow((self.vectorSet[index] - vector), 2)
            distance_from_a_vector += distance_argument
            index += 1

        return math.sqrt(distance_from_a_vector)
