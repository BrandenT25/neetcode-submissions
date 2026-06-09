class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;
        if(s.size() != t.size()){
            return false;
        }
        for(size_t i{0}; i <= s.size(); i++){
            freq[s[i]] += 1;
        }
        for(size_t i{0}; i <= t.size(); i++){
            if (!(freq.contains(t[i])) || (freq[t[i]] == 0)){
                return false;
            }
            freq[t[i]] -= 1;
        }
        return true;
        


    }
};
