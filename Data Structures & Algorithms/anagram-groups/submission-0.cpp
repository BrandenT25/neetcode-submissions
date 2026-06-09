class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        std::unordered_map<std::string, vector<std::string>> signatures;
        for(std::string& w: strs){
            vector<int> freqTable {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
            std::string freqKey {""};
            for(char& c: w){
                int signature(0);
                signature += (c - 'a');
                freqTable[signature]++ ;
            }
            for(int& i : freqTable){
                freqKey += to_string(i) + "#";
            }
            signatures[freqKey].push_back(w);
        }
        for(auto& entry: signatures){
            result.push_back(entry.second);
        }
        return result;
    }
};
