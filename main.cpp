#include <stdio.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <chrono>
#include "lib/nestedmap.h"
#include "lib/matrixrewire.h"
#include "lib/homophily.h"

using namespace std;
bool weighted = false;

/*
Usage:
	A function to print correct usage of the program
	Input:
		None
	Output:
		Print the correct usage to stdout
	Return value: 
		None
*/
void usage(){
	cout << "Windows Usage: main.exe [EdgeFile] [Algorithm] [Rewiring Pattern if Algorithm = 1] [Output filename]"<<endl;
	cout << "Linux Usage: ./main [EdgeFile] [Algorithm] [Rewiring Pattern if Algorithm = 1] [Output filename]"<<endl;
	cout << "Algorithm 0: Clique-based Rewiring; Algorithm 1: Use Input Rewiring Matirx; Algorithm 2: Homophily-oriented Rewiring" <<endl;
}

/*
count_time:
	A function to compute time elapsed since start time
	Input:
		Start_time: the starting time
	Output: 
		None
	Return value: 
		The time elapsed in seconds after the start time
*/
double count_time(chrono::steady_clock::time_point start_time){
	chrono::steady_clock::time_point my_time = std::chrono::steady_clock::now();
	int time_in_ms =std::chrono::duration_cast<std::chrono::microseconds>(my_time - start_time).count();
	double time_in_sec = double(time_in_ms)/1000000;
	return time_in_sec;
}

int main(int argc, char ** argv){
	if (argc != 5 && argc != 4){
		usage();
		return -1;
	}

	chrono::steady_clock::time_point start_time = std::chrono::steady_clock::now();
	string filename = string(argv[1]);
	int algorithm = stoi(string(argv[2]));


	string line;
	ifstream myfile(filename);
	vector<int*> all_motifs;
	vector<int> orbits;
	int N,M,k;
	if (myfile.is_open()){
		getline(myfile,line);
		istringstream is(line);
		int ob;
		while (is >> ob){
			orbits.push_back(ob);
		}
		getline(myfile,line);
		N = stoi(line);
		getline(myfile,line);
		k = stoi(line);
		while(getline(myfile,line)){
			istringstream is(line);
			int number;
			int* motif_edge = new int[k];
			int counter = 0;
			while(is >> number){
				motif_edge[counter] = number;
				counter++;
			}
			all_motifs.push_back(motif_edge);
		}
	}else{
		cout << "Unable to open the file." << endl;
		return -1;
	}
	myfile.close();
	chrono::steady_clock::time_point finish_reading_time = std::chrono::steady_clock::now();
	M = all_motifs.size();
	//Finish reading input files
	NestedMap adj;
	if (algorithm == 0){
		vector<pair<int,int>> selection;
		for (int i = 0; i < k; i++){
			for (int j = 0; j < k; j++){
				if (i != j){
					selection.push_back(make_pair(i,j));
				}
			}
		}
		adj = MatrixRewire(all_motifs,selection);
	}else if (algorithm == 1){
		string pattern = string(argv[3]);
		ifstream myfile(pattern);
		vector<vector<int>> position;
		if (myfile.is_open()){
			for (int i = 0; i < k; i++){
				getline(myfile,line);
				istringstream is(line);
				vector<int> temp;
				int number;
				while(is >> number){//Get the number
					temp.push_back(number);
				}
				position.push_back(temp);
			}
		}else{
			cout << "Could not find rewiring matrix file." << endl;
			return -1;
		}
		myfile.close();
		vector<pair<int,int>> selection;
		for (int i = 0; i < k; i++){
			for (int j = 0; j < k; j++){
				if (position[i][j] != 0){
					selection.push_back(make_pair(i,j));
				}
			}
		}
		adj = MatrixRewire(all_motifs,selection);
	}else if (algorithm == 2){
		adj = HomophilyRewire(all_motifs,orbits,N);
	}else{
		cout << "Wrong algorithm number. Please select from 0 to 2." << endl;
	}


	


	if (argc == 5){
		string outfile = string(argv[4]);
		adj.output(outfile,weighted);
	}else{
		string outfile = string(argv[3]);
		adj.output(outfile,weighted);
	}


	auto total_time = count_time(start_time);
	cout << "Total running time in graph " << filename << " with algorithm " << algorithm << " is " << total_time << endl;

	return 0;
}
