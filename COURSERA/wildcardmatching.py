class Solution (object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # Handle patterns starting with '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[m][n]

# Time Complexity: O(m * n) where m is the length of string s and n is the length of pattern p.
# Space Complexity: O(m * n) for the dp table used to store intermediate results.