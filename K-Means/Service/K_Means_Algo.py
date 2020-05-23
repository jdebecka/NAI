import random
import numpy as np
from Model.Vector_K_means import Vector_K_means
import math
import statistics
import matplotlib.pyplot as plt


def calculate_distance(cluster, vec):
    sum_all = 0
    for c, v in zip(cluster, vec):
        sum_all += pow((c - v), 2)
    return math.sqrt(sum_all)


class K_means:

    def __init__(self, data: Vector_K_means, k):
        self.data = data
        self.k = k
        self.clusters = list(list())
        self.data_list = list()
        self.dick_labels_min_dis = dict()
        self.clustering = dict()
        self.index_it = 0

    def train(self):
        self.transform_data()
        moved = True
        while moved:
            self.assign_clusters()
            moved = self.move_clusters()
        self.print_members()

    def print_cluster_data(self, cluster_data: dict):

        print("-------------- Iteration: ", self.index_it, "--------------")
        self.index_it += 1
        for key in cluster_data:
            list_values = cluster_data.get(key)
            # label_value = labels.get(key)

            avg = statistics.mean(map(lambda x: x[1], list_values))

            print("--------Class:", key, "--------")
            print("Average distance from cluster: ", avg)


            

            # index = 0
            # for value, label in zip(list_values, label_value):
            #     v, distance = value
            #     print('Actual label:', label, "--Vector:", v, "distance from cluster:", distance, "--")
            #     index += 1

    def print_members(self):
        print("----------- Summary -----------")
        for key in self.dick_labels_min_dis:
            print("--", key, "--")
            print(self.dick_labels_min_dis.get(key), len(self.dick_labels_min_dis.get(key)))

    def assign_clusters(self):
        self.clustering = dict()
        self.dick_labels_min_dis = dict()
        cluster_data = dict()
        index = 0
        for one_vec in self.data_list:
            cluster_lbl = 0
            min_cluster_lbl = 0
            cluster_min_distance = 0
            for cluster in self.clusters:
                if cluster_lbl == 0:
                    cluster_min_distance = calculate_distance(cluster, one_vec)
                else:
                    new_distance = calculate_distance(cluster, one_vec)
                    if new_distance < cluster_min_distance:
                        cluster_min_distance = new_distance
                        min_cluster_lbl = cluster_lbl
                cluster_lbl += 1

            if min_cluster_lbl not in self.clustering:
                cluster_data[min_cluster_lbl] = list(tuple())
                self.dick_labels_min_dis[min_cluster_lbl] = list()
                self.clustering[min_cluster_lbl] = list()

            self.clustering[min_cluster_lbl].append(one_vec)
            cluster_data[min_cluster_lbl].append((one_vec, cluster_min_distance))
            self.dick_labels_min_dis[min_cluster_lbl].append(self.data.class_vec[index])
            index += 1
        self.print_cluster_data(cluster_data)

    def move_clusters(self):
        moved = False

        for key in self.clustering:
            cluster_before = self.clusters[key]
            index = 0
            cluster = self.clustering.get(key)
            cluster = np.transpose(cluster)
            for row in cluster:
                move = cluster_before[index]
                cluster_before[index] = statistics.mean(row)
                move -= cluster_before[index]
                if move != 0:
                    moved = True
                index += 1
        return moved

    def transform_data(self):
        keys = len(self.data.coordinate_dick.keys())
        len_vec = len(self.data.class_vec)
        counter_j = 0

        self.data_list = np.zeros((len_vec, keys))
        self.clusters = [[random.random() for _ in range(keys)] for _ in range(self.k)]

        for key in self.data.coordinate_dick.keys():
            counter_i = 0
            for value in self.data.coordinate_dick.get(key):
                self.data_list[counter_i][counter_j] = value
                counter_i += 1

            counter_j += 1

    def plot(self):
        colors = ['red', 'blue', 'orange', 'purple', 'pink', 'black', 'light blue']
        fig, ax = plt.subplots(2)
        for key in self.clustering.keys():
            vec = self.clustering.get(key)
            vec = np.transpose(vec)

            ax[0].scatter(vec[0], vec[2], s=50, c=colors[key])
            ax[0].scatter(self.clusters[key][0], self.clusters[key][2], c=colors[key], s=300, alpha=0.7)

            ax[1].scatter(vec[1], vec[3], s=50, c=colors[key])
            ax[1].scatter(self.clusters[key][1], self.clusters[key][3], c=colors[key], s=300, alpha=0.7)

        ax[0].legend()
        ax[0].grid(True)
        ax[1].legend()
        ax[1].grid(True)

        plt.show()
