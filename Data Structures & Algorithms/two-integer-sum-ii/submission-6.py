class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers) - 1

        while ptr2 > ptr1:
            sum = numbers[ptr2] + numbers[ptr1]
            if sum > target:
                ptr2 -= 1
            if sum < target:
                ptr1 += 1
            if sum == target:
                return [ptr1 + 1, ptr2 + 1]