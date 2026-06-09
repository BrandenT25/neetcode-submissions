class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occurances = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in occurances:
                return [occurances[complement], i]
            occurances[nums[i]] = i