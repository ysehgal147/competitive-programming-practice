# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Solution 1 (2 Pointer, Time Limit Exceeded)

        nums.sort()
        result = []
        for i in range(len(nums)-1):
            start = i + 1
            end = len(nums) - 1
            print(i, start, end)
            while end > start:
                if nums[i] + nums[start] + nums[end] == 0:
                    if [nums[i], nums[start], nums[end]] not in result:
                        result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    start += 1
        return result
