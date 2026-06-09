class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> numberTracker;
        for(size_t i(0); i< nums.size(); i++){
            if((numberTracker.insert(nums[i])).second == false){
                return true;
            }
        }return false;



    }
};