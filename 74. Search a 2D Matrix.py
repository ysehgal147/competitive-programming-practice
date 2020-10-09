# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Binary Search Solution

        if matrix == [[]]:
            return 0

        low, high = 0, len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2

            if target in matrix[mid]:
                return 1

            elif matrix[mid][0] >= target:
                high = mid - 1

            else:
                low = mid + 1

        return 0
