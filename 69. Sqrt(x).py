# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:

        # Binary Search Solution

        if x == 1:
            return 1
        l, r = 0, x
        while l <= r:
            mid = (r+l)//2
            if (mid ^ 2) <= x < (mid+1) ^ 2:
                return mid
            elif x < (mid ^ 2):
                r = mid
            else:
                l = mid
