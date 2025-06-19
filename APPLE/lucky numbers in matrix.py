class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = set(min(row) for row in matrix)
        col_maxs = set(max(col) for col in zip(*matrix))
        return list(row_mins & col_maxs)
