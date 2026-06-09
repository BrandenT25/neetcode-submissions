class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurances = {}
        if len(s) != len(t):
            return False
        for c in s:
            occurances[c] = occurances.get(c, 0) + 1
        for c in t:
            if c not in occurances or occurances[c] == 0:
                return False
            occurances[c] -= 1
        return True

