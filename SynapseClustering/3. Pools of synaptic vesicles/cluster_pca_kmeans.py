# import libraries
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import scipy.cluster.hierarchy as sch
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn import cluster
from scipy.spatial import distance

# load data from csv file
synapse_data = pd.read_csv('synape_matrix.csv', sep=',')
synapse_data = StandardScaler().fit_transform(synapse_data)
print synapse_data.shape

# pca
pca = PCA(n_components=7, whiten=False)
synapse_data_new = pca.fit_transform(synapse_data)
print synapse_data_new.shape
ratio=pca.explained_variance_ratio_
plt.bar(range(1, 7), ratio[0:6], alpha=0.5, align='center', label='individual explained variance')
plt.title('Principle component ratio')
plt.xlabel('principle component')
plt.ylabel('explained variance ratio')
plt.savefig('plot_explained_variance_ratio.png')
plt.show()

#k-means

kmeans_data = synapse_data_new[:, 0:2]
print(kmeans_data)
kmeans = KMeans(n_clusters=3, random_state=111)
kmeans.fit(kmeans_data)
cluster_result = kmeans.labels_

LABEL_COLOR_MAP = {0 : 'r',
                   1 : 'g',
                   2 : 'c',
                   }

label_color = [LABEL_COLOR_MAP[l] for l in cluster_result]
plt.figure('K-means with 3 clusters')
plt.scatter(kmeans_data[:, 0], kmeans_data[:, 1], s=40, c=label_color, linewidths=0)
plt.savefig('K-means cluster results with using PCA')
plt.show()