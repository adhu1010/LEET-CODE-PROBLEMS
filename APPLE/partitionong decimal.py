class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
# # Time Complexity: O(m) where m is the length of the string n, as we iterate through the string once to find the maximum digit.
# # Space Complexity: O(1) since we only use a constant amount of space to store the maximum digit found.