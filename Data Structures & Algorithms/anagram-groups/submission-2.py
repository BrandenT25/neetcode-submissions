class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for str in strs:
            sortedstr = ''.join(sorted(str))
            sol[sortedstr].append(str)
        return list(sol.values())