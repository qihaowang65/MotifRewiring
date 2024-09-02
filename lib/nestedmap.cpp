#include "nestedmap.h"

NestedMap::NestedMap(){
}

NestedMap::~NestedMap(){
	for (auto it = content.begin(); it != content.end(); it++){
		it->second.clear();
	}
	content.clear();
}

void NestedMap::write(int idx1, int idx2, int val){
	auto it = content.find(idx1);
	if (it != content.end()){//Find the first key
		auto itt = it->second.find(idx2);
		if (itt != it->second.end()){//Find the second key
			itt->second = val;
		}else{//Only find the first key
			it->second[idx2] = val;
		}
	}else{//Do not find the first key
		unordered_map<int,int> newmap;
		newmap[idx2] = val;
		content[idx1] = newmap;
	}
	return;
}

void NestedMap::increment(int idx1, int idx2){
	auto it = content.find(idx1);
	if (it != content.end()){//Find the first key
		auto itt = it->second.find(idx2);
		if (itt != it->second.end()){//Find the second key
			itt->second += 1;
		}else{//Only find the first key
			it->second[idx2] = 1;
		}
	}else{//Do not find the first key
		unordered_map<int,int> newmap;
		newmap[idx2] = 1;
		content[idx1] = newmap;
	}
	return;
}

int NestedMap::read(int idx1, int idx2){
	auto it = content.find(idx1);
	if (it == content.end()){
		return -1;
	}
	auto itt = it->second.find(idx2);
	if (itt == it->second.end()){
		return -1;
	}
	return itt->second;
}

void NestedMap::output(string file,bool weighted = false){
	ofstream stream(file);
	for (auto it = content.begin(); it != content.end(); it++){
		int src = it->first;
		for (auto itt = it->second.begin(); itt != it->second.end();itt++){
			int dst = itt->first;
			int weight = itt->second;
			if (weighted){
				stream << src << " " << dst << " " << weight << endl;
			}else{
				stream << src << " " << dst << endl;
			}
		}
	}
	stream.close();
}

