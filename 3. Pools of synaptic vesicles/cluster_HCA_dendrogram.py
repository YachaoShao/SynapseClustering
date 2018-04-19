### import libraries
import pandas as pd
import scipy.cluster.hierarchy as sch
import matplotlib.pylab as plt


# load data from csv file
synapse_data = pd.read_csv('synape_matrix.csv', sep=',')

# Computing distance
disMat = sch.distance.pdist(synapse_data,'euclidean')
# Cluter tree
Z = sch.linkage(disMat, method='average')
# calculate color threshold
k = 6
cl = Z[-(k-1), 2]
# save image plot_dendrogram.png
P = sch.dendrogram(Z,color_threshold=cl)

plt.title('Hierarchical Clustering Dendrogram of Synapses')
plt.xlabel('sample index')
plt.ylabel('euclidean distance')
plt.savefig('plot_dendrogram.png')
plt.show()