class Solution(object):
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for token in s.split():
            if token.isdigit():
                num = int(token)
                if num <= prev:
                    return False
                prev = num
        return True
# # Time Complexity: O(n) where n is the length of the string s, as we traverse the string once.
# # Space Complexity: O(1) since we only use a few variables to keep track of the previous number and the current token.