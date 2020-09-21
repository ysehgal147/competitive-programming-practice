# 172. Factorial Trailing Zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:

        # Solution 1 (Iteratively)

        zeroCnt = 0
        while n > 0:
            n = n//5
            zeroCnt += n

        return zeroCnt

        # Solution 2 (Recursively)
        
        if n < 5:
            return 0
        else:
            return n//5 + self.trailingZeroes(n//5)
