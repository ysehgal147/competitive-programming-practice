# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Solution 1. (Mathematical)

        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))

        # Solution 2. (Dynamic Programming)

        dp = [[1]*n]*m
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
