class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while k > j:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    if [nums[i], nums[j], nums[k]] not in result: result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                if sum > 0:
                    k -= 1
                if sum < 0:
                    j += 1
        return result

# [-1, 0, 1, 2 , -1, -4] -> [-4, -1 , -1, 0, 1, 2] 
"""
i = 4
j = 




"""