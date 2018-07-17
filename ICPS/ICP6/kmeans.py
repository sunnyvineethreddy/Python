import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
# Read the data file
X = pd.read_csv("C:\\Users\\sunny\\OneDrive\\Desktop\\Python\\Python_Lesson6\\Python_Lesson6\\sample_stocks.csv")
X= np.array(X)
# Assigniung the cluster size
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

colors = ["g.","r.","c.","y."]

for i in range(len(X)):
    #print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.show()
"""
Elbow Method - Technique to determine the K
Location of a bend (knee) in the plot is generally considered as an indicator of the appropriate number of clusters.

SSE --> Sum Of Squared Errors

Plot a line graph of the SSE for each value of k. 
If the line graph looks like an arm - a red circle in below line graph (like angle), 
the "elbow" on the arm is the value of optimal k (number of cluster). 
Here, we want to minimize SSE. SSE tends to decrease toward 0 as we increase k 
(and SSE is 0 when k is equal to the number of data points in the dataset, 
because then each data point is its own cluster, and there is no error between it and the center of its cluster).

So the goal is to choose a small value of k that still has a low SSE, and the elbow usually represents 
where we start to have diminishing returns by increasing k.
"""
distortions = {}
# Selecting k in range of 1 to 10
for k in range(1,10):
    kmeans = KMeans(n_clusters=k).fit(X)
    # Inertia: Sum of distances of samples to their closest cluster center
    distortions[k] = kmeans.inertia_

plt.plot(list(distortions.keys()), list(distortions.values()))
plt.show()