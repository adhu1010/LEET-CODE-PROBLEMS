class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1
        current_len = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1

        return max_len
# Time Complexity: O(n) where n is the length of the string s, as we iterate through the string once.
# Space Complexity: O(1) since we are using a constant amount of space for the variables max_len and current_len, regardless of the input size.S