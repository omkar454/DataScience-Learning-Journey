# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import scipy.cluster.hierarchy as sch

# 1. Load the Iris Dataset
iris = load_iris()
X = iris.data
y_true = iris.target # Loaded purely for final comparison, not for training

# 2. Apply PCA for Dimensionality Reduction (4D to 2D for visualization)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# ---------------------------------------------------------
# K-MEANS CLUSTERING & ELBOW METHOD
# ---------------------------------------------------------

# Calculate WCSS for the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow Method
plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='blue')
plt.title('Elbow Method For Optimal k (K-Means)')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

# Train K-Means with optimal k=3
kmeans_model = KMeans(n_clusters=3, init='k-means++', random_state=42, n_init=10)
y_kmeans = kmeans_model.fit_predict(X)


# ---------------------------------------------------------
# HIERARCHICAL CLUSTERING & DENDROGRAM
# ---------------------------------------------------------

# Generate and plot Dendrogram
plt.figure(figsize=(10, 5))
plt.title('Dendrogram for Hierarchical Clustering (Ward Linkage)')
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.xlabel('Iris Samples (Indices)')
plt.ylabel('Euclidean Distance')
plt.axhline(y=7.5, color='r', linestyle='--') # Theoretical cut line
plt.show()

# Train Agglomerative Hierarchical model with optimal k=3
hc_model = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
y_hc = hc_model.fit_predict(X)

# ---------------------------------------------------------
# SILHOUETTE SCORE COMPARISON GRAPH (K-Means vs Hierarchical)
# ---------------------------------------------------------
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans, AgglomerativeClustering

sil_scores_kmeans = []
sil_scores_hc = []

K_range = range(2, 11)

# Silhouette score is only defined for 2 or more clusters
for i in K_range:
    # 1. Calculate for K-Means
    kmeans_temp = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=10)
    y_kmeans_temp = kmeans_temp.fit_predict(X)
    sil_scores_kmeans.append(silhouette_score(X, y_kmeans_temp))
    
    # 2. Calculate for Hierarchical (Agglomerative)
    hc_temp = AgglomerativeClustering(n_clusters=i, metric='euclidean', linkage='ward')
    y_hc_temp = hc_temp.fit_predict(X)
    sil_scores_hc.append(silhouette_score(X, y_hc_temp))

# Plot both scores against k
plt.figure(figsize=(10, 5))
plt.plot(K_range, sil_scores_kmeans, marker='s', linestyle='-', color='blue', label='K-Means')
plt.plot(K_range, sil_scores_hc, marker='o', linestyle='--', color='darkorange', label='Hierarchical')

plt.title('Silhouette Score Comparison: K-Means vs Hierarchical')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Average Silhouette Score')
plt.legend()
plt.grid(True)
plt.show()
# ---------------------------------------------------------
# MATHEMATICAL EVALUATION
# ---------------------------------------------------------

# Calculate and print Silhouette Scores
sil_score_kmeans = silhouette_score(X, y_kmeans)
sil_score_hc = silhouette_score(X, y_hc)

print("\n--- Model Evaluation ---")
print(f"K-Means Silhouette Score:       {sil_score_kmeans:.4f}")
print(f"Hierarchical Silhouette Score:  {sil_score_hc:.4f}")

# ---------------------------------------------------------
# VISUAL COMPARISON USING PCA
# ---------------------------------------------------------

# Create a 1x3 subplot to compare True Labels vs K-Means vs Hierarchical
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: True Predefined Labels
axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y_true, cmap='viridis', s=60, edgecolor='k')
axes[0].set_title('Ground Truth (Predefined Target Labels)')
axes[0].set_xlabel('Principal Component 1')
axes[0].set_ylabel('Principal Component 2')

# Plot 2: K-Means Clustering Results
axes[1].scatter(X_pca[:, 0], X_pca[:, 1], c=y_kmeans, cmap='viridis', s=60, edgecolor='k')
axes[1].set_title('K-Means Clustering Results')
axes[1].set_xlabel('Principal Component 1')

# Plot 3: Hierarchical Clustering Results
axes[2].scatter(X_pca[:, 0], X_pca[:, 1], c=y_hc, cmap='viridis', s=60, edgecolor='k')
axes[2].set_title('Hierarchical Clustering Results')
axes[2].set_xlabel('Principal Component 1')

plt.tight_layout()
plt.show()