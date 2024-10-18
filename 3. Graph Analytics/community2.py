import numpy as np 
import sys
import pickle
from sklearn.cluster import KMeans
from scipy.stats import entropy
import pandas as pd
import networkx as nx


filename = sys.argv[1]
clusters = int(sys.argv[2])


with open(filename,"rb") as fp:
	n,embeddings = pickle.load(fp)

indices = []
val = [False for _ in range(n)]
X = []
for each in embeddings:
    indices.append(each)
    val[each] = True
    X.append(embeddings[each])


kmeans = KMeans(n_clusters=clusters, random_state=0, n_init="auto").fit(X)

ret = kmeans.labels_
final = {}
for i in range(len(ret)):
	current = ret[i]
	if current not in final:
		final[current] = []
	final[current].append(indices[i])

original = filename.split("_")[0] + ".mtx"
edges = []
with open(original,"r") as fp:
    lines = fp.readlines()
for each in lines:
    dummy = each.split(' ')
    a = int(dummy[0])
    b = int(dummy[1])
    if val[a] and val[b]:
        edges.append((a,b)) 


raw = []
for each in final:
	raw.append(final[each])

G = nx.from_edgelist(edges)
print(nx.community.modularity(G,raw))
