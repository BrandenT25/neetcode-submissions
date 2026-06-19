class Solution:
    def maxArea(self, heights: List[int]) -> int:
        firstPtr = 0
        secondPtr = len(heights) - 1
        highestVolume = 0
        while firstPtr < secondPtr:

            if heights[firstPtr] < heights[secondPtr]:
                volume = heights[firstPtr] * abs(secondPtr - firstPtr)
                firstPtr += 1
                if volume > highestVolume:
                    highestVolume = volume
            elif heights[secondPtr] <= heights[firstPtr]:
                volume = heights[secondPtr] * abs(secondPtr - firstPtr)
                secondPtr -= 1
                if volume > highestVolume:
                    highestVolume = volume
                
        return highestVolume
# [1, 7, 2, 5, 4, 7, 3, 6]
# firstPtr = 1 secondptr = 5        