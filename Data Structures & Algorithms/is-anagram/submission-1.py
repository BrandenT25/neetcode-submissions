class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurances = {}
        if len(s) != len(t):
            return False
        for c in range(len(s)):
            occurances[s[c]] = occurances.get(s[c], 0) + 1
        for c in range(len(t)):
            if not occurances.get(t[c]):
                return False
            if occurances.get(t[c]) == 0:
                return False
            occurances[t[c]] -= 1
        return True

