class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
            if lookup[num] > 1:
                return True
        return False