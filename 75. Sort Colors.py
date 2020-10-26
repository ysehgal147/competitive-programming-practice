# 75. Sort Colors

# Solution 1. (String Manipulation)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2


# Solution 2. (3 Pointer Method)    https://www.youtube.com/watch?v=sEQk8xgjx64&t=178s

        zero, one, two = 0, 0, len(nums)-1

        while one <= two:
            if nums[one] == 0:
                nums[one], nums[zero] = nums[zero], nums[one]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            elif nums[one] == 2:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1

# Solution 3. (Using Count Function)

        zeros = nums.count(0)
        for _ in range(zeros):
            nums.remove(0)
            nums.append(0)
        ones = nums.count(1)
        for _ in range(ones):
            nums.remove(1)
            nums.append(1)
        twos = nums.count(2)
        for _ in range(twos):
            nums.remove(2)
            nums.append(2)
