from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np

from Data_generator import choose_random_elements_from_CSV, transform_data_into_raw_format


class KMeans:
    def __init__(self, num_of_clusters):
        """
        just initialization we store num_of_clusters and empty centroids, clusters
        :param num_of_clusters: represents how many clusters should be created
        """
        self.num_of_clusters = num_of_clusters
        
        # the centers (mean feature vector) for each cluster
        self.centroids = []
        # list of sample indices for each cluster
        self.clusters = [[] for _ in range(self.num_of_clusters)]
        

    def predict(self, data):
        """
        Main loop of algorithm
        K-means consists of three steps
        1)assigning centroids
        2)assigning elements to centroids
        3)if converged stop
        we are doing this three steps in this method
        :param data: representation of data as np array
        :return: representation of data and which cluster they belong to after they converged
        """
        self.data = data
        self.number_of_elements = data.shape[0]
        self.dimensions_of_vectors = data.shape[1]

        # initialize first centroids with random vectors
        random_sample_idxs = np.random.choice(self.number_of_elements, self.num_of_clusters, replace=False)
        self.centroids = [self.data[idx] for idx in random_sample_idxs]

        old_centroids = self._one_cluster_step()

        while not (self._converged(old_centroids, self.centroids)):
            old_centroids = self._one_cluster_step()

    def _one_cluster_step(self):
        """
        does to steps of k-means algorithm
        1)assigning centroids
        2)assigning elements to centroids
        :return: old centroits before assignment
        """
        # Assign samples to closest centroids (create clusters)
        self.clusters = self._create_clusters(self.centroids)

        # Calculate new centroids from the clusters
        centroids_old = self.centroids
        self.centroids = self._new_centroids(self.clusters)

        return centroids_old

    def _create_clusters(self, centroids):
        """
        this method assigns every sample to the closest centroid
        :param centroids: numpy array containing info about centroids as vectors
        """
        new_clusters = [[] for _ in range(self.num_of_clusters)]
        for idx, sample in enumerate(self.data):
            centroid_idx = self._assign_centroid(sample, centroids)
            new_clusters[centroid_idx].append(idx)
        return new_clusters

    def _assign_centroid(self, elem, centroids):
        """
        this method assigns new closest centroid to element
        :param elem: element numpy vector
        :param centroids: centroids numpy array of vectors
        :returns new centroid locations
        """
        distances = [second_norm(elem, point) for point in centroids]
        closest_index = np.argmin(distances)
        return closest_index

    def _new_centroids(self, clusters):
        """
        this method gives centroids new values, just calculating mean of all vectors
        in one cluster and giving its value to appropriate centroid
        :param clusters: previous clusters
        """
        centroids = np.zeros((self.num_of_clusters, self.dimensions_of_vectors))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.data[cluster], axis=0)
            centroids[cluster_idx] = cluster_mean
        return centroids

    def _converged(self, centroids_old, centroids):
        """
        this method calculates distances between all previous centroids and current ones
        if no centroid changed location so if distance between all of them is 0 it converged
        therefore loop should stop warking, so I return true in another case I return false
        :param centroids_old: array of vectors where each element represent previous centroid location
        :param centroids: array of vectors where each element represent current centroid location
        """
        distances = [second_norm(centroids_old[i], centroids[i]) for i in range(self.num_of_clusters)]
        if all(item == 0 for item in distances):
            return True
        else:
            return False

    def display(self):
        """
            This method uses matplotlib library and
            displays all elements in apropriate cluster
            also it marks centroids with black x
        """
        fig, ax = plt.subplots(figsize=(12, 8))

        for i, index in enumerate(self.clusters):
            point = self.data[index].T
            ax.scatter(*point)

        for point in self.centroids:
            ax.scatter(*point, marker="x", color="black", linewidth=2)

        plt.show()


def second_norm(x1, x2):
    """
    calculates second norm of difference of two vectors, also called euclidian norm
    :param x1: first vector
    :param x2: second vector
    :return: second norm of vector x1-x2
    """
    return np.sqrt(np.sum((x1 - x2) ** 2))


if __name__ == "__main__":
    n = 40  # number of cities
    # Choosing random n cities
    x = choose_random_elements_from_CSV(n)
    # getting data about cities temperature and humidity !! computer should have access to internet
    y = transform_data_into_raw_format(x)

    clusters = 3

    k = KMeans(num_of_clusters=clusters)  # plot_steps_false
    x = k.predict(y)  # cluster using k-means algorithm
    k.display()  # display result with the help of matplotlib library
