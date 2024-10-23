import numpy as np
import sys
import networkx as nx
import time
from random import choices
import random
from tqdm import tqdm
import gensim
import pickle
from gensim.models import Word2Vec

def PrintError():
    print("Usage: python3 MDW.py [edge file] [l]")


class Adjacency:
	def __init__(self,adj,n):
        #Initialize the directed motif graph
        #Input: motifs:  an M * k arrays of motif edges
        #       roles:   a length-k array indicating the node orbit of each motif 
        #       n:       number of nodes in graph
		self.n = n
		self.adj = adj

		self.current = random.randint(0,n-1)

	def Next(self):
		c = random.randint(0,99)
		if self.current not in self.adj or c >=90:
			self.current = random.randint(0,self.n-1)
		else:
			p = []
			w = []
			v = self.adj[self.current]
			for key in v:
				p.append(key)
				w.append(1)
			current = random.choices(p,w)[0]
			if current >= self.n: #We are at an auxiliary node
				p = []
				w = []
				v = self.adj[current]
				for key in v:
					p.append(key)
					w.append(v[key])
				current = random.choices(p,w)[0]
			self.current = current
		return self.current

	def SetStart(self,start):
		self.current = start


filename = sys.argv[1]
l = int(sys.argv[2])
end_file = filename.split('.')[0] + "_walk.pkl"
with open(filename,"r+") as fp:
    lines = fp.readlines()
adj = {}
for each in lines:
	dummy = each.split(' ')
	a = int(dummy[0])
	b = int(dummy[1])
	if a not in adj:
		adj[a] = [b]
	else:
		adj[a].append(b)

A = Adjacency(adj,len(adj))
n = len(adj)
context = []
for _ in range(3):
	o = [i for i in range(n)]
	random.shuffle(o)
	for v in tqdm(o):
		temp = [v]
		A.SetStart(v)
		for x in range(l):
			temp.append(A.Next())
		context.append(temp)

print(len(context))
model = Word2Vec(context,vector_size=16,sg=1)
wv = model.wv

embedding = {}
for i in range(n):
	if i in wv:
		embedding[i] = wv[i]

with open(end_file,"wb") as fp:
	pickle.dump([n,embedding],fp)


