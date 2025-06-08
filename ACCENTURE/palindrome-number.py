class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        if y[::-1]==y:
            return True
        else :
            return False
# Time Complexity: O(n), where n is the number of digits in x.
# Space Complexity: O(n), where n is the number of digits in x.
# The function converts the integer x to a string, then checks if the string is equal to its reverse.
# If they are equal, it returns True, indicating that x is a palindrome; otherwise, it returns False.
# Example:
# Input: x = 121
# Output: True
# Input: x = -121
# Output: False
# Input: x = 10
# Output: False
# Note: Negative numbers are not considered palindromes, and single-digit numbers are always palindromes.
# The function handles these cases correctly by checking the string representation of the number.
# The function isPalindrome takes an integer x as input and checks if it is a palindrome.
# A palindrome is a number that reads the same backward as forward.
# The function converts the integer to a string, reverses it, and compares it to the original string.
# If they are the same, it returns True; otherwise, it returns False.