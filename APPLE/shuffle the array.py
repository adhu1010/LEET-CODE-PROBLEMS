class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
# Time Complexity: O(n) where n is the length of the first half of the input list nums, as we iterate through the first half once.
# Space Complexity: O(n) for storing the resulting list, which has a length of 2n (the original list nums is of length 2n).