# 75. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

# Solution 1. (Append-Remove Method)

        for i in nums2:
            nums1.append(i)
            nums1.remove(0)
        nums1.sort()
        return nums1
        
# Solution 2. (String Manipulation)

        nums1[m:] = nums2[:n]
        nums1.sort()


