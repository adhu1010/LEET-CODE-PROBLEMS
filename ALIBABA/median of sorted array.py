class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l3=nums1+nums2
        l3.sort()
        n=len(l3)
        if n%2==0:
            return ((l3[(n-1)//2]+l3[n//2])/2)
        else:
            return(float(l3[n//2]))

        