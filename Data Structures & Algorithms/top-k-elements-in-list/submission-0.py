class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqTable = {}
        for num in nums:
            freqTable[num] = freqTable.get(num, 0) + 1
        n = len(nums) + 1
        buckets = [[] for _ in range(n)]
        for key, val in freqTable.items():
            buckets[val].append(key)
        buckets.reverse()
        result = []
        for bucket in buckets:
            for element in bucket:
                if len(result) < k:
                    result.append(element)
                else:
                    return result
        return result
            