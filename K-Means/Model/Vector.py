import math
import numpy as np
import string


class Vector:

    def __init__(self, vec_name, vector: list):
        self.vec_name = vec_name
        self.vectors = list()
        self.vectors.append(vector)

    def append_vector(self, vector):
        self.vectors.append(vector)


    # def normalize(self):
    #     self.vectors = np.transpose(self.vectors)
    #     min_V = np.amin(self.vectors)
    #     max_V = np.amax(self.vectors)
    #     for row in self.vectors:
    #


