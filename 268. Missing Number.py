# 268. Missing Number

# Solution 1. (Using Sets)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for number in range(len(nums) + 1):
            if number not in num_set:
                return number


# Solution 2. (Using Sum of Arithmetic Progression)

        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
