class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> occurances;
        int complement;
        for(int i = 0; i <= nums.size(); i++){
            complement = target - nums[i];
            if (occurances.contains(complement)){
                return {occurances[complement], i};
            }
            occurances[nums[i]] = i;
        } 
    }
};
