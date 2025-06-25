class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_from_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # Length of palindrome

        for i in range(len(s)):
            len1 = expand_from_center(i, i)      # Odd-length palindrome
            len2 = expand_from_center(i, i + 1)  # Even-length palindrome
            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

# Time Complexity: O(n^2), where n is the length of the string s, due to the expansion from each character.
# Space Complexity: O(1), as we are using only a few variables for indices and lengths.
# The function finds the longest palindromic substring by expanding around each character and checking both odd and even length palindromes.S