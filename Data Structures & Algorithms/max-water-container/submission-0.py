class Solution:
    def maxArea(self, heights: List[int]) -> int:
        firstPtr = 0
        secondPtr = len(heights) - 1
        highestVolume = 0
        while firstPtr < secondPtr:
            volume = heights[firstPtr] * abs(secondPtr - firstPtr) if heights[firstPtr] < heights[secondPtr] else heights[secondPtr] * abs(secondPtr - firstPtr)
            if volume > highestVolume:
                highestVolume = volume
            if heights[firstPtr] < heights[secondPtr]:
                firstPtr += 1
            elif heights[secondPtr] <= heights[firstPtr]:
                secondPtr -= 1
                
        return highestVolume
# [1, 7, 2, 5, 4, 7, 3, 6]
# firstPtr = 1 secondptr = 5        