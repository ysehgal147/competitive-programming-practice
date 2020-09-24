# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Solution 1

        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

        # Solution 2

        if not nums:
                return 0

            nums.sort()

            longest_streak = 1
            current_streak = 1

            for i in range(1, len(nums)):
                if nums[i] != nums[i-1]:
                    if nums[i] == nums[i-1]+1:
                        current_streak += 1
                    else:
                        longest_streak = max(longest_streak, current_streak)
                        current_streak = 1

            return max(longest_streak, current_streak)
