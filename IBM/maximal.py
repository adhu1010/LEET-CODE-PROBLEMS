class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(
                            dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                        ) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
    
# This code defines a class `Solution` with a method `maximalSquare` that calculates the area of the largest square containing only '1's in a given binary matrix.
# The method uses dynamic programming to build a 2D array `dp` where `dp[i][j]` represents the side length of the largest square whose bottom-right corner is at `(i, j)`.      
# The maximum side length found is stored in `max_side`, and the area of the largest square is returned as `max_side * max_side`.
# The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the matrix, as we iterate through each cell once.
# The space complexity is also O(m * n) due to the `dp` array used for storing intermediate results.
# The solution handles edge cases where the matrix is empty or has no columns by returning 0 immediately.
# The code is efficient and straightforward, leveraging dynamic programming principles to solve the problem optimally.
# The code is designed to find the largest square of '1's in a binary matrix and return its area.
# The solution is efficient and works well for the problem at hand, ensuring that it handles various edge cases effectively.
# The code is structured to be clear and maintainable, with appropriate variable names and comments explaining the logic.
# The code is ready for use in competitive programming or interview scenarios where the problem of finding the largest square in a binary matrix is presented.
# The code is designed to find the largest square of '1's in a binary matrix and return its area.   
