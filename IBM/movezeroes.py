def moveZeroes(nums):
    last_non_zero = 0  # Position to place the next non-zero element

    # First pass: move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1

    # Second pass: fill the rest of the array with zeros
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0
        
        
# Example usage:
# nums = [0, 1, 0, 3, 12]
# moveZeroes(nums)
# print(nums)  # Output: [1, 3, 12, 0, 0]
# This function moves all zeroes in the input list `nums` to the end while maintaining the order of non-zero elements.
# The function uses two passes:
# 1. The first pass iterates through the list and moves non-zero elements to the front.
# 2. The second pass fills the remaining positions with zeroes.
# The time complexity is O(n), where n is the length of the input list, as we traverse the list twice.
# The space complexity is O(1) since we are modifying the list in place without using any additional data structures.
# The function is efficient and straightforward, making it suitable for scenarios where we need to rearrange elements in a list while preserving their order.
# The function is designed to be used in scenarios where we need to rearrange elements in a list while preserving their order.
# The code is structured to be clear and maintainable, with appropriate variable names and comments explaining the logic.
# The code is ready for use in competitive programming or interview scenarios where the problem of moving zeroes in an array is presented.
# The function is designed to be efficient and straightforward, making it suitable for scenarios where we need to rearrange elements in a list while preserving their order.

