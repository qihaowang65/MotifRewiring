LOOP = 0
import sys
#This file will convert directed graph into gfd file


filename = str(sys.argv[1])
outname = filename.split(".")[0] + ".gfd"
all_nodes = {}
vertex_all = []
number_of_edges = 0
with open(filename,'r') as fp:
    # do stuff with fp
    lines = fp.readlines()
if '\t' in lines[0]:
	spliter = '\t'
elif ',' in lines[0]:
	spliter = ','
else:
	spliter = ' '

for each_line in lines:
	src,dst = each_line.split(spliter)
	src = int(src)
	dst = int(dst)
	vertex_all.append(src)
	vertex_all.append(dst)

	if src == dst:
		if LOOP == 0:
			continue
	#Check the other direction:
	number_of_edges = number_of_edges + 1
	if src in all_nodes:
		all_nodes[src].append(dst)
	else:
		all_nodes[src] = [dst]

vertex_all = set(vertex_all)
number_of_vertices = len(vertex_all)

#Check
vertex_all = sorted(vertex_all)
node_mapping = {}
true_node = 0
for each_node in vertex_all:
	node_mapping[each_node] = true_node
	true_node = true_node + 1#

#for key in all_nodes:
#	print(all_nodes[key])
with open(outname,'w') as outfile:
	outfile.write("#Mygraph \n") #graph name
	outfile.write(str(number_of_vertices))
	outfile.write('\n')
	for i in range(number_of_vertices):
		outfile.write("a\n")
	outfile.write("%i" %(number_of_edges))
	outfile.write("\n")
	for each_node in all_nodes:
		results = all_nodes[each_node]
		for each_dst in results:
			true_dst = node_mapping[each_dst]
			true_src = node_mapping[each_node]
			outfile.write("%i " %true_src)
			outfile.write("%i \n" %true_dst)
			#outfile.write("%i " %true_dst)
			#outfile.write("%i \n" %true_src)

