import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        new = s[::-1]
        if s == new:
            return True
        else:
            return False


        