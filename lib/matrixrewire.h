/*
A matrix rewire solver for 
*/
#ifndef MATRIXREWIRE_H
#define MATRIXREWIRE_H

#include <unordered_map>
#include <vector>
#include <iostream>
#include "nestedmap.h"
using namespace std;

NestedMap MatrixRewire(vector<int*>& all_motifs,vector<pair<int,int>>selection);


#endif