class Solution(object):
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                operations += increment
                nums[i] += increment
        return operations
# # Time Complexity: O(n) where n is the length of the input list nums, as we iterate through the list once.
# # Space Complexity: O(1) since we only use a few variables to keep track of the operations and the current index.
## Example usage:
# solution = Solution()