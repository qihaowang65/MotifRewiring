import os
import sys
import time

start = time.time()
data = sys.argv[1]
query =sys.argv[2]

cmd = "./ri36 ind gfd " + query + " " + query + " results.log > dummy.txt"

os.system(cmd)

with open("dummy.txt","r") as fp:
	lines = fp.readlines()

#Get the size of motif
k = int(lines[0])

raw = []
for _ in range(k):
	raw.append([])

for i in range(2,len(lines)):
	current = lines[i].split(' ')
	for j in range(k):
		raw[j].append(int(current[j]))

orbit = []
for each in raw:
	orbit.append(min(each))


norbits = len(set(orbit))
remapping = {}
current = 0
for each in orbit:
	if each not in remapping:
		remapping[each] = current
		current += 1
temp = []
for each in orbit:
	temp.append(remapping[each])

orbit = temp

del lines
del raw

def HandleOneEdge(edge,orbit,norbits,k,matching):
	nodes = edge.split(" ")
	node_orbits = [[] for _ in range(norbits)]
	for i in range(k):
		node_orbits[orbit[i]].append(int(nodes[i]))
	temp = []
	for each in node_orbits:
		temp += sorted(each)

	matching.append(temp)

def indices_to_str(line):
	out_str = ""
	for each_number in line:
		out_str += str(each_number)
		out_str += " "
	out_str += "\n"
	return out_str

output_file = query.split('.')[0] + ".edge"

cmd = "./ri36 ind gfd " + data + " " + query + " results.log > dummy.txt"
os.system(cmd)


with open(output_file,'w+') as out:
	with open("dummy.txt",'r') as fp:
		first_line = fp.readline()
		n = int(first_line)
		first_line = fp.readline()
		matching = []
		current_line = fp.readline()
		while (current_line):
			HandleOneEdge(current_line,orbit,norbits,k,matching)
			current_line = fp.readline()

	matching_set = set(tuple(x) for x in matching)
	matching = [list(x) for x in matching_set]
	out.write(indices_to_str(orbit))
	out.write(str(n))
	out.write("\n")
	out.write(str(k))
	out.write("\n")
	for each_line in matching:
		out.write(indices_to_str(each_line))

with open('time.log','a+') as fp:
	end = time.time() - start
	s = ''
	s += output_file
	s += ':'
	s += str(end)
	s += '\n'
	fp.write(s)
