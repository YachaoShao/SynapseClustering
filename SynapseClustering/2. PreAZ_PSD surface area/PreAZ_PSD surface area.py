# import libraries
import xlrd
import csv
import pandas as pd
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as sch
import matplotlib.pylab as plt
from scipy import stats
# load data from excel and save it to csv file
with xlrd.open_workbook('pre_synapse.xlsx') as wb:
    sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
    with open('pre_synapse_data_new.csv', 'wb') as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))

pre_synapse_data = pd.read_csv('pre_synapse_data_new.csv', sep=',')
# normalize the original dataset
synapse_data = stats.zscore(pre_synapse_data)
# Hierarchical classifying

# Cluster tree
Z = sch.linkage(synapse_data, method='ward')
# save image plot_dendrogram.png
P = sch.dendrogram(Z)

plt.title('Dendrogram of PreAzs and PSDs')
plt.xlabel('sample index')
plt.ylabel('distance')
plt.savefig('plot_preAZ_PSDs_cluster.png')
plt.show()

kmeans_data = synapse_data
kmeans = KMeans(n_clusters=2, random_state=111)
kmeans.fit(kmeans_data)
cluster_result = kmeans.labels_

LABEL_COLOR_MAP = {0 : 'r',
                   1 : 'b',
                   }

label_color = [LABEL_COLOR_MAP[l] for l in cluster_result]

plt.scatter(kmeans_data[:, 0], kmeans_data[:,1], s=40, c=label_color, linewidths=0)
plt.xlabel('PreAZs surface area')
plt.ylabel('PSDs surface area')
plt.title('Scatter plot of dataset using K-means')
plt.savefig('Scatter plot of dataset using K-means.eps', format='eps', dpi=1000)
plt.show()