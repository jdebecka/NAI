# import numpy as np
import matplotlib.pyplot as plt
from Service import DataReader
from Service.K_Means_Algo import K_means

data = DataReader.read_and_save('/Users/juliadebecka/Documents/GitHub/NAI/K-Means/Resources/iris.data')
data.normalize()

k_means = K_means(data, 3)

k_means.train()

k_means.plot()