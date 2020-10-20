# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            array = nums1
            other = nums2
        else:
            array = nums2
            other = nums1
        result = []
        for i in array:
            if i in other:
                if i not in result:
                    result.append(i)
        return result
