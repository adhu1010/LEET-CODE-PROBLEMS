class Solution (object):
    
    def merge(self, intervals):
        if not intervals:
            return []

        # Step 1: Sort intervals by the starting time
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # if merged is empty or no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # there is overlap, so merge the current and previous
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
#Time Complexity: O(n log n) due to sorting
#Space Complexity: O(n) for the merged list
# This code defines a class `Solution` with a method `merge` that merges overlapping intervals from a list of intervals.
