class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for str in strs:
            freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for c in str:
                index = ord(c) - 97
                freq[index] += 1
            sol[tuple(freq)].append(str)
        return list(sol.values())