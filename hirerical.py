import numpy as np
import matplotlib.pyplot as plt
x=[3,4,5,10,4,11,14,6,10,12]
y=[21,20,19,24,16,17,24,23,22,21]
len(x)
10
len(y)
10
plt.scatter(x,y)
plt.show()
from scipy.cluster.hierarchy import dendrogram,linkage
x=[3,4,5,10,4,11,14,6,10,12]
y=[21,20,19,24,16,17,24,23,22,21]
data=list(zip(x,y))
linkage_data=linkage(data,method="ward",metric="euclidean")
dendrogram(linkage_data)
plt.title("Dendrogram")