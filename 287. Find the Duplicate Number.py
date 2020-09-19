# 287. Find the Duplicate Number

# Solution 1. (Fast Slow Pointer)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


# Solution 2. (Using Python Count Function)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) > 1:
                return i


# Solution 3. (Using Python Sets)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = set(nums)
        for i in x:
            if nums.count(i) > 1:
                return i

# Solution 4. (Using Python Sets 2)

        x = set()
        for i in nums:
            if i in x:
                return i
            else:
                x.add(i)
