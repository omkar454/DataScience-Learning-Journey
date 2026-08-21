import numpy as np
import matplotlib.pyplot as plt

# --- Generate Synthetic Dataset ---
np.random.seed(42)
data = np.random.rand(100, 2) * 10

# -------------------------------
# 🔹 K-Means Functions
# -------------------------------
def assign_clusters(data, centroids):
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def update_centroids(data, labels, K):
    return np.array([data[labels == i].mean(axis=0) for i in range(K)])

def compute_wcss(data, centroids, labels):
    wcss = 0
    for i in range(len(data)):
        centroid = centroids[labels[i]]
        wcss += np.linalg.norm(data[i] - centroid) ** 2
    return wcss

def kmeans(data, K, max_iters=100):
    centroids = data[np.random.choice(len(data), K, replace=False)]
    
    for _ in range(max_iters):
        labels = assign_clusters(data, centroids)
        new_centroids = update_centroids(data, labels, K)
        
        if np.all(centroids == new_centroids):
            break
            
        centroids = new_centroids
        
    return centroids, labels

# -------------------------------
# 🔹 ELBOW METHOD
# -------------------------------
wcss_values = []
K_range = range(1, 10)

for k in K_range:
    centroids, labels = kmeans(data, k)
    wcss = compute_wcss(data, centroids, labels)
    wcss_values.append(wcss)

# --- Plot Elbow Graph ---
plt.figure()
plt.plot(K_range, wcss_values, marker='o')

# 🔴 Highlight optimal K = 3
plt.axvline(x=3, linestyle='--')
plt.scatter(3, wcss_values[2], s=100)  # index 2 because K starts from 1

plt.title("Elbow Method (Optimal K = 3)")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.grid()

plt.show()

# -------------------------------
# 🔹 FINAL CLUSTERING (K = 3)
# -------------------------------
K = 3
centroids, labels = kmeans(data, K)

# --- Plot Clusters ---
plt.figure()
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200)
plt.title("K-Means Clustering (K=3)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid()
plt.show()