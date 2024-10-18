import numpy as np
import sys
import networkx as nx
import time
from orbit import Adjacency
from random import choices
import random
from tqdm import tqdm
import gensim
import pickle
from gensim.models import Word2Vec

def PrintError():
    print("Usage: python3 MDW.py [motif-edge file] [l]")


filename = sys.argv[1]
l = int(sys.argv[2])
matchings = []
end_file = filename.split('.')[0] + "_walk.pkl"
with open(filename,"r+") as fp:
    lines = fp.readlines()

roles = []
for each in lines[0].split():
	roles.append(int(each))

n = int(lines[1])
lines = lines[3:]
for each in lines:  
    map_obj = map(int,each.split())
    motif = list(map_obj)
    matchings.append(motif)

del lines
A = Adjacency(matchings,roles,n)


context = []
for _ in range(5):
	o = [i for i in range(n)]
	random.shuffle(o)
	for v in tqdm(o):
		temp = [v]
		A.SetStart(v)
		for x in range(l):
			temp.append(A.Next())
		context.append(temp)
		
model = Word2Vec(context,vector_size=16,sg=1)
wv = model.wv

embedding = {}
for i in range(n):
	if i in wv:
		embedding[i] = wv[i]

with open(end_file,"wb") as fp:
	pickle.dump([n,embedding],fp)


