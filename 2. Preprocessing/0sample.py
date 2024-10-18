import numpy as np
import random
import sys
from copy import copy

input_file = str(sys.argv[1])
size = int(sys.argv[2])

neighbor = {}
adj = {}
with open(input_file,"r") as fp:
	lines = fp.readlines()


largest = -1

spliter = ' '
if '\t' in lines[0]:
	spliter = '\t'
elif ',' in lines[0]:
	spliter = ','

for each_line in lines:
	src,dst = each_line.split(spliter)
	src = int(src)
	dst = int(dst)
	if src > largest:
		largest = src
	if dst > largest:
		largest = dst
	if src not in neighbor:
		neighbor[src] = [dst]
	else:
		neighbor[src].append(dst)
	if dst not in neighbor:
		neighbor[dst] = [src]
	else:
		neighbor[dst].append(src)
	if src not in adj:
		adj[src] = [dst]
	else:
		adj[src].append(dst)



def add_one_more_node(ret_nodes,neighbor_nodes,neighbor):
	for i in range(0,50):
		newnode = random.choice(neighbor_nodes)
		if newnode not in ret_nodes:
			ret_nodes.append(newnode)
			neighbor_nodes = neighbor_nodes + neighbor[newnode]
			return True
	return False


first = random.randint(0,largest-1)
ret_nodes = [first]
neighbor_nodes = copy(neighbor[first])


while(len(ret_nodes) < size):
	if (add_one_more_node(ret_nodes,neighbor_nodes,neighbor) == False):
		first = random.randint(0,largest-1)
		ret_nodes = [first]
		neighbor_nodes = copy(neighbor[first])

def connection(ret_nodes,adj):
	k = len(ret_nodes)
	connectivity = np.zeros((k,k))
	for i in range(k):
		src = ret_nodes[i]
		for j in range(k):
			dst = ret_nodes[j]
			if src in adj:
				if dst in adj[src]:
					connectivity[i][j] = 1
	return connectivity


connectivity = connection(ret_nodes,adj)
k = len(ret_nodes)
out_file = input_file.split('.')[0] + "_" + str(sys.argv[2])+".txt"
with open(out_file,"w+") as fp:
	for i in range(k):
		for j in range(k):
			if (connectivity[i][j] == 1):
				outstr = str(i) + " " + str(j) + "\n"
				fp.write(outstr)




