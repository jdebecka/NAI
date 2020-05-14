# import numpy as np
import matplotlib.pyplot as plt
from Service import DataReader

data = DataReader.read_and_save('/Users/juliadebecka/Documents/GitHub/NAI/K-Means/Resources/iris.data')
xs = []
ys = []
zs = []
store_label = []

for item in data:
    store_label.append(item.vec_name)
    xs.append(item.coordinates[3])
    ys.append(item.coordinates[2])
    zs.append(item.coordinates[1])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xs, ys, zs, s=50, alpha=0.6, edgecolors='w')

ax.set_xlabel('Sepal length')
ax.set_ylabel('Pedal length ')
ax.set_zlabel('Pedal width')

fig.show()