# Motif-based Rewiring
This project aims to perform graph rewiring based on motifs and apply downstream applications to the rewired graphs.
## Compile
The makefile is provided. You only need to compile the file with:
```bash
make
```
## Usage
To execute the program, please run
```bash
main.exe [Motif Edge File] [Algorithm] [Rewired Pattern if Algorithm is 1] [Output File Name]
```
For example, if the input file's name is "book.edge", we aim to perform homophily-oriented rewiring, and the output file should be book_rewire.txt, then we need to run
```bash
main.exe book.edge 2 book_rewire.txt
```
## Input Format
The input file should be a txt file. Its first line should be the node orbit information of the motif. The second line should be the size of motif and the third line indicates the number of nodes in the graph. Then each line will list all nodes in each motif edge. Nodes in the same edge will be separated by space. All duplicated edges should be removed if you need weighted edges. An example of input file (book_5.edge) is provided.

The input file for the rewired pattern should also be a txt file. It should have a k * k binary matrix, where k is the size of the motif. An example of rewired pattern (rewire.txt) is provided.

## Algorithm Number
Here is the list of algorithms:

0. Clique-based rewiring in existing works
1. Rewiring the graph based on the input matrix
2. Homophily-oriented rewiring.