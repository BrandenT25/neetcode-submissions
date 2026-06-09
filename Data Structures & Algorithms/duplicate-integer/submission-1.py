class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for i in nums:
            values[i] = values.get(i, 0) + 1
            if values[i] > 1:
                return True
        return False


        