# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Solution 1 (Set Approach)

        nums_set = set(nums)
        result = []
        ans = []
        for i in nums_set:
            result.append([nums.count(i), i])
        result.sort()
        result.reverse()
        for j in range(k):
            ans.append(result[j][1])
        return ans
