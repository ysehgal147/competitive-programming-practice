# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Solution using Mathematics

        nums = nums1 + nums2

        nums.sort()

        if len(nums) % 2 == 0:
            x = len(nums)//2
            y = x - 1
            return (nums[x] + nums[y]) / 2
        else:
            return nums[len(nums)//2]
