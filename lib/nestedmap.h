/*
A nested map class used to store adjacency matrix
*/
#ifndef NESTEDMAP_H
#define NESTEDMAP_H

#include <unordered_map>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

class NestedMap{
	public:
		NestedMap();//Constructor
		~NestedMap();
		void write(int idx1, int idx2, int val);//Wreite the value to (idx1,idx2)
		void increment(int idx1, int idx2);//Increase the value of (idx1,idx2) by 1
		void output(string file, bool weight);//Output the adjacency as a file
		int read(int idx1, int idx2);//Read the value at the given index
	private:
		unordered_map<int,unordered_map<int,int>> content;//The main nested map object
};


#endif