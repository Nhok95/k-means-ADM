from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


data = pd.read_csv("housing.csv");

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X);