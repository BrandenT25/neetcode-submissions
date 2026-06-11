class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqTable;
        for(size_t i{0}; i < nums.size(); ++i){
            freqTable[nums[i]]++;
        }
        int n = nums.size() + 1;
        vector<vector<int>> buckets(n);
        for (const auto& [key, value]: freqTable){
            buckets[value].push_back(key);
        }
        vector<int> result;
        for (size_t i{buckets.size()}; i > 0; --i){
            for(size_t j{0}; j < buckets[i - 1].size(); ++j){
                if(result.size() < k){
                    result.push_back(buckets[i - 1][j]);
                }else{
                    return result;
                }
            }
        }
        return result;
    }
};
