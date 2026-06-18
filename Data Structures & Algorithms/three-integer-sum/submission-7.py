class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for n in range(len(nums) - 2):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            ptr1 = n + 1
            ptr2 = len(nums) - 1
            while ptr2 > ptr1:
                sum = nums[n] + nums[ptr1] + nums[ptr2]
                if sum == 0:
                    result_nums = [nums[n], nums[ptr1], nums[ptr2]]
                    if result_nums not in result: result.append(result_nums) 
                    ptr1 += 1
                    ptr2 -= 1
                elif sum > 0:
                    ptr2 -= 1
                elif sum < 0:
                    ptr1 += 1
            n += 1
        return result
