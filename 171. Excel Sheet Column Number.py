# 171. Excel Sheet Column Number

# Solution 1.

class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in s:
            result *= 26
            result += ord(i) - ord('A') + 1
        return result
