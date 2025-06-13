class Solution(object):
    def findShortestSubArray(self,nums):
        from collections import defaultdict
    
        count = defaultdict(int)
        first_index = {}
        last_index = {}
    
        for i, num in enumerate(nums):
            count[num] += 1
            if num not in first_index:
                first_index[num] = i
            last_index[num] = i

        degree = max(count.values())
        min_length = float('inf')
    
        for num in count:
            if count[num] == degree:
                length = last_index[num] - first_index[num] + 1
                min_length = min(min_length, length)
    
        return min_length
