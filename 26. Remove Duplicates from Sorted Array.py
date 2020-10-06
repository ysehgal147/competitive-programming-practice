# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Solution 1 (Set Approach)

        nums[:] = sorted(set(nums))
        return len(nums)

        # Solution 2 (O(1))

        x = 1
        for i in range(len(nums)-1):
            if(nums[i] != nums[i+1]):
                nums[x] = nums[i+1]
                x += 1
        return(x)
