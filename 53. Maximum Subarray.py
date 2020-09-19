# 53. Maximum Subaaray

# Solution 1. (Kadane's Algorithm)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max = -math.inf
        sum = 0

        for i in nums:
            sum += i
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0

        return max
