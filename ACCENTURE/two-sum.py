class Solution(object):
    def twoSum(nums, target):
        num_map = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []        
# Time Complexity: O(n), where n is the number of elements in nums.
# Space Complexity: O(n), where n is the number of elements in nums.    
# The function iterates through the list nums once, storing each number and its index in a dictionary.
# When it finds a number that, when added to a previously seen number, equals the target, it returns the indices of those two numbers.
# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
# Note: The function assumes that there is exactly one solution and does not handle cases where no solution exists.
# The function twoSum takes a list of integers nums and an integer target as input.
# It returns the indices of the two numbers in nums that add up to target.
# The function uses a dictionary to store the numbers and their indices as it iterates through the list.
# When it finds a number that, when added to a previously seen number, equals the target, it returns the indices of those two numbers.


        