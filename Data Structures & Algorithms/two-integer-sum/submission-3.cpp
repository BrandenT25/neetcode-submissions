
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        size_t index(0);
        vector<int> indices;
        std::unordered_map<int, size_t> numsValues;
        while(index < nums.size()){
            if(numsValues.find(target - nums[index]) == numsValues.end()){
                numsValues[nums[index]] = index;
                index++;
            }else{
                indices.push_back(numsValues[target - nums[index]]);
                indices.push_back(index);
                return indices;
            }
        }
    }
};