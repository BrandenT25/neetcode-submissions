class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        std::unordered_map<char, int> freqTable;

        for(const auto& c : s){
            freqTable[c]++;
        }

        for(const auto& c : t){
            freqTable[c]--;
        }
        for(const auto& value : freqTable){
            if(value.second != 0){
                return false;
            }
            return true;
        }

    }
};
