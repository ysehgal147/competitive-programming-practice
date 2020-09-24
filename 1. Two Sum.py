# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Solution 1. (Hash Map)

        dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dict:
                return [dict[difference], i]
            else:
                dict[nums[i]] = i
