# 53. Merge Intervals

# Solution 1. (Sorting)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

# Partial Solution. (Brute Force)

    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 1
        intervals.sort()
        while second < len(intervals):
            if intervals[first][1] >= intervals[second][0]:
                intervals[first][1] = max(
                    intervals[second][1], intervals[first][1])
                intervals.pop(second)
            first += 1
            second += 1
        return intervals
