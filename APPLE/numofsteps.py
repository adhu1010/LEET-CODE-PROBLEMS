class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps

# # Time Complexity: O(log n) in the worst case, as the number is halved in each step when it is even.
# # Space Complexity: O(1) since we are using a constant amount of space for the steps variable.