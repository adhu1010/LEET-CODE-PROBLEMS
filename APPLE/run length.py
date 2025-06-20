class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            result.extend([val] * freq)
        return result

# Time Complexity: O(n) where n is the length of the input list nums, as we iterate through the list in steps of 2.
# Space Complexity: O(n) for the output list, which can be as large as the sum of all frequencies in nums.