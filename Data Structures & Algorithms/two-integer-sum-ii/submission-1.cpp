class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        size_t i {0};
        size_t j {numbers.size() - 1};
        int sum{0};
        vector<int> indices;
        while(i < j){
            sum = numbers[i] + numbers[j];
            if(sum == target){
                indices = {i + 1, j + 1};
                return indices;
            }else if(sum > target){
                j--;
            }else if(sum < target){
                i++;
            }
        }
        return indices;
    }
};
