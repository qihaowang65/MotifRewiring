#include "matrixrewire.h"

NestedMap MatrixRewire(vector<int*>& all_motifs,vector<pair<int,int>>selection){
    NestedMap adj;
    for (int i = 0; i < all_motifs.size();i++){
        int* current = all_motifs[i];
        for (int j = 0; j < selection.size(); j++){
            pair<int,int> s = selection[j];
            int src = current[s.first];
            int dst = current[s.second];
            adj.increment(src,dst);
        }
    }
    return adj;
}