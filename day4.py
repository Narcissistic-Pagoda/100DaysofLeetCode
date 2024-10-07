#valid parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        for i in range(len(s)):
            if s[i] != s[n-1-i]:
                return False
            else:
                return True