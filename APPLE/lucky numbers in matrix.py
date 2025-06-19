class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = set(min(row) for row in matrix)
        col_maxs = set(max(col) for col in zip(*matrix))
        return list(row_mins & col_maxs)
# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the matrix, as we need to find the minimum of each row and the maximum of each column.
# Space Complexity: O(m + n) for storing the row minimums and column maximums, where m is the number of rows and n is the number of columns in the matrix.