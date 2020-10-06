# 63. Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # Solution Dynamic Programming

        if obstacleGrid[0][0] == 1:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        for r in range(rows):
            for c in range(cols):

                if r == 0 and c == 0:
                    obstacleGrid[r][c] = 1
                    continue

                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                    continue

                if r == 0:
                    obstacleGrid[r][c] += obstacleGrid[r][c-1]

                elif c == 0:
                    obstacleGrid[r][c] += obstacleGrid[r-1][c]

                else:
                    obstacleGrid[r][c] += (obstacleGrid[r-1]
                                           [c] + obstacleGrid[r][c-1])

        return obstacleGrid[-1][-1]
