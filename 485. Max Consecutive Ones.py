# 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # Solution 1 (O(N))

        arr = []
        count = 0
        ans = 0
        for i in nums:
            if i == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        return ans

        # Solution 2 (O(1))

        count = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0
        return result
