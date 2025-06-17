class Solution(object):
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]

#Time Complexity: O(n) where n is the length of the input list nums, as we iterate through the list once.
#Space Complexity: O(n) for storing the resulting list, which has the same length as nums.