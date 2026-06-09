class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> lookup;
        for(size_t i{0}; i < nums.size(); i++){
            lookup[nums[i]] += 1;
            if(lookup[nums[i]] > 1){
                return true;
            }
        }
        return false;
    }
};