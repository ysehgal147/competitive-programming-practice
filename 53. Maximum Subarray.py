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

# Solution 2. (Kadane's Algorithm)

        curr = nums[0]
        maximum = nums[0]

        for i in nums[1:]:
            curr = max(i, curr+i)
            maximum = max(maximum, curr)
        return maximum
