# import libraries
import xlrd
import csv
import pandas as pd
import matplotlib.pylab as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# load data from excel file and store it in csv file.
with xlrd.open_workbook('Synapticparameters 2D.xlsx') as wb:
    sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
    with open('parameter2D.csv', 'wb') as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))

parameter2D = pd.read_csv('parameter2D.csv', sep=',')
parameter2D = StandardScaler().fit_transform(parameter2D)
# set parameters for PCA, use PCA to analyze Parameter2D
pca = PCA(n_components=7, whiten=False)
# Fit the model with parameter2D and apply the dimensionality reduction on parameter2D
new_parameter2D = pca.fit_transform(parameter2D)
ratio = pca.explained_variance_ratio_
print ratio
# Get the figure of variance ratio
plt.bar(range(1, 7), ratio[0:6], alpha=0.5, align='center', label='individual explained variance')
plt.title('Principle component ratio')
plt.xlabel('principle component')
plt.ylabel('explained variance ratio')
plt.savefig('Synaptic_explained_variance_ratio.png')
plt.show()
