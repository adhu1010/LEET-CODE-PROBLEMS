class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
# Time Complexity: O(n^2) where n is the length of the input lists nums and index, as we may need to shift elements in the target list for each insertion.
# Space Complexity: O(n) for storing the resulting target list, which can be at most the same length as nums or index.
# Note: This solution is not optimal for large inputs due to the O(n^2) time complexity. A more efficient approach would involve using a different data structure or algorithm to handle insertions more efficiently.