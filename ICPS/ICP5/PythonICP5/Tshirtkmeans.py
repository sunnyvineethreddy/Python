import numpy as np
import matplotlib.pyplot as plt
import random

# Create clusters randomly with initial centroids
def create_cluster(X, centroid_pts):
    cluster = {}
  # here we are using order 1 to calculate normalized distance
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroid_pts[i[0]]))for i in enumerate(centroid_pts)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

# Creates new clusters with new centroids after each iteration
def calculate_new_center(cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu
 # Matches with old centroids and if they are equal, the iteration stops
def matched(new_centroids, old_centroids):
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))
#  Applying K means
def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.
    old_centroids = np.random.randint(N, size = K)
    old_centroid_pts = np.array([X[i]for i in old_centroids])
    print("old :",old_centroids)
    print(old_centroid_pts)
    cluster_info = create_cluster(X, old_centroid_pts)
    print("Initial cluster information:")
    print(cluster_info)
    new_centroid_pts=calculate_new_center(cluster_info)
    print("new :", new_centroid_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    plot_cluster(old_centroid_pts,cluster_info,itr)
    while not matched(new_centroid_pts, old_centroid_pts): # Loop runs till the old centriod points matches with new centroid points
        itr = itr + 1
        old_centroid_pts = new_centroid_pts
        cluster_info = create_cluster(X,new_centroid_pts)
        plot_cluster(new_centroid_pts, cluster_info,itr)
        new_centroid_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    plot_cluster(new_centroid_pts, cluster_info, itr)
    return
# Plot the cluster with the values passed
def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()
# Prints the graph with the height and weight arguments
def init_graph(N, height, weight):
    X = np.array([(random.choice(height),random.choice(weight))for i in range(N)])
    return X

def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    #N = int(input('Enter the number of points.......'))
    K = int(input('Enter the number of Clusters.......'))
    print('Now Enter the bounds for choosing uniform value....\n')
    height = [5.5, 5.6,5.7,5.8,5.9,6, 6.1,6.2,6.3,6.4]
    weight = [45,50,52,53,59,63,69,75,89,90]
    X = init_graph(len(height),height, weight)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()
    temp = Apply_Kmeans(X, K, len(X))


if __name__ == '__main__':
    Simulate_Clusters()