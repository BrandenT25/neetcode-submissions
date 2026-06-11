class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqTable = {}
        for num in nums:
            freqTable[num] = freqTable.get(num, 0) + 1
        n = len(nums) + 1
        buckets = [[] for _ in range(n)]
        for key, val in freqTable.items():
            buckets[val].append(key)
        result = []

        for i in range(len(buckets)-1, -1, -1):
            for val in (buckets[i]):
                if len(result) < k:
                    result.append(val)
                else:
                    return result
        return result
