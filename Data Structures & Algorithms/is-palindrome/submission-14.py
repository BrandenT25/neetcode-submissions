class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) -1
        while ptr2 > ptr1:
            while not s[ptr1].isalnum() and ptr1 < ptr2:
                ptr1 += 1
            while not s[ptr2].isalnum() and ptr1 < ptr2:
                ptr2 -=1
            if s[ptr1].lower() != s[ptr2].lower():
                return False
            ptr2 -= 1
            ptr1 += 1
        return True