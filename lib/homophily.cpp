#include "homophily.h"

NestedMap HomophilyRewire(vector<int*>& all_motifs,vector<int>orbit,int N){
    NestedMap adj;
    int k = orbit.size();
    unordered_map<int,vector<int>> orbit_member;
    for (int i = 0; i < k;i++){
        auto it = orbit_member.find(orbit[i]);
        if (it != orbit_member.end()){
            it->second.push_back(i);
        }
        else{
            vector<int> temp;
            temp.push_back(i);
            orbit_member[orbit[i]] = temp;
        }
    }
    vector<pair<int,int>> selection;
    for (auto it = orbit_member.begin(); it != orbit_member.end(); it++){
        vector<int> current = it->second;
        for (int i = 0; i < current.size(); i++){
            for (int j = 0; j < current.size();j++){
                if (i != j){
                    selection.push_back(make_pair(current[i],current[j]));
                }
            }
        }
    }

    int M = all_motifs.size();
    for (int i = 0; i < M; i++){
        int* current = all_motifs[i];
        for (int j = 0; j < selection.size(); j++){
            pair<int,int> s = selection[j];
            int src = current[s.first];
            int dst = current[s.second];
            adj.increment(src,dst);
        }

        for (int j =0; j < k; j++){
            int src = current[j];
            int dst = i + N;
            adj.increment(src,dst);
            adj.increment(dst,src);
        }
    }


    return adj;
}

