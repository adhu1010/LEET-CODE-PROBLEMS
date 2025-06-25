class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l3=nums1+nums2
        l3.sort()
        n=len(l3)
        if n%2==0:
            return ((l3[(n-1)//2]+l3[n//2])/2)
        else:
            return(float(l3[n//2]))

# Time Complexity: O((m+n) log(m+n)), where m is the length of nums1 and n is the length of nums2, due to the sorting step.
# Space Complexity: O(m+n) for storing the combined list l3.
# The function combines two sorted arrays, sorts the combined array, and then finds the median.